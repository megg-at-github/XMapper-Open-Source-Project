import wmi
import socket
import speedtest
import subprocess

st = speedtest.Speedtest()

best_server = st.get_best_server()

download_speed = st.download()
upload_speed = st.upload()

download_speed = round(download_speed / (10**6), 2)
upload_speed = round(upload_speed / (10**6), 2)

def get_connected_device_count():
    # Execute the ARP command and capture the output
    arp_output = subprocess.check_output(['arp', '-a']).decode('utf-8')

    # Count the number of unique MAC addresses in the ARP output
    mac_addresses = set()
    for line in arp_output.splitlines():
        if 'dynamic' in line.lower():
            mac_address = line.split()[1]
            mac_addresses.add(mac_address)

    return len(mac_addresses)

# Get the count of connected devices
device_count = get_connected_device_count()

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
            print(f"Number of devices connected to the network: {device_count}")
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
            file.write(f"Number of devices connected to the network: {device_count}")
    print(f"Network details saved.")

# Get network details and save to a file
XMapper = get_network_details()


        
