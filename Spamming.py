from SendEmail import SendEmail

c = open("credentials.json", "r")
sender, password = [l.strip() for l in c.readlines()]

import time, random

receiver_email = input("Enter email: ")

chars = "qwertyuiopasdghjklzxcvbnmmQIOPAKLZXNM1234556778990,.,./'[]89`-HDCAWhjpfajwodj9u"

def GetRandomAmount(x):
    str = ""
    for i in range(x):
        str += chars[random.randint(0,len(chars)-1)]
    return str

def spam():
    while True:
        SendEmail(sender, password, receiver_email, GetRandomAmount(50))
        time.sleep(0.25)


spam()
