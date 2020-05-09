from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """:return a list containing numbers"""

        apiview_list = ['one',
                        'two',
                        'three',
                        'four',
        ]

        return Response({'message':'hello!!','apiview_list':apiview_list})
