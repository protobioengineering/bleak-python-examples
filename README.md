# Bleak Bluetooth LE Python Examples for macOS

Example code for connecting to Bluetooth LE devices with Python and [Bleak](https://github.com/hbldh/bleak) (a Bluetooth LE library) on macOS.

## Requirements

* Python 3 (tested with 3.9.6)
* [Bleak](https://github.com/hbldh/bleak) (tested with 0.18.1)
* MacOS 12.0+

Might work with other versions of Python and Bleak. See [Bleak Issues](https://github.com/hbldh/bleak/issues) for troubleshooting help.

## Examples

* [Find all Bluetooth LE devices near me (one-time)](https://github.com/protobioengineering/bleak-python-examples/blob/main/static_ble_scanner.py)
* [Find all Bluetooth LE devices near me (continuous)](https://github.com/protobioengineering/bleak-python-examples/blob/main/continuous_ble_scanner.py)
* [Find a Bluetooth LE device by UUID or MAC address](https://github.com/protobioengineering/bleak-python-examples/blob/main/find_device_by_uuid_or_mac.py)
* [Connect to and disconnect from a Bluetooth LE device by UUID or MAC address](https://github.com/protobioengineering/bleak-python-examples/blob/main/connect_to_ble_device_by_uuid_or_mac.py)