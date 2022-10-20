'''
Bluetooth LE continuous device scanner.

Scan for Bluetooth LE devices continuously and print them as they're found.
This will print many duplicates of the same devices.

Requires Bleak (Bluetooth LE Agnostic Klient)
    - https://github.com/hbldh/bleak
    - https://bleak.readthedocs.io/en/latest/

Example output:
$ python3 continuous_ble_scanner.py
ABCDEFGA-1234-5678-9AAB-BCC112233445: iPad AdvertisementData(local_name='...etc...})
BCC11223-AABB-1234-1234-ABCDEFGABCDE: SmartOven AdvertisementData(local_name='...etc...})
11223344-1111-2222-3333-444445555566: Unknown AdvertisementData(local_name='...etc...})
'''

import asyncio
from bleak import BleakScanner

def on_device_discovery_callback(device, advertisement_data):
    # Print details about device and the advertisement packet it sent out
    print(str(device) + ' ' + str(advertisement_data))

async def main():
    # When BleakScanner finds a device, it will send the device data
    # as arguments to on_device_discovery_callback
    scanner = BleakScanner(on_device_discovery_callback)

    # Start the scanner, print results continuously for 60 seconds, then stop.
    # You can change the sleep() value to however many seconds you want.
    await scanner.start()
    await asyncio.sleep(60.0)
    await scanner.stop()


asyncio.run(main())

