import random
import smtplib
from email.message import EmailMessage
import mysql.connector

mydb = mysql.connector.connect(user='root', passwd='9415', host='localhost',auth_plugin='mysql_native_password', database="preteur")

mycursor = mydb.cursor(buffered=True)


randomNumber = random.randint(100000,999999)
sender_email = "trigun.pandey2021@vitstudent.ac.in"
sender_password = "fun2trigun"

receiver_email ="pandeytrigun02@gmail.com"

msg = EmailMessage()
msg.set_content('''
\n
Hey User,
Your OTP is {}
\n
'''.format(randomNumber))

msg['Subject'] = 'One Time Password'
msg['From'] = "trigun.pandey2021@vitstudent.ac.in"
msg['To'] = "pandeytrigun02@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("trigun.pandey2021@vitstudent.ac.in", "fun2trigun")
server.send_message(msg)
server.quit()
print('otp sent to mail')


x = int(input("enter the otp:"))
if x == randomNumber:
    print("Success")
else:
    print("Failure")

acc_no=int(input("Enter account number:"))
try:
    cmd = "select Email from preteur_1  WHERE ACC_NO=%s"
    mycursor.execute(cmd,acc_no)
    mydb.commit()
    F = "%10s %12s %15s %22s %25s %14s %11s %15s"
    print(F % ("PAN_CARD","ACC_NO", "NAME", "MOBILE", "EMAIL","ADDRESSS", "PINCODE", "OCCUPATION", "ANNUAL_INC"))
    print("="*155)
    for i in mycursor:
        G = "%13s %15s %15s %30s %20s %10s %10s %15s"
        print(G % i)
    print("="*155)
except:
    print("Table doesn't exist")