import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Add message body
    message.attach(MIMEText(body, 'plain'))

    # Connect to the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to your gmail account
    server.login(sender_email, sender_password)

    # Send Email
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Quit the server
    server.quit()


sender_email = "avinashaws9588@gmail.com"
sender_password = "mcst rhrz krcr baoe"
receiver_email = "rishavi08072002@gmail.com"
subject = "API WORKING FINE"
body = "It is to inform you that the we are correctly abled to fetch the correct price of the DESIRED INSTRUEMENT and network other componenets are working fine"


while True:
    send_email(sender_email, sender_password, receiver_email, subject, body)








