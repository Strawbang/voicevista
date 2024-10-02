from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def create_user(self, user_data: dict):
        pass
    
    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def find_by_email(self, email: str):
        pass