from rest_framework.permissions import AllowAny

from rest_framework import viewsets, mixins

from authentication.serializers import (LoginSerializer, RegistrationSerializer,)


class LoginViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Login endpoint
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """
        This will create a currency.
        """
        return self.create(request, *args, **kwargs)


class RegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Registration endpoint
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        """
        This will registrate a user.
        """
        return self.create(request, *args, **kwargs)

