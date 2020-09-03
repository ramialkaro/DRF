from django.shortcuts import render
from django.http import JsonResponse

# third-party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers  import PostSerializers
from .models import Post

class TestView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        post = qs.first()
        # serializer = PostSerializer(qs, many=True)
        serializer = PostSerializers(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
