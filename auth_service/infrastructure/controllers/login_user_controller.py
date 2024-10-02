from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from injector import inject
from domain.interfaces.user_service_interface import UserServiceInterface
from application.commands.login_user_commands import LoginUserCommand

class LoginUserController(APIView):

    @inject
    def __init__(self, user_service: UserServiceInterface):
        self.user_service = user_service
        super().__init__()

    def post(self, request):
        user_data = request.data
        command = LoginUserCommand(**user_data)

        try:
            token = self.user_service.login_user(command)
            return Response({'token': token}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)