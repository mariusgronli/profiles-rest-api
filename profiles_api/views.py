from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """
    Test API view
    """
    def get(self,request,format=None):
        an_apiview = [
            'Uses HTTP methods as functions (get,patch,put,delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]
        return Response({'Message': 'Hello','an_apiview': an_apiview})
