import psutil
import time
import logging

logging.basicConfig(filename='system.log', level=logging.INFO)

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk

def check_thresholds(cpu, memory, disk):
    if cpu > 80:
        logging.warning(f"High CPU Usage: {cpu}%")
    if memory > 80:
        logging.warning(f"High Memory Usage: {memory}%")
    if disk > 80:
        logging.warning(f"High Disk Usage: {disk}%")

def monitor():
    while True:
        cpu, memory, disk = get_system_stats()
        print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")
        check_thresholds(cpu, memory, disk)
        time.sleep(5)

if __name__ == "__main__":
    monitor()
