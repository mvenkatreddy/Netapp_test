"""
Problem 1

Parse the two SYSCONFIG-A files in the data folder.
Extract the following:
* System Serial Number
* Model Name (A model name will start with FAS and have 4 numbers after it)
* Extract the name of each PCI card in each slot.  Ignore items in slot 0,
  as those are on the motherboard.
  Note: there may be multiple lines for the same PCI card.
  This is due to having multiple ports on each card.  The PCI card should be listed only once,
  regardless of how many ports are on the card.
* Extract the number of disks on each port.
  A disk adapter port looks something like this (the port number is 7a)
    slot 7: FC Host Adapter 7a (LSI Logic 949E rev. A.1, L-port, <UP>)
  An example disk looks like this:
    16  : NETAPP   X276_FAL9E288F10 NA05 272.0GB 520B/sect (DH07P790548K)

Input:
The input to the script should be the name of the SYSCONFIG-A file.

Output expectations:
The output of the script should be JSON format.
The JSON should contain:
* properties for the model name and serial number
* List of PCI cards.  This list should include the slot number and the description for the card.
* list of each port that have disks and the quantity of disks on that port.

Example output might look like this:
{'model': 'FAS6030', 'disks_per_port':
{'6a': 84, '6b': 84, '7b': 84, '7a': 84, '0a': 56, '2a': 24, '0e': 56, '5a': 84, '5b': 84},
'serial': '1003093853', 'PCICards': {'1': 'NVRAM (NVRAM VI)',
'2': 'SAS Host Adapter 2a (PMC-Sierra PM8001 rev. C, SAS, <UP>)',
'5': 'FC Host Adapter 5a (LSI Logic 949E rev. A.1, L-port, <UP>)',
'7': 'FC Host Adapter 7a (LSI Logic 949E rev. A.1, L-port, <UP>)',
'6': 'FC Host Adapter 6a (LSI Logic 949E rev. A.1, L-port, <UP>)',
'8': 'Dual 10G Ethernet Controller T320E-XFP'}}
"""
# Python modules
import re
import json


def get_pc_details():
    with open("SYSCONFIG-A.1.txt") as input_file:
        file_data = input_file.read()
    data = {
        "model": re.findall("FAS[0-9]{4}", file_data)[0],
        "serial": re.findall("System Serial Number: (\d+)", file_data)[0],
        "PCICards": re.findall("slot ([1-9]+): (.*)\n", file_data),
        "disks_per_port": ""
    }
    return json.dumps(data)

if __name__ == '__main__':
    print get_pc_details()