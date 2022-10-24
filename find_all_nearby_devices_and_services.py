'''
Scan for all BLE devices and print services and characteristics.
'''

import asyncio
import platform
import sys

from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError


class textcolor:
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GOLD = '\033[33m'
    BOLD = '\033[1m'
    END = '\033[0m'

def device_details_to_dict(raw_details):
    # Format device details into string. Accommodate errors caused by lack of data.
    dict_ = {
        'address': None,
        'details': None,
        'metadata': None,
        'name': None,
        'rssi': None
    }
    try:
        dict_['address'] = raw_details.address
    except Exception:
        print(f'Address not found for device with the following data: {raw_details}')
    try:
        dict_['details'] = raw_details.details
    except Exception:
        print(f'Details not found for device with the following data: {raw_details}')
    try:
        dict_['metadata'] = raw_details.metadata
    except Exception:
        print(f'Metadata not found for device with the following data: {raw_details}')
    try:
        dict_['name'] = raw_details.name
    except Exception:
        print(f'Name not found for device with the following data: {raw_details}')
    try:
        dict_['rssi'] = raw_details.rssi
    except Exception:
        print(f'RSSI not found for device with the following data: {raw_details}')

    return dict_




async def main():
    print('///////////////////////////////////////////////')
    print('\t\tDevice scan')
    print('///////////////////////////////////////////////')
    print('Scanning for Bluetooth LE devices...')
    devices = await BleakScanner.discover()
    print(f'Devices found (raw data):\n\t{devices}')
    print(f'Number of devices found: {textcolor.CYAN}{len(list(devices))}{textcolor.END}')
    print(f'Details of devices found:')
    for device in devices:
        device_dict = device_details_to_dict(device)
        print('Device found:')
        print(f'\tAddress: {textcolor.GOLD}{device.address}{textcolor.END}')
        print(f'\tName: {textcolor.GREEN}{device.name}{textcolor.END}')
        print(f'\tDetails: {device.details}')
        print(f'\tMetadata: {device.metadata}')
        print(f'\tRSSI: {device.rssi}')

    print('///////////////////////////////////////////////')
    print('\t\tServices scan')
    print('///////////////////////////////////////////////')
    print('Requesting list of services and characteristics from found Bluetooth LE devices...')
    for device in devices:
        try:
            temp_device = await BleakScanner.find_device_by_address(device.address, timeout=20)
            async with BleakClient(temp_device) as client:
                print('Services found for device')
                print(f'\tDevice address: {textcolor.GOLD}{device.address}{textcolor.END}')
                print(f'\tDevice name: {textcolor.GREEN}{device.name}{textcolor.END}')
                print("\tServices:")
                for service in client.services:
                    print('\t\tService')
                    print(f'\t\tDescription: {textcolor.CYAN}{service.description}{textcolor.END}')
                    print(f'\t\tService: {textcolor.GOLD}{service}{textcolor.END}')

                    characteristics = []
                    for c in service.characteristics:
                        characteristics.append([c.uuid, c.description, c.handle, c.properties])
                    print(f'\t\tCharacteristics: {characteristics}')
        except asyncio.exceptions.TimeoutError:
            print(f'{textcolor.RED}TimeoutError:{textcolor.END} Device at address `{device.address}` timed out.')
        except Exception as error:
            print(f'Exception: An error occurred while connecting to device `{device.address}`:\n\t{error}')


if __name__ == "__main__":
    asyncio.run(main())

