import wmi
import logging
from datetime import datetime

# Setup logger
logging.basicConfig(filename="usb_log.txt", level=logging.INFO, format='%(asctime)s - %(message)s')
c = wmi.WMI()

def log(msg):
    print(msg)
    logging.info(msg)

def monitor_usb_wmi():
    log("\nStarting USB monitoring with WMI...")
    watcher_insert = c.watch_for(
        notification_type="Creation",
        wmi_class="Win32_USBControllerDevice"
    )
    watcher_remove = c.watch_for(
        notification_type="Deletion",
        wmi_class="Win32_USBControllerDevice"
    )

    while True:
        try:
            inserted = watcher_insert(timeout_ms=1000)
            if inserted:
                log(f"Device Connected: {inserted.Dependent}")
        except wmi.x_wmi_timed_out:
            pass

        try:
            removed = watcher_remove(timeout_ms=1000)
            if removed:
                log(f"Device Disconnected: {removed.Dependent}")
        except wmi.x_wmi_timed_out:
            pass

if __name__ == "__main__":
    monitor_usb_wmi()
