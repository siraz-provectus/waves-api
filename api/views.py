from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.core.serializers import serialize

from api.models import User
from api.serializers import UserSerializer
# Also add these imports
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from django.http import JsonResponse

import pywaves as pw

import logging
logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

def create_wallet(request):
  params = request.POST

  if request.method == "GET" or len(params) == 0:
    return JsonResponse({'message': 'Bad request'}, status=400 )

  pw.setNode(node = 'https://pool.testnet.wavesnodes.com', chain = 'testnet')
  newAddress = pw.Address(seed = params['seed'])

  iheartToken = 0

  for asset in newAddress.assets():
    iheartToken = newAddress.balance(asset)



  data = {'address': newAddress.address, 'privateKey': newAddress.privateKey ,'waves': newAddress.balance(), 'iheartToken': iheartToken}

  return JsonResponse(data)