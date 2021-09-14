from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework import status

from users.models import CustomUser
from users.serializer import UserSerializer, LoginSerializer


class UserAction:
    @staticmethod
    def register(request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return serializer.errors, status.HTTP_400_BAD_REQUEST
        else:
            user = serializer.create(serializer.data)
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'username': user.username,
                'email': user.email,
                'token': token.key,
            }
            return data, status.HTTP_201_CREATED

    @staticmethod
    def login(request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return serializer.errors, status.HTTP_400_BAD_REQUEST
        else:
            try:
                user = CustomUser.objects.get(username=serializer.data['username'])
                if not check_password(serializer.data['password'], user.password):
                    return 'Incorrect username or password.', status.HTTP_400_BAD_REQUEST
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return {'username': user.username, 'email': user.email, 'token': token.key}, status.HTTP_200_OK
            except CustomUser.DoesNotExist:
                return 'Incorrect username or password.', status.HTTP_400_BAD_REQUEST

        # data = request.data
        # error = {}
        # if 'username' not in data:
        #     error['username'] = ['The username field is required.']
        # if 'password' not in data:
        #     error['password'] = ['The password field is required.']
        # if len(error) == 0:
        #     try:
        #         user = CustomUser.objects.get(username=data['username'])
        #         if not check_password(data['password'], user.password):
        #             return 'username or password is incorrect.', status.HTTP_400_BAD_REQUEST
        #         login(request, user)
        #         token, created = Token.objects.get_or_create(user=user)
        #         return {'username': user.username, 'email': user.email, 'token': token.key}, status.HTTP_200_OK
        #     except CustomUser.DoesNotExist:
        #         return 'username or password is incorrect.', status.HTTP_400_BAD_REQUEST

    @staticmethod
    def logout(request):
        print(request.user.auth_token.delete())
        logout(request)
        return {'message': 'Successfully logged out.'}, status.HTTP_200_OK
