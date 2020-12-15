#!/usr/bin/env python3
"""List host, Serial, npod name info for SPU's"""
### usage: ./nebGetHosts.py -u myuser
import argparse
import sys
import getpass

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', type=str, required=False)

args = parser.parse_args()
username = args.username       # username to connect on.nebulon.com

try:
    from nebpyclient import NebPyClient
    print("Using NewPyClient")
except ModuleNotFoundError as err:
    # Error handling
    print("Error finding NeyPyClient.  Try 'pip install nebpyclient'")      
### command line arguments

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

client = NebPyClient(username, password)

def getnpodname(uuid):
    npod_list = client.get_npods()
    for npod in npod_list.items:
        #print(f"npod name: {npod.name}, {npod.uuid}")
         if {npod.uuid} == uuid:
             return(npod.name)
                
host_list = client.get_hosts()
print(f"host.name, host.uuid host.board_serial, host.spu_serials, npod_name,")
for host in host_list.items:
    print(f"{host.name}, {host.uuid}, {host.board_serial}, {host.spu_serials}, " + getnpodname({host.npod_uuid}))
