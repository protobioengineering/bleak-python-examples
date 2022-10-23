'''
Connect to Bluetooth LE device by UUID or MAC address.

Requires Bleak (Bluetooth LE Agnostic Klient)
    - https://github.com/hbldh/bleak
    - https://bleak.readthedocs.io/en/latest/

Example output:
    $ python3 connect_to_ble_device_by_uuid.py

'''

import asyncio
import sys

from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError


'''
Below is an example UUID address.

`address` can be a MAC address or a UUID. UUIDs are most likely to work on macOS.
MAC address format = aa:bb:cc:12:34:56
UUID format = ABCDEFGG-1111-2222-3333-444455556666
'''
address = 'ABCDEFGA-1234-5678-9AAB-BCC112233445'


'''
The real difference between this and find_device_by_uuid_or_mac.py is the use
of BleakClient via `async with BleakClient(device) as client:` (line 40)
'''
async def main(ble_address):
    print(f'Looking for Bluetooth LE device at address `{ble_address}`...')
    device = await BleakScanner.find_device_by_address(ble_address, timeout=20.0)
    if(device == None):
        print(f'A Bluetooth LE device with the address `{ble_address}` was not found.')
    else:
        print(f'Client found at address: {ble_address}')
        print(f'Connecting...')

        # This `async` block starts and keeps the Bluetooth LE device connection.
        # Once the `async` block exits, BLE device automatically disconnects.
        async with BleakClient(device) as client:
            print(f'Client connection = {client.is_connected}')

        print(f'Disconnected from `{ble_address}`')

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) == 2 else address))

