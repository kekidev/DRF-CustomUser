from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from django.http import Http404
from rest_framework.views import APIView


class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
                
        return Response(serializer.data)

class GetUserById(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk) 
        serializer  = UserSerializer(user)
        return Response(serializer.data)