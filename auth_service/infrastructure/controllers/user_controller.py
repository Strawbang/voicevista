from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from injector import inject
from domain.interfaces.user_service_interface import UserServiceInterface
from application.commands.register_user_commands import RegisterUserCommand

class RegisterUserController(APIView):

    @inject
    def __init__(self, user_service: UserServiceInterface):
        self.user_service = user_service
        super().__init__()

    def post(self, request):
        user_data = request.data
        command = RegisterUserCommand(**user_data)  # Create command object from user_data
        
        try:
            user = self.user_service.register_user(command)  # Call the register_user method
            return Response({
                'id': user.id,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:  # Catch all other exceptions
            return Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        