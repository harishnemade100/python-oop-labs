from abc import ABC, abstractmethod
from pratice_question.notification_system.schema import SentResult

class NofiticationChannel(ABC):

    name = "base"

    @abstractmethod
    def send(self, notification):
        error = self._validation(notification)
        if len(error) == 0:
            return SentResult("False", self.name, error)
        payload = self._fromatting(notification)
        self._delivery(payload)
        return SentResult(True, self.name)

    
    @abstractmethod
    def _validation(self, notification):
        pass

    @abstractmethod
    def _fromatting(self, notification):
        pass

    @abstractmethod
    def _delivery(self, notification):
        pass
