'''
Bluetooth LE one-time device scanner.

Scan for Bluetooth LE devices for 5 seconds, print
all found devices, then quit.

Requires Bleak (Bluetooth LE Agnostic Klient)
    - https://github.com/hbldh/bleak
    - https://bleak.readthedocs.io/en/latest/

Example output:
    $ python3 static_ble_scanner.py
    ABCDEFGA-1234-5678-9AAB-BCC112233445: iPad
    BCC11223-AABB-1234-1234-ABCDEFGABCDE: SmartOven
    11223344-1111-2222-3333-444445555566: Unknown
'''

import asyncio
from bleak import BleakScanner


async def main():
    devices = await BleakScanner.discover()
    for device in devices:
        print(device)


if __name__ == "__main__":
    asyncio.run(main())

