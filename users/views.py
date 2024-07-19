# users/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import getUsersList, getUserDetail, createUser, updateUser, deleteUser

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/users/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of users'
        },
        {
            'Endpoint': '/users/<id>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single user object'
        },
        {
            'Endpoint': '/users/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new user with data sent in post request'
        },
        {
            'Endpoint': '/users/<id>/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing user with data sent in post request'
        },
        {
            'Endpoint': '/users/<id>/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing user'
        },
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        return getUsersList(request)
    elif request.method == 'POST':
        return createUser(request)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    if request.method == 'GET':
        return getUserDetail(request, pk)
    elif request.method == 'PUT':
        return updateUser(request, pk)
    elif request.method == 'DELETE':
        return deleteUser(request, pk)