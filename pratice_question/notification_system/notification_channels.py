from abc import ABC, abstractmethod
from schema import SentResult, User, Notification

class NofiticationChannel(ABC):

    name = "base"

    def send(self, notification):
        errors = self._validation(notification)
        if errors:
            return SentResult(False, self.name, tuple(errors))
        payload = self._fromatting(notification)
        self._delivery(payload)
        return SentResult(True, self.name)

    
    @abstractmethod
    def _validation(self, notification):
        pass

    @abstractmethod
    def _fromatting(self, notification):
        pass

    def _delivery(self, payload):     # children get this for free
        print("SENT:", payload)



class EmailChannel(NofiticationChannel):

    name = "email"

    def _validation(self, n):
        errors = []

        if not n.user.email or "@" not in n.user.email:
            errors.append("Invalid Email")
        if not n.title.strip():
            errors.append("subject is empty")
        if not n.body.strip():
            errors.append("body is empty")
        return errors

    def _fromatting(self, n):
        return {
            "To": n.user.email,
            "Subject": n.title,
            "Body": f"Hi {n.user.name}, {n.body}"
        }
    



class SmsChannel(NofiticationChannel):

    name = "sms"

    def _validation(self, n):
        errors = []

        if not n.user.phone_number:
            errors.append("no phone number")
        if len(n.title + n.body) > 160:
            errors.append("message too long")
        return errors

    def _fromatting(self, n):
        return {"to": n.user.phone_number, "text": f"{n.title}: {n.body}"}


class PushChannel(NofiticationChannel):

    name = "push"

    def _validation(self, n):
        errors = []
        if not n.user.device_token:
            errors.append("no device token")
        return errors

    def _fromatting(self, n):
        return {"token": n.user.device_token, "title": n.title, "body": n.body}


user = User("Harish", email = "harishnemade100@gmail.com",phone_number="+919876543210")
note = Notification(user, "How Are You ?", "Just Asking")