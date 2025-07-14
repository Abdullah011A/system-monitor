import psutil
import platform
import time
from datetime import datetime

def get_uptime():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()
    uptime = now - boot_time
    return str(uptime).split('.')[0]

def main():
    print("="*40)
    print("🖥️  System Monitor")
    print("="*40)

    print(f"System: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print(f"Uptime: {get_uptime()}")
    print("-"*40)

    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")

    print("="*40)

if __name__ == "__main__":
    main()
