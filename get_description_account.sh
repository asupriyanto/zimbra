#!/bin/bash

# Loop melalui daftar akun dalam file /tmp/list_account.txt
while IFS= read -r acct || [[ -n "$acct" ]]; do
    # Mendapatkan informasi akun dari zmprov
    a=$(zmprov -l ga "$acct" | grep "displayName:" | cut -d ' ' -f2-)
    b=$(zmprov -l ga "$acct" | grep "description:" | cut -d ' ' -f2-)
    c=$(zmprov -l ga "$acct" | grep "zimbraAccountStatus:" | cut -d ' ' -f2-)
    timestamp=$(zmprov -l ga "$acct" | grep "zimbraLastLogonTimestamp:" | cut -d ' ' -f2-)

    # Periksa apakah timestamp ditemukan
    if [[ -z "$timestamp" ]]; then
        time="Tidak Pernah Login"
    else
        # Mengonversi timestamp menjadi format yang lebih mudah dibaca
        time=$(date -d "${timestamp:0:4}-${timestamp:4:2}-${timestamp:6:2} ${timestamp:8:2}:${timestamp:10:2}:${timestamp:12:2}")
    fi

    # Mencetak informasi akun
    echo "$acct,$a,$b,$c,$time"
done < /tmp/list_account.txt