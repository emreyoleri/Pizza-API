from authentication.models import User
from .serializers import UserCreationSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class HelloAuthView(generics.GenericAPIView):

    def get(self, request):

        return Response(data={'message': 'Hello Auth'},  status=status.HTTP_200_OK)
    

class UserCreateView(generics.GenericAPIView):
    
    serializer_class = UserCreationSerializer

    def post(self,request):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
