import ipaddress
import boto3

#ip = '192.168.1.15'
#subnet_mask = '/18'
print("enter the Ip Address")
ip = input()
print(" enter  subnetmask  ")
subnet_mask = input()
network = ipaddress.IPv4Network(ip + "/" + subnet_mask, strict=False)
print(f"Network Address: {network.network_address}")
print(f"Broadcast Address: {network.broadcast_address}")
print(f"Total Hosts: {network.num_addresses-2}")  # exclude network and broadcast address
print(f"Valid Host Range: {network.network_address + 1} - {network.broadcast_address - 1}")
print(f"Next Subnet : {network.broadcast_address+1}")


