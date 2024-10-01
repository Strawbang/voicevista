from injector import inject
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from domain.interfaces.user_service_interface import UserServiceInterface
import json
@method_decorator(csrf_exempt, name='dispatch')
class RegisterUserView(View):

    @inject
    def __init__(self, user_service: UserServiceInterface):
        self.user_service = user_service
        super().__init__()

    def post(self, request) -> JsonResponse:
        user_data = json.loads(request.body)
        if self.user_service.user_exists(user_data['email']):
            return JsonResponse({'error': 'User already exists'}, status=400)
        user = self.user_service.register_user(user_data)
        return JsonResponse({'id': user.id, 'email': user.email}, status=201)
        