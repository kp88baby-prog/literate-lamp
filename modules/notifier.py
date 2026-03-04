import smtplib
import logging
from email.message import EmailMessage

class EmailNotifier:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        logging.basicConfig(filename='email_notifier.log', level=logging.ERROR)

    def send_email(self, subject, body, to_email):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = to_email
        msg.set_content(body)

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to TLS
                server.login(self.username, self.password)
                server.send_message(msg)
            print(f'Email sent to {to_email}')
        except Exception as e:
            logging.error(f'Failed to send email to {to_email}: {e}')
            print(f'An error occurred: {e}')