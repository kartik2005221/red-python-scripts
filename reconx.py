import os
import whois
import dns.resolver
import requests


def print_banner():
    print("=" * 50)
    print("         🔍 ReconX - Info Gathering Tool")
    print("=" * 50)


def whois_lookup(domain):
    print("\n[🔎 WHOIS Lookup]")
    try:
        w = whois.whois(domain)
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
    except Exception as e:
        print(f"❌ WHOIS Error: {e}")


def dns_lookup(domain):
    print("\n[🌐 DNS A Record Lookup]")
    try:
        result = dns.resolver.resolve(domain, 'A')
        for ipval in result:
            print(f"IP: {ipval.to_text()}")
    except Exception as e:
        print(f"❌ DNS Error: {e}")


def nmap_scan(target):
    print("\n[⚙️  Nmap Fast Scan (Top 1000 Ports)]")
    try:
        os.system(f"nmap -T4 -F {target}")
    except Exception as e:
        print(f"❌ Nmap Error: {e}")


def subdomain_lookup(domain):
    print("\n[🌐 Subdomain Discovery (crt.sh)]")
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)
        subdomains = set()
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                name = entry['name_value']
                if domain in name:
                    subdomains.add(name)
            for sub in sorted(subdomains):
                print(f" - {sub}")
        else:
            print("❌ crt.sh lookup failed.")
    except Exception as e:
        print(f"❌ Subdomain Error: {e}")


def main():
    print_banner()
    target = input("Enter a domain or IP: ").strip()

    if not target:
        print("⚠️ No target provided.")
        return

    whois_lookup(target)
    dns_lookup(target)
    subdomain_lookup(target)
    nmap_scan(target)


if __name__ == "__main__":
    main()