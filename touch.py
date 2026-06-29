import subprocess


def listen_touch(master_serial):
    print(f"Luisteren naar touch-events van {master_serial}...")

    process = subprocess.Popen(
        ["adb", "-s", master_serial, "shell", "getevent", "-lt"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    for line in process.stdout:
        print(line.strip())