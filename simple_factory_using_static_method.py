from abc import ABC, abstractmethod

# -------------------------------
# PRODUCT
# -------------------------------
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# -------------------------------
# CONCRETE PRODUCTS
# -------------------------------
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"[EMAIL] {message}")

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"[SMS] {message}")

class PushNotification(Notification):
    def send(self, message: str):
        print(f"[PUSH] {message}")

# -------------------------------
# SIMPLE FACTORY
# -------------------------------
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

# -------------------------------
# CLIENT CODE
# -------------------------------
if __name__ == "__main__":
    notification = NotificationFactory.create_notification("email")
    notification.send("Hello via email!")

    notification = NotificationFactory.create_notification("sms")
    notification.send("Hello via SMS!")

    notification = NotificationFactory.create_notification("push")
    notification.send("Hello via Push!")
