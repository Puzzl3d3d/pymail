import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls

# Create a secure SSL context
context = ssl.create_default_context()

def SendEmail(sender, password, reciever, message):
    try:
        # Try to log in to server and send email
        server = smtplib.SMTP(smtp_server,port)
        server.starttls(context=context) # Secure the connection
        server.login(sender, password)
        server.sendmail(sender, reciever, message)
    except Exception as e:
        print(e, "Try enabling Less Secure Apps in your Google account settings.")
    finally:
        server.quit()