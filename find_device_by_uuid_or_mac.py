'''
Bluetooth LE device finder.

Find a Bluetooth LE device by its MAC address or UUID.

Requires Bleak (Bluetooth LE Agnostic Klient)
    - https://github.com/hbldh/bleak
    - https://bleak.readthedocs.io/en/latest/

Example output:
    $ python3 find_device_by_uuid_or_mac.py
    Device found:
    Address: ABCDEFGA-1234-5678-9AAB-BCC112233445
    Device name: iPad
    RSSI: -93
    Metadata: {'uuids': ...etc...}
    Details: <CBPeripheral: ...etc...>
'''

import asyncio
import sys
from bleak import BleakScanner


'''
Below is an example UUID address.

`address` can be a MAC address or a UUID. UUIDs are most likely to work on macOS.
MAC address format = aa:bb:cc:12:34:56
UUID format = ABCDEFGG-1111-2222-3333-444455556666
'''
address = 'ABCDEFGA-1234-5678-9AAB-BCC112233445'


async def main(address):
    device = await BleakScanner.find_device_by_address(address)
    if(device == None):
        print(f'A Bluetooth LE device with the address `{address}` was not found.')
    else:
        print('Device found:')
        print(f'Address: {device.address}')
        print(f'Device name: {device.name}')
        print(f'RSSI: {device.rssi}')
        print(f'Metadata: {device.metadata}')
        print(f'Details: {device.details}')


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) == 2 else address))

