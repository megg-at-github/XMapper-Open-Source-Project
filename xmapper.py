import wmi
import socket
import speedtest

st = speedtest.Speedtest()

best_server = st.get_best_server()

download_speed = st.download()
upload_speed = st.upload()

download_speed = round(download_speed / (10**6), 2)
upload_speed = round(upload_speed / (10**6), 2)

import os, re
# run the arp -a command and get the output as a string
arp_output = os.popen('arp -a').read()
# split the output by lines and filter out the empty ones
arp_lines = list(filter(None, arp_output.split('\n')))
# loop through the lines and extract the IP and MAC addresses using regular expressions
devices = []
for line in arp_lines:
    # skip the lines that do not contain an IP address
    if not re.search(r'\d+\.\d+\.\d+\.\d+', line):
        continue
    # find the IP address and the MAC address in the line
    ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
    mac_match = re.search(r'[0-9a-fA-F]{2}(-[0-9a-fA-F]{2}){5}', line)
    # check if the matches are not None before calling the group () method
    if ip_match and mac_match:
        # append a tuple of IP and MAC to the devices list
        devices.append((ip_match.group(), mac_match.group()))
# print the number of devices and their IP and MAC addresses

def get_network_details():
    c = wmi.WMI()
    interfaces = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)

    with open("network_details.txt", "w") as file:
        for interface in interfaces:

            print("=== XMapper ===")
            print("== v1.0 running on Python ==")
            print("=== Net. Data ===")
            print(f"Interface: {interface.Description}")
            print(f"IPv4 Address: {interface.IPAddress[0]}")
            if interface.IPAddress[1]:
                print(f"IPv6 Address: {interface.IPAddress[1]}")
            print(f"MAC ID: {interface.MACAddress}")
            print(f"Default Gateway: {interface.DefaultIPGateway[0]}")
            print(f"Subnet Mask: {interface.IPSubnet[0]}")
            print(f"DNS Servers: {', '.join(interface.DNSServerSearchOrder)}")
            print(f"DHCP Enabled: {interface.DHCPEnabled}")
            print(f"DHCP Server: {interface.DHCPServer}")
            print(f"DHCP Lease Obtained: {interface.DHCPLeaseObtained}")
            print(f"DHCP Lease Expires: {interface.DHCPLeaseExpires}")
            print(f"IP Connection Metric: {interface.IPConnectionMetric}")
            print(f"IP Enabled: {interface.IPEnabled}")
            print(f"IP Connection Metric: {interface.IPConnectionMetric}")
            print(f"IP Subnet: {interface.IPSubnet}")
            print(f"IP Default Gateway: {interface.DefaultIPGateway}")
            print(f"IP DHCP Enabled: {interface.DHCPEnabled}")
            print(f"IP DHCP Server: {interface.DHCPServer}")
            print(f"IP DNS Servers: {interface.DNSServerSearchOrder}")
            print(f"Server: {best_server['host']}")
            print(f"Location: {best_server['name']}, {best_server['country']}")
            print(f"Latency: {best_server['latency']} ms")
            print(f"Download speed: {download_speed} Mbps")
            print(f"Upload speed: {upload_speed} Mbps")
            print(f"There are {len(devices)} devices connected to the network:")
            for device in devices:
                print(f"IP: {device[0]}, MAC: {device[1]}")
                print()

            hostname = socket.gethostname()
            print(f"Hostname: {hostname}")
            
            ip_address = socket.gethostbyname(hostname)
            print(f"IP Address: {ip_address}")


            port = socket.getservbyname("http")
            print(f"Port: {port}")

            protocol = socket.getprotobyname("tcp")
            print(f"Protocol: {protocol}")

            file.write("=== XMapper ===\n")
            file.write("== v1.0 running on Python ==\n")
            file.write("=== Net. Data ===\n")
            file.write(f"Interface: {interface.Description}\n")
            file.write(f"IPv4 Address: {interface.IPAddress[0]}\n")
            if interface.IPAddress[1]:
                file.write(f"IPv6 Address: {interface.IPAddress[1]}\n")
            file.write(f"MAC ID: {interface.MACAddress}\n")
            file.write(f"Default Gateway: {interface.DefaultIPGateway[0]}\n")
            file.write(f"Subnet Mask: {interface.IPSubnet[0]}\n")
            file.write(f"DNS Servers: {', '.join(interface.DNSServerSearchOrder)}\n")
            file.write(f"DHCP Enabled: {interface.DHCPEnabled}\n")
            file.write(f"DHCP Server: {interface.DHCPServer}\n")
            file.write(f"DHCP Lease Obtained: {interface.DHCPLeaseObtained}\n")
            file.write(f"DHCP Lease Expires: {interface.DHCPLeaseExpires}\n")
            file.write(f"IP Connection Metric: {interface.IPConnectionMetric}\n")
            file.write(f"IP Enabled: {interface.IPEnabled}\n")
            file.write(f"IP Connection Metric: {interface.IPConnectionMetric}\n")
            file.write(f"IP Subnet: {interface.IPSubnet}\n")
            file.write(f"IP Default Gateway: {interface.DefaultIPGateway}\n")
            file.write(f"IP DHCP Enabled: {interface.DHCPEnabled}\n")
            file.write(f"IP DNS Servers: {interface.DNSServerSearchOrder}\n")
            file.write(f"Hostname: {hostname}\n")
            file.write(f"IP Address: {ip_address}\n")
            file.write(f"Port: {port}\n")
            file.write(f"Protocol: {protocol}\n")
            file.write(f"Server: {best_server['host']}\n")
            file.write(f"Location: {best_server['name']}, {best_server['country']}\n")
            file.write(f"Latency: {best_server['latency']} ms\n")
            file.write(f"Download speed: {download_speed} Mbps\n")
            file.write(f"Upload speed: {upload_speed} Mbps\n")
            file.write(f"There are {len(devices)} devices connected to the network:")
            for device in devices:
                file.write(f"IP: {device[0]}, MAC: {device[1]}")

    print(f"Network details saved.")

# Get network details and save to a file
XMapper = get_network_details()

