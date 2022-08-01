from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from talk.models import Profile
from talk.serializers import ProfileSerializer

# Create your views here.

class Dashboard(APIView):

    def get(self, reqeust, format=None):
        name = self.request.user
        return Response({'message':f'hello, {name}'})


class profile_list(APIView):
    def get(self, request, format=None):
        profiles = Profile.objects.exclude(user=request.user)
        serializer = ProfileSerializer(profiles,many=True)
        return Response(serializer.data)

class Profile(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.pk(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Respnse(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', ])
# def greet(request):
#     """
#     Greets the user with a message.
#     The `name` is passed as a query parameter.
#     """
#     if request.method != 'GET':
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#     name = request.query_params.get('name', 'World')
#     return Response({'message': f'Hello, {name}!'})
