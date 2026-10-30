"""Write is_valid_ipv4() to check dotted addresses and look up well-known ports from a dictionary."""

WELL_KNOWN_PORTS = {
    "HTTP": 80,
    "HTTPS": 443,
    "FTP": 21,
    "SSH": 22,
    "SMTP": 25,
    "MySQL": 3306,
}


def is_valid_ipv4(text):
    parts = text.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if int(part) > 255:
            return False
    return True


for address in ["127.0.0.1", "192.168.1.300", "10.0.0", "8.8.8.8", "abc.def.1.2"]:
    print(f"{address:<15} valid: {is_valid_ipv4(address)}")

print()
for protocol, port in sorted(WELL_KNOWN_PORTS.items(), key=lambda item: item[1]):
    print(f"{protocol:<6} -> port {port}")

print()
for name in ["HTTPS", "Telnet"]:
    port = WELL_KNOWN_PORTS.get(name)
    if port is None:
        print(f"{name}: not in the table")
    else:
        print(f"{name}: {port}")
