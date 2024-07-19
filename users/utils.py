from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer


def getUsersList(request):
    users = CustomUser.objects.all().order_by('-created_at')
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)


def getUserDetail(request, pk):
    user = CustomUser.objects.get(id=pk)
    serializer = CustomUserSerializer(user, many=False)
    return Response(serializer.data)


def createUser(request):
    data = request.data
    user, created = CustomUser.objects.get_or_create(
        email=data['email'],
        defaults={'first_name': data.get('first_name', ''), 'last_name': data.get('last_name', '')}
    )
    if not created:
        return Response({'message': 'User already exists'}, status=400)
    serializer = CustomUserSerializer(user, many=False)
    return Response(serializer.data, status=201)


def updateUser(request, pk):
    data = request.data
    user = CustomUser.objects.get(id=pk)
    serializer = CustomUserSerializer(instance=user, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


def deleteUser(request, pk):
    user = CustomUser.objects.get(id=pk)
    user.delete()
    return Response('User was deleted!', status=204)