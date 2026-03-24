import nmap

target = input("Enter IP address: ")
scanner = nmap.PortScanner(nmap_search_path=('C:\\Program Files (x86)\\Nmap\\nmap.exe',))

print("Scanning... please wait ⏳")

scanner.scan(target, arguments='-F')

for host in scanner.all_hosts():
    print("\nHost:", host)
    print("State:", scanner[host].state())

    for proto in scanner[host].all_protocols():
        print("Protocol:", proto)

        ports = scanner[host][proto].keys()
        for port in ports:
            print("Port:", port, "State:", scanner[host][proto][port]['state'])