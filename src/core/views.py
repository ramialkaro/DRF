from django.shortcuts import render
from django.http import JsonResponse

# third-party imports
from rest_framework.response import Response
from rest_framework.views import APIView

class testView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name':'Rami',
            'age':27
        }
        return Response(data)

def test_view(request):
    data = {
        'name':'Rami',
        'age':27
    }
    return JsonResponse(data)