#Mohamed SAIFI

from abc import ABC, abstractclassmethod

# =====================================
#1. PRODUCT
class Notification(ABC):
    @abstractclassmethod
    def send(self, message: str):
        pass


# =====================================
#2. CONCRETE PRODUCTS
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"[EMAIL] {message}")


class SMSNotification(Notification):
    def send(self, message: str):
        print(f"[SMS] {message}")

class PushNotification(Notification):
    def send(self, message: str):
        print(f"[PUSH] {message}")


#======================================
#3. CREATOR (FACTORY)

class NotificationFactory(ABC):
    @abstractclassmethod
    def create_notification(self) -> Notification:
        pass

    def send_message(self, msg:str):
        Notification = self.create_notification()
        Notification.send(msg)


#=========================================
#4. CONCRETE FACTORIES

class EmailFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()


class SMSFactory(NotificationFactory):
    def create_notification(self) -> Notification:   #This function returns this type (Notification)
        return SMSNotification()


class PushFactory(NotificationFactory):
    def createNotification(self) -> Notification:
        return PushNotification()
    


#5. CLIENT CODE

def client_code(factory: NotificationFactory):
    factory.send_message("Hello, this is a notification")


if __name__== "__main__":
    print("sending Email: ")
    client_code(EmailFactory())

    print("Sending SMS: ")
    client_code(SMSFactory())

    print("Sending Push Notification: ")
    client_code(PushFactory())



    

