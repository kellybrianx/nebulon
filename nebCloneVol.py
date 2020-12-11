#!/usr/bin/env python3
"""Find volume and create clone"""
### usage: ./nebCloneVol.py -u myuser [-p mypassword] -s vmware_00 -d vmware_00clone
import argparse
import sys
import getpass
from nebpyclient import NebPyClient
### command line arguments

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', type=str, required=False)
parser.add_argument('-s', '--sourcevolume', type=str, required=True)
parser.add_argument('-d', '--destvol', type=str, required=True)

args = parser.parse_args()
username = args.username       # username to connect on.nebulon.com
sourcevol = args.sourcevolume  # Friendly name of source volume
destvol = args.destvol         # name of destination volume

try:
    import config
    print("..using auth config file for connection strings")
    username = config.username
    password = config.password
except ModuleNotFoundError as err:
    # Error handling
    print("auth config not found, using command args")
    username = args.username
    try:
        password = getpass.getpass()
    except Exception as error:
        print('ERROR', error)

def clonevolume(source, dest):
    client.create_clone(dest,source)

client = NebPyClient(username, password)

vol_list = client.get_volumes()
#print("uuid, lun_id, spu_serial, volume_uuid")
for vol in vol_list.items:
    if vol.name == sourcevol:
        print(f"Found matching source volume {sourcevol} , cloning to {destvol}")
        clonevolume(vol.uuid,destvol)
        

