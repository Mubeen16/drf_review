from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(['GET'])
def hello(request):
    return Response({"message": "hello DRF"})

@api_view(['POST'])
def hellow_name(request):
    name = request.data.get('a')
    return Response("hello " + name)
@api_view(['POST'])
def add(request):
    a = int(request.data.get('a'))
    b = int(request.data.get('b'))
    return Response(a + b)

class greetings_api(APIView):
    def post(self, request):
        name = request.data.get("a")
        return Response({"greetings": "hellow " + name})
    







