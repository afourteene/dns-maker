#! /bin/python3

import re
import sys
from colorama import Fore, Back, Style
import config.zones
systemArgs = sys.argv

description = """
| Option | Description |
| ------ | ----------- |
| zone   | start to create zone file|
| rev-zone | start to create reverse zone file |
"""

del systemArgs[0]



def zone():
        domain ,ip,ns1,ns2 = input("enter your domain and your ns records with a space : ").split()
        fileName = input("enter your file name : ")
        zoneStr = config.zones.zone.format(domain = domain,ip = ip,ns1 = ns1,ns2 = ns2)
        newZoneFile = open('./outputs/'+fileName,'w')
        newZoneFile.write(zoneStr)
        print(Fore.GREEN+'file created successfuly!')

def reversZone():
        domain ,reverseIp,ns1,ns2,lastIp = input("enter your domain and your ns records and last part of your ipwith a space : ").split()
        reverseZoneStr = config.zones.reverseZone.format(domain = domain,revIp = reverseIp,ns1 = ns1,ns2 = ns2 ,lastIpPart = lastIp)
        fileName = input("enter your file name : ")
        newZoneFile = open('./outputs/'+fileName,'w')
        newZoneFile.write(reverseZoneStr)
        print(Fore.GREEN+'file created successfuly!')


try:
    if(systemArgs[0] == "zone"):
          zone()
    elif(systemArgs[0] == "rev-zone"):
          reversZone()
    else:
          print(description)
except:
    print(Fore.RED+'used wrong option')



