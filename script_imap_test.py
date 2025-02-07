import imaplib

def login_imap(username, password, imap_server, port):
    try:
        # Membuat koneksi ke server IMAP
        imap_connection = imaplib.IMAP4_SSL(imap_server, port)

        # Melakukan login
        imap_connection.login(username, password)
        
        print("Login berhasil!")
        
        # Menutup koneksi
        imap_connection.logout()
    except imaplib.IMAP4.error as e:
        print("Login gagal:", e)

# Mengatur informasi login
username = "username@domain.com"
password = "password"
imap_server = "smtp.server.com"
port = 993  # Port default untuk IMAP SSL

# Memanggil fungsi login_imap dengan informasi login
login_imap(username, password, imap_server, port)
