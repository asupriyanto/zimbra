import socket
import sys

# Daftar penyedia blacklist (DNSBL)
BLACKLIST_SERVERS = [
    "zen.spamhaus.org",
    "b.barracudacentral.org",
    "bl.spamcop.net",
    "dnsbl.sorbs.net",
    "psbl.surriel.com",
    "ubl.unsubscore.com",
    "rbl.interserver.net",
    "truncate.gbudb.net",
]

def check_blacklist(ip):
    """Fungsi untuk mengecek apakah IP masuk dalam blacklist"""
    # Balikkan urutan IP (Misal: 192.168.1.1 -> 1.1.168.192)
    reversed_ip = ".".join(ip.split(".")[::-1])

    results = {}
    
    for blacklist in BLACKLIST_SERVERS:
        query = f"{reversed_ip}.{blacklist}"
        
        try:
            socket.gethostbyname(query)  # Jika berhasil, IP masuk blacklist
            results[blacklist] = "⚠️ BLACKLISTED"
        except socket.gaierror:
            results[blacklist] = "✅ CLEAN"
    
    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 check_blacklist.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]
    print(f"\n🔍 Checking Blacklist for IP: {ip_address}\n")

    results = check_blacklist(ip_address)

    print(f"{'Blacklist Server':<35} {'Status'}")
    print("=" * 50)
    
    for bl, status in results.items():
        print(f"{bl:<35} {status}")
