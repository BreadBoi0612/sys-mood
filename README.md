# SysMood 😎🔥

SysMood is a fun, personality-driven **Linux terminal system monitor** built with Python and Rich.  
It shows live system stats like CPU, RAM, disk usage, and network speeds — and gives your system a *mood* based on how stressed it is.

Because system monitors don’t have to be boring.

---

## ✨ Features

- 📊 Live CPU, RAM, and disk usage
- 🌐 Real-time upload & download speeds
- 😎 Emoji-based system mood
- 🎨 Clean, colorful terminal UI
- ⚡ Lightweight and fast
- 🐧 Works on any Linux distro

---

## 🖥️ Preview

😐 System Mood: Stressed

[ CPU ] ██████████░░░░░░░░░░ 63%

[ RAM ] ████████░░░░░░░░░░░░ 48%

[ DISK ] ███████████░░░░░░░░ 71%

Network
⬆ Upload: 320 KB/s
⬇ Download: 1.4 MB/s

---

## 📦 Requirements

- Python 3.9+
- Linux
- Terminal with Unicode support

Python libraries:
- `psutil`
- `rich`

---


## 🚀 Installation

```bash
git clone https://github.com/BreadBoi0612/sys-mood.git
cd sys-mood
pip install -r requirements.txt
python main.py
```
# To Install pip:
```bash
sudo pacman -Syu
sudo pacman -S python-pip
```

## 🧠 How It Works

SysMood calculates system load in real time and assigns a mood based on CPU and RAM usage:

- Load	Mood
- < 30%	😎 Chillin
- 30–60%	🙂 Working
- 60–80%	😐 Stressed
- 80%+	🔥 PANIC

Network speeds are calculated by tracking byte deltas over time using psutil.

## 🛠️ Built With

- Python

- Rich

- psutil

## 🔮 Roadmap

 Per-interface network stats

 Graph history (last 60 seconds)

 Config file + themes

 Network stress affects mood

 Package for Linux distros
