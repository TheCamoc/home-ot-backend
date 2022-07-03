from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins, generics, renderers
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from backend.serializers import UserSerializer, GroupSerializer, DeviceSerializer, SwitchSerializer, RoomSerializer
from backend.models import Device, Switch, Room


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view and modify Devices
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view and modify Devices
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class SwitchViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view and modify Devices
    """
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer
    permission_classes = [permissions.IsAuthenticated]

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def get(self, request, *args, **kwargs):
    #     device = self.get_object()
    #     return Response(device)