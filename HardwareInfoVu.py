# Embedded file name: /media/build/vti-dorie/build/tmp/work/armv7ahf-vfp-neon-oe-linux-gnueabi/enigma2-python/enigma2-python-vti-15.0.0-20200921-r00r00/git/lib/python/Tools/HardwareInfoVu.py


class HardwareInfoVu:
    device_name = None

    def __init__(self):
        if HardwareInfoVu.device_name is not None:
            return
        else:
            HardwareInfoVu.device_name = 'unknown'
            HardwareInfoVu.vendor_name = 'unknown'
            try:
                file = open('/proc/stb/info/model', 'r')
                HardwareInfoVu.vendor_name = 'octagon'
                HardwareInfoVu.device_name = file.readline().strip()
                file.close()
            except:
                vtilog('hardware detection failed')

            return

    def get_device_name(self):
        return HardwareInfoVu.device_name

    def get_vendor_name(self):
        return HardwareInfoVu.device_name


hwinfo = HardwareInfoVu()
