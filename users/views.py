from django.views.generic.base import View
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_all(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)