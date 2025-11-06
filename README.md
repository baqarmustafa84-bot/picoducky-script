# PICKODUCKY - macOS Automation Workflow

**One-click workspace setup: Spotify + CapCut + Browser with perfect 50/50 split screen**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-green.svg)](https://pyautogui.readthedocs.io/)
[![PicoDucky](https://img.shields.io/badge/PicoDucky-purple)](https://picoducky.hackclub.com/)

##  Overview

Python script using `pyautogui` to automate macOS workflow setup. Launches **Spotify** (for music), **CapCut** (for video editing), and a **web browser** (Adobe website), then intelligently arranges windows in a 50/50 split screen layout for optimal productivity.

##  Installation

### Standard Python
```bash
pip install pyautogui
python macos_automation.py
```

### PicoDucky Hardware
1. Install CircuitPython on Raspberry Pi Pico
2. Copy `adafruit_hid` library to `/lib` folder  
3. Convert Python script to DuckyScript format
4. Upload to Pico root directory

##  Detailed Automation Steps
1. **Setup** - `pyautogui.FAILSAFE = True` (move mouse to corner to stop)
2. **Launch Spotify** - `cmd+space` → Spotify → `enter`
3. **Search Spotify** - Click center → `cmd+k` → "pyari" → `enter`
4. **Minimize** - `cmd+m` (runs in background)
5. **Launch CapCut** - `cmd+space` → CapCut → `enter`
6. **Launch Browser** - `cmd+space` → `http://adobe.com` → `enter`
7. **Detect Windows** - `find_browser_window()`, `find_window_by_partial_title('CapCut')`
8. **Position CapCut** - Left 50%: `activate()` → `moveTo(0,0)` → `resizeTo(half_width, screen_height)`
9. **Position Browser** - Right 50%: `activate()` → `moveTo(half_width,0)` → `resizeTo(half_width, screen_height)`

##  PicoDucky Implementation

**What is PicoDucky?**  
A Raspberry Pi Pico microcontroller programmed to emulate a USB keyboard.

**How it works:**
1. Plug PicoDucky into macOS computer
2. Device emulates keyboard input automatically
3. Opens Terminal via keyboard commands
4. Downloads and executes Python automation script
5. Your workspace is configured and ready!

##  Configuration Options
```python
SPOTIFY_SEARCH = "pyari"
BROWSER_URL = "http://adobe.com"
MUSIC_APP = "Spotify"
EDITOR_APP = "CapCut"
LAUNCH_DELAY = 2
```

##  Troubleshooting

| Issue | Solution |
|-------|----------|
| Apps won't launch | Verify app names match Spotlight search exactly |
| Windows won't arrange | Enable accessibility: `System Preferences → Security & Privacy → Accessibility` |
| Script runs too fast | Increase `time.sleep()` delay values in code |
| Browser not detected | Ensure default browser is Chrome, Safari, or Firefox |

##  Usage

**Standard Python:**  
```bash
python noducky.py
```

**PicoDucky:**  
Plug in device → Wait 5-10 seconds → Ready to work!

##  Requirements

- **OS**: macOS 10.14 or later
- **Python**: 3.11+
- **Library**: PyAutoGUI
- **Apps**: Spotify, CapCut, Web Browser
- **Permissions**: Accessibility permissions for Terminal/Python

##  License

Free to use and modify for personal automation workflows.

---

**Made for creators 🎨**
