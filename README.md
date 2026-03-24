This project is about creating simple network scanning tools using Python.
I have implemented three types of scanners. The first one is a ping scanner, which is used to check whether a system is active or not. The second one is an ARP scanner, which helps to find devices connected in the same network along with their IP and MAC addresses. The third one is an Nmap scanner, which is used to scan open ports in a system.

Ping Scanner (ping_scanner.py): The ping scanner is used to check whether a particular host or system is reachable over the network. It works by sending a ping request and waiting for a response from the target. This tool can handle both single IP addresses and multiple inputs, making it flexible to use. It is designed to work across different operating systems like Windows, Linux, and Mac by adjusting the command internally. The output shows whether the host is active along with the response time, which helps in understanding the speed of the connection.

ARP Scanner (arp_scanner.py): The ARP scanner is used to identify devices connected within the same local network. It sends ARP requests to all devices in the network range and collects their responses. Based on these responses, the script displays the IP address and corresponding MAC address of each device. This helps in understanding how many devices are currently active and connected. The output is shown in a simple and clear format, making it easy to read and analyze.

Nmap Scanner (nmap_scanner.py): The Nmap scanner is used to perform port scanning on a target system. It works by using the Nmap tool through Python to identify open ports and check the status of services running on those ports. This helps in understanding which services are accessible on a system. The scanner performs the process efficiently and provides the results without delay. It is useful for basic network analysis and gives an idea about system exposure in a network.

To run the project:
•	Run ping_scanner.py to check active hosts

•	Run arp_scanner.py to find devices in network

•	Run nmap_scanner.py to scan open ports

Screenshots of the outputs are also added in this repository for reference.

During the implementation, I also understood how different tools and libraries work together. I used Python along with modules like subprocess and scapy, and also worked with Nmap for port scanning. This gave me practical exposure to basic network analysis and helped me understand how these concepts are applied in real-time. This project helped me understand basic networking concepts and how scanning works in cybersecurity.

Overall, this project improved my understanding of networking as well as my confidence in writing simple automation scripts.

