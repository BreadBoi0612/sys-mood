import psutil
import time

class NetworkMonitor:
    def __init__(self):
        net = psutil.net_io_counters()
        self.last_sent = net.bytes_sent
        self.last_recv = net.bytes_recv
        self.last_time = time.time()

    def get_speed(self):
        now = time.time()
        net = psutil.net_io_counters()

        elapsed = now - self.last_time
        if elapsed <= 0:
            return 0, 0

        up = (net.bytes_sent - self.last_sent) / elapsed
        down = (net.bytes_recv - self.last_recv) / elapsed

        self.last_sent = net.bytes_sent
        self.last_recv = net.bytes_recv
        self.last_time = now

        return up, down


def format_speed(bps):
    if bps < 1024:
        return f"{bps:.0f} B/s"
    elif bps < 1024 ** 2:
        return f"{bps / 1024:.1f} KB/s"
    else:
        return f"{bps / 1024 ** 2:.1f} MB/s"
