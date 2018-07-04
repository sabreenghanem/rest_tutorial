from django.shortcuts import render
from user.models import UserGeneralInfo,User,CountryCodeLookup
from user.serializers import UserGeneralInfoSerializer,UserSerializer,CountryCodeLookupSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status




class CountryCodeLookupsViewSet (viewsets.ModelViewSet):
    queryset = CountryCodeLookup.objects.all()
    serializer_class = CountryCodeLookupSerializer

    def list(self,request,format=None):
        countries = CountryCodeLookup.objects.all()
        serializer = CountryCodeLookupSerializer(countries,many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, format=None):
        users = User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404


    def retrieve(self, request, pk,format=None):
        user=self.get_object(pk)
        serializer=UserSerializer(user)
        return Response(serializer.data)

    def create(self, request, format=None):
         content = request.data

         user = User.objects.create(first_name = content.get("first_name"),
                                    surname = content.get("surname"),
                                    email= content.get("email"),
                                    date_of_birth = content.get("date_of_birth"),
                                    phone = content.get("phone"),
                                    country_code_lookup = content.get("country_code_lookup"),
                                    gender = content.get("gender"), password = content.get("password") )
         user.save()

         serializer = UserSerializer(data=content)
         if serializer.is_valid():
          return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk, format=None):


            content = request.data
            user = self.get_object(pk)

            if content.get("first_name")!=None:
                user.first_name=content.get("first_name")

            if content.get("surname")!=None:
                user.surname=content.get("surname")

            if content.get("email")!=None:
                user.email=content.get("email")
            if content.get("date_of_birth")!=None:
                user.date_of_birth=content.get("date_of_birth")
            if content.get("phone") != None:
                user.phone = content.get("phone")
            if content.get("country_code_lookup")!=None:
                user.country_code_lookup=content.get("country_code_lookup")
            if content.get("gender")!=None:
                user.gender=content.get("gender")
            if content.get("password")!=None:
                user.password=content.get("password")

            user.save()
            return Response(status=status.HTTP_200_OK)

    def destroy(self, request, pk,format=None):
        user=self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserGeneralInfoViewSet(viewsets.ModelViewSet):
    queryset = UserGeneralInfo.objects.all()
    serializer_class = UserGeneralInfoSerializer

    def list(self,request,user_pk):
        queryset = self.queryset.filter(user=user_pk)
        serializer = UserGeneralInfoSerializer(queryset,many=True)
        return Response(serializer.data)



    def retrieve(self,request,pk,user_pk):
        queryset = self.queryset.filter(pk=pk,user=user_pk)
        serializer = UserGeneralInfoSerializer(queryset,many=True)
        return Response(serializer.data)

    def get_object(self,pk,user_pk):
        try:
            return UserGeneralInfo.objects.get(pk=pk,user=user_pk)
        except UserGeneralInfo.DoesNotExist:
            raise Http404


    def update(self,request,pk,user_pk,format=None):

        user_info= self.get_object(pk,user_pk)
        content = request.data

        if content.get("user")!=None:
            user_info.user=content.get("user")

        if content.get("hight")!=None:
            user_info.hight=content.get("hight")

        if content.get("weight")!=None:
             user_info.weight=content.get("weight")
        if content.get("marital_status")!=None:
             user_info.marital_status=content.get("marital_status")
        if content.get("registered_treatment") != None:
             user_info.registered_treatment = content.get("registered_treatment")



        user_info.save()
        return Response(status=status.HTTP_200_OK)



