import subprocess
import ipaddress
import concurrent.futures

def ping_ip(ip):
    result = subprocess.call(['ping', '-c', '1', '-W', '0.2', str(ip)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return ip if result != 0 else None

def find_free_ip_management_subnet(cnt):
    free_ips = []
    start_ip = ipaddress.ip_address('10.196.149.52')
    end_ip = ipaddress.ip_address('10.196.149.126')
    ips_to_ping = [str(ip) for ip in range(int(start_ip), int(end_ip) + 1)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(ping_ip, str(ipaddress.ip_address(ip))): ip for ip in range(int(start_ip), int(end_ip) + 1)}
        for future in concurrent.futures.as_completed(futures):
            ip = futures[future]
            if future.result() is not None:
                free_ips.append(ipaddress.ip_address(ip))
                if len(free_ips) >= int(cnt):
                    break

    return free_ips

def find_free_ip_data_vlans(vlan, cnt):
    free_ips = []
    start_ip = ipaddress.ip_address(f'192.168.{vlan}.0')
    end_ip = ipaddress.ip_address(f'192.168.{vlan}.254')
    ips_to_ping = [str(ip) for ip in range(int(start_ip), int(end_ip) + 1)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(ping_ip, str(ipaddress.ip_address(ip))): ip for ip in range(int(start_ip), int(end_ip) + 1)}
        for future in concurrent.futures.as_completed(futures):
            ip = futures[future]
            if future.result() is not None:
                free_ips.append(ipaddress.ip_address(ip))
                if len(free_ips) >= int(cnt):
                    break

    return free_ips


def main():
    print("Options:")
    print("1) Find free IP in management subnet")
    print("2) Find free IP from data VLANs")

    option = input("Enter your choice: ").strip().lower()
    ip_cnt = input("Number of IPs needed: ").strip().lower()
    if option == '1':
        free_ips = find_free_ip_management_subnet(ip_cnt)
        print("Free IPs in management subnet:")
        for ip in free_ips:
            print(ip)
    elif option == '2':
        vlan = input("Enter VLAN ID: ").strip()
        free_ips = find_free_ip_data_vlans(vlan, ip_cnt)
        print("Free IPs in data VLAN:")
        for ip in free_ips:
            print(ip)
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
