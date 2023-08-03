#! /bin/python3

import re
import sys


systemArgs = sys.argv

#remove file name from list 

del systemArgs[0]


ipPattern = 'your-ip'
domainPattern = 'your-domain'
lastIpPattern = 'last'
revIpPattern = 'rev-ip'
zoneFile = open('./files/db.local.txt', 'r')
revZoneFile = open('./files/rev.db.local.txt', 'r')
checkIpPattern = '[0-9]+.[0-9]+.[0-9]+.[0-9]+.'
checkDomainPattern = '[a-zA-Z0-9]+.com.|[a-zA-Z0-9]+.[a-zA-Z]+.com.'
checkRevIpPattern = '[0-9]+.[0-9]+.[0-9]+'
checkLastpartIp = '[0-9]{3}'


def replaceIp(pattern,ip,data):
    setIp = re.sub(pattern,ip,data)
    return setIp

def replaceDomain(pattern,domain,data):
    setdomain = re.sub(pattern,domain,data)
    return setdomain
    
def replaceLastPartIp(pattern,domain,data):
    setRevIp = re.sub(pattern,domain,data)
    return setRevIp





if(systemArgs[0] == 'zone'):
    domain,ipAddress = input('entar your domain like this (domain.example.com.) and your ip address please seperate them with a space : ').split()
    fileName = input('enter your file name : ')
    if(re.match(checkIpPattern,ipAddress) and re.match(checkDomainPattern,domain) ):

        ipWasSet = replaceIp(ipPattern,ipAddress,zoneFile.read())

        domainWasSet = replaceDomain(domainPattern,domain,ipWasSet)

        newZoneFile = open('./output/'+fileName,'w')

        newZoneFile.write(domainWasSet)
    else:
        print('please check your ip address and domain dictation and retry again.')

elif(systemArgs[0] == 'rev-zone'):
        
                     
        domain,revIpAddress = input('entar your domain like this (domain.example.com.) and your rev-ip address please seperate them with a space : ').split()
        lastPartIp = input('enter last part of your ip : ')
        
            

        fileName = input('enter your file name : ')
        if(re.match(checkLastpartIp,lastPartIp) and re.match(checkRevIpPattern,revIpAddress) and re.match(checkDomainPattern,domain)):
             RevIpWasSet = replaceIp(revIpPattern,revIpAddress,revZoneFile.read())
             domainWasSet = replaceDomain(domainPattern,domain,RevIpWasSet)
             lastIpWasSet = replaceLastPartIp(lastIpPattern,lastPartIp,domainWasSet)
             
             newRevZonFile = open('./output/'+fileName,'w')
             newRevZonFile.write(lastIpWasSet)
        else:
             print('please check your inputs and try again')

else:
     print('wrong option used!')


