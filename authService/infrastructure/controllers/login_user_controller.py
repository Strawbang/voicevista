from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from injector import Injector
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from domain.interfaces.user_service_interface import UserServiceInterface
from application.commands.login_user_commands import LoginUserCommand

class LoginUserController(APIView):

    # @inject
    # def __init__(self, user_service: UserServiceInterface):
    #     self.user_service = user_service
    #     super().__init__()

    @swagger_auto_schema(
        operation_description="Log in a user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={200: openapi.Response('User logged in successfully')}
    )
    def post(self, request):
        injector = Injector()
        user_service = injector.get(UserServiceInterface)
        user_data = request.data
        command = LoginUserCommand(**user_data)

        try:
            token = user_service.login_user(command)
            return Response({'token': token}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)