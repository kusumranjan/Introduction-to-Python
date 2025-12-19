class Notification:
    def send(self,msg):
        print("Sending Notification",msg)

class EmailNotification(Notification):
    def send(self,msg):
        print("Sending Email Notification",msg)

class SMSNotification(Notification):
    def send(self,msg):
        print("Sending SMS Notification",msg)


class PushNotification(Notification):
    def send(self,msg):
        print("Sending Push Notification",msg)


n1=EmailNotification()
n1.send("Your order is confirmed")
n2=SMSNotification()
n2.send("Your OTP is 3434")
n3=PushNotification()
n3.send("You have a notification")
