from django import forms
from .models import *

class EditorProduct(forms.Form):
    product_name = forms.CharField(max_length=100)
    product_description = forms.CharField(widget=forms.Textarea())
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = forms.IntegerField()

class AddProduct(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'price', 'product_quantity']

class DelProduct(forms.Form):
    product_id = forms.IntegerField()

class ProductWithImgForm(forms.Form):
    product_name = forms.CharField(max_length=100)
    product_description = forms.CharField(widget=forms.Textarea())
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = forms.IntegerField()
    product_img = forms.ImageField()

class FormMetaProductImg(forms.ModelForm):

    class Meta:
        model = MetaProductImg
        fields = '__all__'