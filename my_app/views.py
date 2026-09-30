from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from my_app.serializer import AdminRegisterSerializer
from my_app.models import About,Education
from my_app.serializer import AboutSerializer,EducationSerializer

# Create your views here.

class AdminRegisterView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instants = AdminRegisterSerializer(data=form_data)

        if serializer_instants.is_valid():

            cleened_data = serializer_instants.validated_data

            User.objects.create_superuser(**cleened_data)

            return Response(data=serializer_instants.data)

class AboutListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,reqsuest):

        qs = About.objects.all()

        serializer_instans = AboutSerializer(qs,many= True)

        return Response(data=serializer_instans.data)

    def post(self,request):

        form_data = request.data

        serializer_instans = AboutSerializer(data=form_data)

        if serializer_instans.is_valid():

            cleeaned_data = serializer_instans.validated_data

            About.objects.create(**cleeaned_data)

            return Response(data=serializer_instans.data)

        else:
            return Response(data=serializer_instans.errors)

class AboutRetrieveUpdateDelete(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,request,pk=None):

        qs = About.objects.get(id=pk)

        seializer_instat = AboutSerializer(qs)

        return Response(data=seializer_instat.data)

    def put(self,request,pk=None):

        form_data = request.data

        serializer_instant = AboutSerializer(data=form_data)

        if serializer_instant.is_valid():

            cleeaned_data = serializer_instant.validated_data

            About.objects.filter(id=pk).update(**cleeaned_data)

            return Response(data=serializer_instant.data)

        else:
            return Response(data=serializer_instant.errors)

    def delete(self,request,pk=None):

        qs = About.objects.get(id=pk)

        seializer_instat = AboutSerializer(qs)

        qs.delete()

        return Response(data=seializer_instat.data)

class EducationListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,reuqest):

        qs = Education.objects.all()

        serializer_instants = EducationSerializer(qs,many=True)

        return Response(data=serializer_instants.data)


