from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets,filters
from profiles_api import serializers,models,permissions
from rest_framework.authentication import TokenAuthentication


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return a list containing numbers"""

        apiview_list = ['one',
                        'two',
                        'three',
                        'four',
        ]

        return Response({'message':'hello!!','apiview_list':apiview_list})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            message = "hello "+ name+" age is "+age
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset =['eleven',
                    'twelve',
                    'thirteen',
                    'fourteen'
                    ]

        return Response({'message': 'hello view set', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            message = "hello "+name+" the age is "+age
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles Creating and Updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)



