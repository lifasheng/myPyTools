#!/usr/local/bin/python

import ipaddr

cidrs = [
    "10.0.0.0/18",
    "10.0.64.0/18",
    "10.0.128.0/18",
    "10.0.192.0/20",
    "10.0.208.0/20",
    "10.0.224.0/20"
]

def isSubnetOverlap(cidr1, cidr2):
    subNet1 = ipaddr.IPNetwork(cidr1)
    subNet2 = ipaddr.IPNetwork(cidr2)
    isOverlapped = subNet1.overlaps(subNet2)
    if isOverlapped:
        print("overlapped")
    else:
        print("not overlapped")

for i in range(0, len(cidrs)):
    for j in range(i+1, len(cidrs)):
        #print(cidrs[i], ", ", cidrs[j])
        isSubnetOverlap(cidrs[i], cidrs[j])
