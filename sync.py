import threading
from touch import listen_touch

running = False


def start_sync(master, followers):
    global running

    if running:
        return

    running = True

    print("=" * 50)
    print("SYNC GESTART")
    print("MASTER    :", master)
    print("FOLLOWERS :", followers)
    print("=" * 50)

    thread = threading.Thread(
        target=sync_loop,
        args=(master, followers),
        daemon=True
    )
    thread.start()


def stop_sync():
    global running
    running = False
    print("SYNC GESTOPT")


def sync_loop(master, followers):
    listen_touch(master)

    while running:
        pass