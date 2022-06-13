import re
HOST = 'devasc-iosxe-mgmt-1.cisco.com'
USER = 'developer'
PASS = 'CactusMopedGreen42'
PORT = 830
NATIVE_NS = "{http://cisco.com/ns/yang/Cisco-IOS-XE-native}"

NATIVE_PATTERN = re.compile(NATIVE_NS)
NAT_INT_PATTERN = re.compile(NATIVE_NS+"interface")