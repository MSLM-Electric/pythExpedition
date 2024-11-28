import sys
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

import logging

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 4 google.com"
    command = ['ping', param, '2', host]

    s = subprocess.getoutput(' '.join(command))
    logging.info(s)
    print(s)

    return 0 #subprocess.call(command) == 0


#---------------------------------------------------------------#
#TO USE DO command:
#python ip_scan.py 192.168.x.n 255.255.x.0
#x - subAddress
#n - the address from begining. Usually you may begin from zero (n = 0)
#Note: the mask filtering not implemented yet
#---------------------------------------------------------------#

if __name__ == '__main__':
    argumentList = sys.argv
    print(argumentList)
    sysargvLen = len(sys.argv)

    ipaddrToBegin = sys.argv[1]
    maskRange = sys.argv[2]
    #ping(ipaddrToBegin)
    logging.basicConfig(filename='ip_scan.log', level=logging.DEBUG)

    res = ipaddrToBegin.split('.')
    LSBAddrBegin = int(res[3])
    LSBAddrEnd = 255 - LSBAddrBegin
    for toScanByLSBAddr in range(LSBAddrBegin, LSBAddrEnd):
        try:
            ipAddr = res
            ipAddr[3] = str(toScanByLSBAddr)
            ipAddr = '.'.join(ipAddr)
            #if(ping(ipAddr)):
                #logging.info(ipAddr + " get request!")
            ping(ipAddr)
        except :
            print("Error!")
            break
