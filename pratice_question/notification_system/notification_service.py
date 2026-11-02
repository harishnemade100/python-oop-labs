
from notification_channels import EmailChannel, SmsChannel, PushChannel
from schema import SentResult, User, Notification

class NotificationService:
    def __init__(self, channels):
        self._channels = channels

    def send(self, notification, channel_name):
        try:
            channel = self._channels[channel_name]
        except KeyError:
            return SentResult(False, channel_name, ("unknown channel",))
        return channel.send(notification)


if __name__ == "__main__":
    service = NotificationService({
        "email": EmailChannel(),
        "sms": SmsChannel(),
        "push": PushChannel(),
    })

    user = User(name="Asha", email="asha@example.com", phone_number="+919876543210")
    note = Notification(user, "Order shipped", "Your order #123 is on its way.")

    print(service.send(note, "email"))
    print(service.send(note, "sms"))
    print(service.send(note, "push"))      # fails: no device token
    print(service.send(note, "whatsapp"))  # fails: unknown channel