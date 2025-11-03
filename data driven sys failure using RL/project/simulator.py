import psutil
import random
import time
import os
from datetime import datetime
from models import Metric
from collections import deque

# Maintain rolling windows for adaptive detection
CPU_WINDOW = deque(maxlen=60)
MEM_WINDOW = deque(maxlen=60)


def read_current_metrics():
    cpu = float(psutil.cpu_percent(interval=0.1))
    memory = float(psutil.virtual_memory().percent)
    # Disk usage for root filesystem
    try:
        disk = float(psutil.disk_usage('/').percent)
    except Exception:
        disk = 0.0
    status = 'Healthy'
    # Introduce random transient spikes to simulate occasional issues
    if random.random() < 0.05:
        cpu = min(100.0, cpu + random.uniform(20, 50))
    if random.random() < 0.05:
        memory = min(100.0, memory + random.uniform(20, 50))
    # Update windows
    CPU_WINDOW.append(cpu)
    MEM_WINDOW.append(memory)
    # Adaptive thresholding using mean + 2*std when enough history exists
    import numpy as _np
    if len(CPU_WINDOW) >= 10 and len(MEM_WINDOW) >= 10:
        cpu_mean, cpu_std = _np.mean(CPU_WINDOW), _np.std(CPU_WINDOW)
        mem_mean, mem_std = _np.mean(MEM_WINDOW), _np.std(MEM_WINDOW)
        cpu_thresh = cpu_mean + 2 * max(cpu_std, 1e-3)
        mem_thresh = mem_mean + 2 * max(mem_std, 1e-3)
        if cpu >= cpu_thresh or memory >= mem_thresh:
            status = 'Failed'
    else:
        if cpu >= 90.0 or memory >= 90.0:
            status = 'Failed'
    return cpu, memory, disk, status


def simulate_failure_metric():
    # Force a failure metric
    cpu = random.uniform(90.0, 100.0)
    memory = random.uniform(90.0, 100.0)
    return Metric(timestamp=datetime.utcnow(), cpu=cpu, memory=memory, disk=95.0, status='Failed')


def detect_failure(cpu: float, memory: float, disk: float):
    """Determine failure type, identify top offending process, and suggest a solution.

    Uses a short sampling window to get meaningful per-process CPU percentages.
    """
    try:
        this_pid = os.getpid()

        if cpu is not None and cpu > 90:
            # Sample per-process CPU over a short interval for accuracy
            procs = [p for p in psutil.process_iter(['pid', 'name'])]
            for p in procs:
                try:
                    p.cpu_percent(None)
                except Exception:
                    pass
            time.sleep(0.1)
            top_name = 'Unknown'
            top_val = -1.0
            for p in procs:
                try:
                    if p.pid == this_pid:
                        continue
                    val = p.cpu_percent(None)
                    if val is not None and val > top_val:
                        top_val = val
                        top_name = p.info.get('name') or p.name() or f'pid-{p.pid}'
                except Exception:
                    continue
            return "CPU Overload", top_name, "Restart the service or reduce load"

        if memory is not None and memory > 85:
            top_name = 'Unknown'
            top_val = -1.0
            for p in psutil.process_iter(['pid', 'name', 'memory_percent']):
                try:
                    if p.pid == this_pid:
                        continue
                    val = p.info.get('memory_percent')
                    if val is None:
                        continue
                    if val > top_val:
                        top_val = val
                        top_name = p.info.get('name') or f'pid-{p.pid}'
                except Exception:
                    continue
            return "Memory Leak", top_name, "Scale up memory or restart app"

        if disk is not None and disk > 90:
            return "Disk Full", "System Storage", "Clear temporary files or expand storage"

        return "Normal", "None", "System stable"
    except Exception:
        return "Unknown", "Unknown", "Investigate system logs"
