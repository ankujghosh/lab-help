# Free IP Finder

This Python script helps you find free IP addresses within a given subnet or VLAN. It uses ICMP echo requests (ping) to check the availability of IP addresses.

## Prerequisites

- Python 3.x
- `ipaddress` module (usually included in Python standard library)
- `concurrent.futures` module (usually included in Python standard library)

## Usage

1. Clone the repository or download the script file.
2. Run the script using Python:

    ```bash
    python free_ip_finder.py
    ```

3. Follow the on-screen prompts to choose the option and specify the number of IPs needed.

## Options

### 1. Find Free IP in Management Subnet

This option finds free IP addresses within a specified management subnet.

### 2. Find Free IP from Data VLANs

This option finds free IP addresses within specified data VLANs.

## How It Works

The script sends ICMP echo requests (pings) to each IP address within the specified range. If an IP address responds, it's considered unavailable. If an IP address does not respond within a timeout period, it's considered available and added to the list of free IPs.

## Note

- The script uses ICMP echo requests, so make sure ICMP traffic is allowed in your network environment.
- The availability of IP addresses may depend on various factors such as network configuration, firewall rules, and device availability.

---

Feel free to customize the README further with additional information, usage examples, or installation instructions as needed.
