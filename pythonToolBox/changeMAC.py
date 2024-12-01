#! /usr/bin/env python3

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change the MAC address")
    parser.add_option("-m", "--mac", dest="addr", help="new MAC address of the interface")
    (options, arguments) = parser.parse_args()
    if not options.interface:
            parser.error("[-] Please specify an interface, type --help for more info.")
    elif not options.addr:
            parser.error("[-] Please specify an address, type --help for more info")
    return options



def change_mac(interface, addr):
    print("[+] Changing MAC address for " + interface + " to address " + addr)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", addr])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_address(interface):
    ifconfig_output = subprocess.check_output(["ifconfig", interface])
  #  print(ifconfig_output)

    change_mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output.__str__())
    if change_mac_result:
        return (change_mac_result.group(0))
    else:
        print("[-] Could not change the MAC address")

options=get_arguments()


change_mac(options.interface, options.addr)

output=get_current_address(options.interface)
if output==options.addr:
    print("[+] MAC address successfully changed to "+ output)
else:
    print("[-] Could not change the MAC address")