# Embedded file name: /media/build/vti-dorie/build/tmp/work/armv7ahf-vfp-neon-oe-linux-gnueabi/enigma2-python/enigma2-python-vti-15.0.0-20200921-r00r00/git/lib/python/Tools/HardwareInfo.py
import os

class HardwareInfo:
    device_name = None
    vu_device_name = None
    chip_name = None

    def __init__(self):
        if HardwareInfo.chip_name is None:
            HardwareInfo.chip_name = 'unknown'
            try:
                file = open('/proc/stb/info/chipset', 'r')
                HardwareInfo.chip_name = file.readline().strip()
                file.close()
            except:
                vtilog('[HardwareInfo] unable to fetch SoC info')

        if HardwareInfo.device_name is not None:
            return
        else:
            HardwareInfo.device_name = 'unknown'
            try:
                file = open('/proc/stb/info/model', 'r')
                HardwareInfo.device_name = file.readline().strip()
                file.close()
            except:
                vtilog('[HardwareInfo] ----------------')
                vtilog('you should upgrade to new drivers for the hardware detection to work properly')
                vtilog('[HardwareInfo] ----------------')
                vtilog('fallback to detect hardware via /proc/cpuinfo!!')
                try:
                    rd = open('/proc/cpuinfo', 'r').read()
                    if rd.find('hi3789mv200') != -1:
                        HardwareInfo.device_name = 'dm8000'
                        vtilog('dm8000 detected!')
                    elif rd.find('Brcm7401 V0.0') != -1:
                        HardwareInfo.device_name = 'dm800'
                        vtilog('dm800 detected!')
                    elif rd.find('MIPS 4KEc V4.8') != -1:
                        HardwareInfo.device_name = 'dm7025'
                        vtilog('dm7025 detected!')
                except:
                    pass

            HardwareInfo.vu_device_name = 'unknown'
            vumodel_path = '/proc/stb/info/model'
            if os.access(vumodel_path, os.F_OK):
                HardwareInfo.vu_device_name = open(vumodel_path, 'r').read().strip()
            return

    def get_device_name(self):
        return HardwareInfo.device_name

    def get_chip_name(self):
        return HardwareInfo.chip_name

    def get_vu_device_name(self):
        return HardwareInfo.vu_device_name

    def get_friendly_name(self):
        devices = {'bm750': 'Duo',
         'solo': 'Solo',
         'uno': 'Uno',
         'ultimo': 'Ultimo',
         'solo2': 'Solo2',
         'duo2': 'Duo2',
         'solose': 'Solo SE',
         'zero': 'Zero',
         'solo4k': 'Solo 4K',
         'uno4k': 'Uno 4K',
         'ultimo4k': 'Ultimo 4K',
         'uno4kse': 'Uno 4K SE',
         'zero4k': 'Zero 4K',
         'duo4k': 'Duo 4K',
         'duo4kse': 'Duo 4K SE'}
        if devices.has_key(HardwareInfo.vu_device_name):
            return devices[HardwareInfo.vu_device_name]
        else:
            return 'Vu+ STB'
