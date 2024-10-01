import hashlib
from injector import inject
from ..interfaces.user_service_interface import UserServiceInterface
from infrastructure.interfaces.user_repository_interface import UserRepositoryInterface
from ..entities.user import User
class UserService(UserServiceInterface):

    @inject
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def register_user(self, user_data: dict) -> User:
        user_data['password'] = self.hash_password(user_data['password'])  # Hash the password
        return self.user_repository.create_user(user_data)

    def user_exists(self, email: str) -> bool:
        return self.user_repository.exists_by_email(email)

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()