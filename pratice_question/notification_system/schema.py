from dataclasses import dataclass
from typing import Optional



@dataclass(frozen=True)
class User:
    name: str
    email: Optional[str]=None
    phone_number: Optional[str]=None
    device_token: Optional[str]=None


@dataclass(frozen=True)
class Notification:
    user: User
    title: str
    body: str

@dataclass(frozen=True)
class SentResult:
    success: bool
    channel: str
    error: Optional[str] = None


user = User("Harish", "harishnemade@gmail.com")
notification = Notification(User, "Hello", "My Name is Harish")
result = SentResult("True", "email")

print(user)
print(notification)
print(result)
