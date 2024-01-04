from rest_framework import serializers,validators
from .models import *
from rest_framework.validators import ValidationError
from django.conf import settings 
from rest_framework.response import Response
from rest_framework import status
import requests
from .serializers import *

class Category_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Category
		fields='__all__'

class Product_Serializer(serializers.ModelSerializer):
	Category = Category_Serializer(read_only=True)
	class Meta:
		model=Product
		fields='__all__'

class Cart_detail_Serializer(serializers.ModelSerializer):
	Product = Product_Serializer(read_only=True)
	class Meta:
		model=Cart_detail
		fields='__all__'

class Cart_Serializer(serializers.ModelSerializer):
	Cart_detail_Cart=Cart_detail_Serializer(read_only=True,many=True)
	class Meta:
		model=Cart
		fields='__all__'

class Oder_detail_Serializer(serializers.ModelSerializer):
	Product = Product_Serializer(read_only=True)
	class Meta:
		model=Oder_detail
		fields='__all__'

class Oder_Serializer(serializers.ModelSerializer):
	Oder_detail_Oder = Oder_detail_Serializer(read_only=True,many=True)
	class Meta:
		model=Oder
		fields='__all__'
					
class User_Serializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=False)
	Cart_User = Cart_Serializer(read_only=True)
	Oder_User = Oder_Serializer(read_only=True,many=True)
	# Avatar = serializers.CharField(required=False)
	class Meta:
		model=User
		fields='__all__'					

class Trademark_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Trademark
		fields='__all__'

class Made_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Made
		fields='__all__'


class Stock_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Stock
		fields='__all__'

class Goods_received_note_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Goods_received_note
		fields='__all__'
					
class Cart_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Cart
		fields='__all__'

class Cart_detail_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Cart_detail
		fields='__all__'

class Oder_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Goods_received_note
		fields='__all__'
					
class Oder_detail_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Cart
		fields='__all__'