from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .models import MainUsers, SubUsers
from .serializer import MainUsersSerializer,SubUsersSerializer
# Create your views here.

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


class ListUsers(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        users = MainUsers.objects.all()
        serializer = MainUsersSerializer(users,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MainUsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message":"something went wrong"})

    def update(self, request, pk):
        user = MainUsers.objects.get(id=pk)
        serializer = MainUsersSerializer(instance=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message":"did not update"})

    def delete(self, request,pk):
        user = MainUsers.objects.get(id=pk)
        user.delete()
        return Response({"message":"user deleted successfully"})

class ListSubUsers(APIView):
    def get(self, request,pk):
        users = SubUsers.objects.filter(mainUser=pk)
        serializer = SubUsersSerializer(users,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubUsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message":"something went wrong"})

