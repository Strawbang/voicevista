from abc import ABC, abstractmethod

from application.commands.register_user_commands import RegisterUserCommand
from application.commands.login_user_commands import LoginUserCommand
from ..entities.user import User

class UserServiceInterface(ABC):

    @abstractmethod
    def register_user(self, command: RegisterUserCommand) -> User:
        """Registers a new user."""
        pass

    @abstractmethod
    def user_exists(self, email: str) -> bool:
        """Checks if a user exists by email."""
        pass
    
    @abstractmethod
    def login_user(self, command: LoginUserCommand):
        pass
