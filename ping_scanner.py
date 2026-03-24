import subprocess
import platform

host = input("Enter IP address: ")

if platform.system() == "Windows":
    command = ["ping", "-n", "1", host]
else:
    command = ["ping", "-c", "1", host]

result = subprocess.run(command, capture_output=True, text=True)

if result.returncode == 0:
    print("Host is UP")
    print(result.stdout)
else:
    print("Host is DOWN")