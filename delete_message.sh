#!/bin/bash
# rm_message.sh - Menghapus email tertentu dari semua akun Zimbra berdasarkan pola pencarian

search_ptrn="from:recipient@domain.com date:mm/dd/yy" # Date format date:mm/dd/yy
#search_ptrn='subject:"SPAM Alert"'  # Ganti dengan subject email yang ingin dihapus
LOGFILE="/var/log/zimbra_delete.log"

# Simpan daftar akun dalam file sementara agar lebih cepat
if [ ! -f /tmp/zimbra_accounts ]; then
    zmprov -l gaa | grep -vE "admin|virus-quarantine|spam|ham|galsync|amavis|milter" | sort > /tmp/zimbra_accounts
fi

# Baca daftar akun dengan aman
while IFS= read -r acct; do
    echo "$(date): Searching in $acct for pattern: $search_ptrn" | tee -a $LOGFILE

    # Cari email berdasarkan search pattern
    for msg in $(/opt/zimbra/bin/zmmailbox -z -m "$acct" s -t message "$search_ptrn" | awk 'NR>1 && !/Id|---/ {print $2}')
    do
        echo "Removing message ID $msg from $acct" | tee -a $LOGFILE
        /opt/zimbra/bin/zmmailbox -z -m "$acct" dm "$msg"
        echo "$(date): Deleted message ID $msg from $acct" | tee -a $LOGFILE
    done
done < /tmp/zimbra_accounts
