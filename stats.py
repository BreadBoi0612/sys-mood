import psutil

def get_cpu():
    return psutil.cpu_percent(interval=0.5)

def get_ram():
    return psutil.virtual_memory().percent

def get_disk():
    return psutil.disk_usage("/").percent
