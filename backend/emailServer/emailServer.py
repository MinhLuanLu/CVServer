import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("sender_email")
password = os.getenv('Password')
recipient_email = os.getenv("recipient_email")

# Establish a secure SSL connection to the Gmail SMTP server
def sendEmail(subject, body):

    message = f'Subject: {subject} \n\n{body}'
    message = str(message)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    
        server.login(sender_email, password)
        #print("Login successful!")

                # Send the email
        server.sendmail(
                    sender_email,
                    recipient_email,
                    message
        )
        success = "Email sent successfully!"

        return success
    

