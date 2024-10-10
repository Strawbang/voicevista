from domain.interfaces.user_repository_interface import UserRepositoryInterface
from django.apps import apps

class DjangoUserRepository(UserRepositoryInterface):

    def create_user(self, user_data: dict):
        UserModel = apps.get_model('infrastructure', 'UserModel')
        user = UserModel(**user_data)
        user.save()
        return user

    def exists_by_email(self, email: str) -> bool:
        UserModel = apps.get_model('infrastructure', 'UserModel')
        return UserModel.objects.filter(email=email).exists()
    
    def find_by_email(self, email: str):
        UserModel = apps.get_model('infrastructure', 'UserModel')
        try:
            return UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None