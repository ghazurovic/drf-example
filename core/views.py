from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.helpers.model_manager import get_unique_or_none
from core.helpers.exceptions import AuthenticationException
from .serializers import UserSerializer


class ApiLoginView(APIView):

    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def get(self, request):
        """Returns current logged-in user
        """
        if type(request.user) != AnonymousUser:
            user = get_unique_or_none(User, pk=request.user.id)
            serializer = UserSerializer(user)

            return Response(serializer.data)
        return Response({})

    def post(self, request):
        try:
            """Login a user
            """
            username = request.data.get('username')
            password = request.data.get('password')

            user = get_unique_or_none(User, username=username)
            if not user:
                raise AuthenticationException(f'User "{username}" not found.')

            user = authenticate(username=username, password=password)

            if user is None:
                raise AuthenticationException(
                    f'Login failed for user "{username}."'
                )

            login(request, user)
            user = get_unique_or_none(User, pk=request.user.id)
            serializer = UserSerializer(user)
            return Response(serializer.data)

        except Exception as e:
            return Response(
                data={'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class ApiLogoutView(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def post(self, request):
        try:
            logout(request)
            return Response(data={'message': 'Logged out.'})
        except Exception:
            return Response(data={'message': 'Logout failed.'})
