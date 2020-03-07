import datetime
import math
import smtplib

def is_prime(n):
    if n==1: return False
    for k in range(2, int(math.sqrt(n)+1)):
        if n%k==0:
            return False
    
    return True


##SMTPサーバに接続する
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
type(smtp_obj)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login('dradra9512@gmail.com', 'hzrp futj znsh miyi')


while True:
    dt=datetime.datetime.now()
    dtint=int(dt.strftime("%Y%m%d%H%M%S"))
    print("1")


    ##素数判定
    if is_prime(dtint)==True:
        smtp_obj.sendmail('dradra9512@gmail.com', 'dradra9512@gmail.com', 'Subject: PrimeNumber\nPrime Number!\n%d' %dtint)
        smtp_obj.quit()
        break
