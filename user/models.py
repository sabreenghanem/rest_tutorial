from django.db import models
from enum import Enum

class CountryCodeLookup (models.Model):
    iso = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    nice_name=models.CharField(max_length=45)
    iso3 = models.CharField(max_length=45)
    number_code = models.IntegerField()
    phone_code = models.IntegerField()
    flag = models.CharField(max_length=45)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()
    class Meta:
        ordering = ['name']
        db_table = 'country_code_lookup'



class User (models.Model):
    class GenderChoice(Enum):
        male= ('m','male')
        female = ('f','female')

    @classmethod
    def get_value(cls, member):
        return (cls[member].value[0])

    first_name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    date_of_birth = models.DateTimeField()
    phone = models.CharField(max_length=45)
    country_code_lookup = models.ForeignKey(CountryCodeLookup,on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=45,
        choices=[(x,x.value) for x in GenderChoice]
    )
    password = models.CharField(max_length=45)
    class Meta:
        ordering = ['first_name']
        db_table = 'user'

class UserGeneralInfo(models.Model):
    class MaritalStatusChoice(Enum):
         M = ('Married')
         S = ('Single')
         D = ('Divorced')
         W = ('Widowed')
    @classmethod
    def get_value (cls,member):
        return (cls[member].value[0])

    user= models.ForeignKey(User,on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    marital_status = models.CharField(
         max_length=45,
        choices=[(x,x.value) for x in MaritalStatusChoice ]
    )
    registered_treatment = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        ordering = ['user_id']
        db_table = 'user_general_info'
