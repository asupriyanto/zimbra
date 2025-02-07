import smtplib

# Detail server SMTP dan kredensial
smtp_server = "smtp.server.com"
smtp_port = 587
sender_email = "username@domain.com"
sender_password = "password"

def test_smtp_connection(smtp_server, smtp_port, sender_email, sender_password):
    try:
        # Membuat koneksi ke server SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()  # Menyapa server

        # Memulai sesi TLS untuk keamanan
        server.starttls()
        server.ehlo()  # Menyapa server lagi setelah memulai TLS

        # Melakukan login ke server SMTP
        server.login(sender_email, sender_password)
        print("Koneksi ke server SMTP berhasil dan autentikasi berhasil.")
        
        # Menutup koneksi ke server SMTP
        server.quit()
    except Exception as e:
        print(f"Gagal terhubung ke server SMTP: {e}")

# Memanggil fungsi untuk menguji koneksi
test_smtp_connection(smtp_server, smtp_port, sender_email, sender_password)
