# rest_framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken

# local
from .models import User
from .serializers import UserSerializer


class UserTokenViewSet(viewsets.ModelViewSet):
    queryset = User.objects.none()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [
                AllowAny,
            ]
        return super().get_permissions()

    def list(self, request):
        '''To return requesting user's accesstoken'''
        token = User.objects.get(username=request.user.username).fb_token
        return Response({"token": token})

    def create(self, request, *args, **kwargs):
        '''To save fb token in db and to get back access token in return'''
        data = request.data
        user = User.objects.filter(username=data['username'])
        if user:
            user.update(fb_token=data['fb_token'])
            user = user.first()

        else:

            user = User.objects.create(username=data['username'],
                                       fb_token=data['fb_token'],
                                       password='Pwd@12345')
        token = AccessToken.for_user(user)
        print(type(token), token)
        return Response({'token': str(token)})
