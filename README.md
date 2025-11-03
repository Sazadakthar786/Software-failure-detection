# ✅ Data-Driven Failure Detection and Automatic Recovery using Reinforcement Learning
*A Real-Time Self-Healing System for Software Failures*

---

## 📌 Overview
This project is a **web-based intelligent monitoring and auto-recovery system** that detects software failures, identifies the cause, and repairs the issue using **Reinforcement Learning (RL)**.

Instead of using a fixed dataset, the system **collects real-time computer metrics** (CPU, memory, disk, running processes) and automatically learns the best recovery actions over time.

The dashboard displays:
- ✅ Live system metrics
- ✅ Failure type
- ✅ Affected application
- ✅ Suggested recovery solution
- ✅ RL actions and logs
- ✅ Real-time alerts on failures

---

## ✨ Key Features

### 🔍 1. Real-Time Failure Detection
- Monitors CPU, memory, and disk usage using `psutil`
- Identifies failure types:
  - **CPU Overload**
  - **Memory Leak**
  - **Disk Full**
  - **Normal state**

### 🧠 2. Intelligent Root Cause Identification
- Detects **which application/process** is causing abnormal behavior
- Shows the exact app name on the dashboard

### 🛠️ 3. Automatic Recovery Using RL
- Uses **Stable Baselines3** (PPO/DQN)
- RL agent chooses the best recovery action:
  - Restart service
  - Scale up resources
  - Do nothing (if system stable)
- Learns and improves with continuous feedback

### 🌐 4. Live Web Dashboard
Built using **HTML + CSS + JavaScript + Chart.js**, featuring:
- System health indicators
- Live performance charts
- Failure type card
- Affected application card
- Suggested solution card
- Recovery action logs
- Popup alert notifications
- Buttons for **Train AI**, **Simulate Failure**, and **Recover**

### 💾 5. Local Database Storage
Uses **SQLite** to store:
- Historical metrics
- Failure events
- RL actions & rewards
- Suggested solutions

---

## 🛠️ Technologies Used

### ✅ Backend
- Python
- Flask
- psutil (system monitoring)
- SQLAlchemy
- Stable Baselines3 (Reinforcement Learning)
- SQLite

### ✅ Frontend
- HTML
- CSS
- JavaScript
- Chart.js

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run the app
python app.py

### 5️⃣ Open in your browser
http://127.0.0.1:5000

Now you will see your **live dashboard** 🎉

---

## 🧪 Usage Instructions

▶️ **Train the AI**
Click the Train AI button → RL learns recovery behaviors.

⚠️ **Simulate Failure**
Injects a random CPU/memory/disk spike for testing.

🔄 **Auto Recovery**
Press Recover → RL agent chooses the best fix.

📊 **Live Monitoring**
Charts and info cards update every 5 seconds.

---

## 🧠 How the System Works Internally

✅ **Step 1 — Collect Real-Time Metrics**
Using psutil:
- CPU percent
- Memory percent
- Disk usage
- Process list

✅ **Step 2 — Detect Failure Type**
Using rules & thresholds:
CPU > 90 → CPU Overload
Memory > 85 → Memory Leak
Disk > 90 → Disk Full
Else → Normal

✅ **Step 3 — Identify Affected Application**
Finds the process using the most CPU or memory.

✅ **Step 4 — Suggest Best Solution**
Each failure type has a mapped recovery action (restart, scale, etc.)

✅ **Step 5 — RL Agent Chooses Action**
Environment → State → Action → Reward → Update

✅ **Step 6 — Log Everything**
All actions and metrics are stored in SQLite.

---

## 🔮 Future Scope
- 🧠 Online (continuous) learning for real-time adaptation
- ☁️ Multi-agent RL for distributed cloud systems
- 🔍 Predictive failure detection using ML (LSTM/Random Forest)
- 🤖 Integration with LLMs for smart explanations
- 📱 Mobile app version for remote monitoring
- 🔒 Add network/security failure detection

---

## ✅ Why This Project Is Important
- Software systems fail frequently due to overloads or bugs
- Manual recovery is slow and inefficient
- Traditional monitoring tools use fixed rules
- This project uses data-driven AI to learn, adapt, and recover automatically
- Reduces downtime, improves reliability, and saves maintenance time
- A practical AIOps (AI + DevOps) system used by modern industries

---

## ❤️ Contributors
- Shaik Sazad Akther – AI Engineer & Developer

---

## 📜 License
This project is released under the MIT License.
You may freely modify and distribute it.

---

## ⚙️ requirements.txt
Flask==3.0.3
SQLAlchemy==2.0.30
psutil==5.9.8
stable-baselines3==2.3.2
gymnasium==0.29.1
numpy==1.26.4
pandas==2.2.2
matplotlib==3.9.0
chart-studio==1.1.0
torch==2.2.2

(These versions are stable as of 2025 and compatible with your RL + Flask setup.)

---

## Then run:
git add .
git commit -m "Initial commit - Data-Driven Failure Detection System"
git push origin main
