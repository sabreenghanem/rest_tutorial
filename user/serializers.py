from rest_framework import serializers
from user.models import User,UserGeneralInfo,CountryCodeLookup

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
      #  fields = ('id','first_name','surname','email','date_of_birth','phone','country_code_lookup','gender','password')

class CountryCodeLookupSerializer (serializers.ModelSerializer):
    class Meta:
        model = CountryCodeLookup
        fields = ('id','iso','name','nice_name','iso3','number_code','phone_code','flag','created','updated')

class UserGeneralInfoSerializer (serializers.ModelSerializer):
    class Meta :
        model = UserGeneralInfo
        fields = ('id','user_id','hight','weight','marital_status','registered_treatment','created','updated')