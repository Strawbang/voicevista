from abc import ABC, abstractmethod
from ..entities.user import User

class UserServiceInterface(ABC):

    @abstractmethod
    def register_user(self, user_data: dict) -> User:
        """Registers a new user."""
        pass

    @abstractmethod
    def user_exists(self, email: str) -> bool:
        """Checks if a user exists by email."""
        pass
