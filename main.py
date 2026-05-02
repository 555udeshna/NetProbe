from netprobe.ping import ping_host
from netprobe.scanner import scan_ports
from netprobe.dns_lookup import dns_lookup
from netprobe.utils import print_banner

COMMON_PORTS = [21, 22, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

def main():
    print_banner()
    target = input("Enter target (IP or domain): ").strip()

    print("\n[+] Checking host availability...")
    if ping_host(target):
        print("[✔] Host is UP")
    else:
        print("[✘] Host is DOWN")
        return

    print("\n[+] Scanning common ports...")
    open_ports = scan_ports(target, COMMON_PORTS)

    if open_ports:
        print(f"[✔] Open ports: {open_ports}")
    else:
        print("[✘] No open ports found")

    print("\n[+] Performing DNS lookup...")
    ips = dns_lookup(target)

    if ips:
        print(f"[✔] IP Addresses: {ips}")
    else:
        print("[✘] No DNS records found")

if __name__ == "__main__":
    main()
