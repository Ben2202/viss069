# viss069

viss069 is a desktop control tool for Android device mirroring and touch synchronization. It detects connected Android devices over ADB, opens scrcpy mirror windows, lets you choose one master device, and forwards touch input from that master to selected follower devices.

The tool is intended for managing multiple Android devices side by side during testing, demos, automation preparation, or repeated workflows where several devices need to follow the same touch actions.

## Features

- Detect connected Android devices through ADB.
- Choose a master device and follower devices.
- Open scrcpy mirror windows for selected devices.
- Start and stop touch synchronization from the GUI.
- Display detected devices as equal-size cards for easier scanning.
- Reuse persistent input injectors for faster event forwarding.

## Requirements

- Python 3
- ADB
- scrcpy
- Root access on follower devices for `sendevent`
- Python packages from `requirements.txt`

## Usage

```bash
pip install -r requirements.txt
python3 main.py
```
