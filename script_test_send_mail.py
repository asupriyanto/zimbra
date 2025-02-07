import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Pengaturan SMTP
smtp_server = 'smtp.server.com'
smtp_port = 587  # Ganti port SMTP sesuai dengan konfigurasi penyedia email Anda
smtp_username = 'sender@domain.com'
smtp_password = 'password'

# Pengaturan email
sender_email = 'sender@domain.com'
subject = 'Kirim Pakai Script Python'
message = 'Uji kirim email via script'

# Alamat email penerima
receiver_email = 'recipient@domain.com'

# Jumlah email yang akan dikirim
num_emails = 20

# Inisialisasi koneksi SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Mengaktifkan enkripsi TLS untuk keamanan

try:
    # Login ke server SMTP
    server.login(smtp_username, smtp_password)

    for _ in range(num_emails):
        # Membuat objek pesan email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Menambahkan konten email
        msg.attach(MIMEText(message, 'plain'))

        # Mengirim email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f'Email sent to {receiver_email}')

    print('All emails sent successfully!')

except Exception as e:
    print(f'Error: {e}')

finally:
    # Menutup koneksi SMTP
    server.quit()