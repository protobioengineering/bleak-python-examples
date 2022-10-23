'''
Minimal Bluetooth LE connection code.

Requires Python3 and the Bleak library.
'''


import asyncio
from bleak import BleakClient, BleakScanner


# Add your device's address here.
# Can be UUID or MAC address
address = 'ABCDEFGG-1111-2222-3333-444455556666'

async def main():
    device = await BleakScanner.find_device_by_address(address)

    async with BleakClient(device) as client:
        print(f'Client connection = {client.is_connected}') # prints True or False

if __name__ == "__main__":
    asyncio.run(main())

