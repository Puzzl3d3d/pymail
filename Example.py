from SendEmail import SendEmail

c = open("credentials.json", "r")
sender, password = [l.strip() for l in c.readlines()]

SendEmail(sender, password, input("Reciever: "), input("Message: "))