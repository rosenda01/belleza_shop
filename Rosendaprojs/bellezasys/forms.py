from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


		
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email', 'password1', 'password2']

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = ['name','phone','address','product']

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = '__all__'

class UpdateFormOrder(ModelForm):
	class Meta:
		model = Order
		fields= ['status']