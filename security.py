import psutil
import os

def system_status():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    return cpu, ram

def usb_devices():
    devices = []
    for d in psutil.disk_partitions():
        if 'removable' in d.opts:
            devices.append(d.device)
    return devices

def block_usb():
    os.system(
        'reg add HKLM\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR '
        '/v Start /t REG_DWORD /d 4 /f'
    )

def kill_process(name):
    for p in psutil.process_iter(['pid', 'name']):
        if name.lower() in p.info['name'].lower():
            psutil.Process(p.info['pid']).terminate()
