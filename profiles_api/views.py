
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from profiles_api import serializers
# Create your views here.



class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hellow message with name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST)



    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class =serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset=[
            'Uses actions(list, create, retrive, update, partial_update)',
            'Automaticly maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello!','a_viewset': a_viewset})

    def create(self, request):
        """Create a new message"""
        seriakizer = self.serializer_class(data= request.data)

        if seriakizer.is_valid():
            name = seriakizer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})

        else:
            return Response(
                seriakizer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk= None):
        """Handle getting an object by ID"""
        return Response({'http_method': 'GET'})


    def update(self, request, pk = None):
        """Handle updating object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})
