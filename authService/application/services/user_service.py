import hashlib
from authService import settings
from injector import inject
import jwt 
from datetime import datetime, timedelta
from domain.interfaces.user_service_interface import UserServiceInterface
from domain.interfaces.user_repository_interface import UserRepositoryInterface
from domain.entities.user import User
from application.commands.register_user_commands import RegisterUserCommand
from application.commands.login_user_commands import LoginUserCommand
class UserService(UserServiceInterface):

    @inject
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository
        super().__init__()

    def register_user(self, command: RegisterUserCommand) -> User:
        if self.user_exists(command.email):
            raise ValueError("User already exists")
        
        # Perform password hashing and user registration
        hashed_password = self.hash_password(command.password)
        user_data = {
            'email': command.email,
            'username': command.username,
            'password': hashed_password
        }
        return self.user_repository.create_user(user_data)

    def user_exists(self, email: str) -> bool:
        return self.user_repository.exists_by_email(email)

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
    
    def login_user(self, command: LoginUserCommand):
        user = self.user_repository.find_by_email(command.email)
        if user is None or not self.verify_password(command.password, user.password):
            raise ValueError("Invalid credentials")

        token = self.create_jwt_token(user)
        return token

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return hashed_password == hashlib.sha256(plain_password.encode()).hexdigest()

    def create_jwt_token(self, user) -> str:
        payload = {
            'id': user.id,
            'email': user.email,
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')