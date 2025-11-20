from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock_count')

    def clean_price(self):
        """ Field level validation for the price field"""
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('price cannot be negative')
        return price
    
    def clean_stock_count(self):
        """ Field level validation for the price field"""
        price = self.cleaned_data.get('stock_count')
        if price < 0:
            raise forms.ValidationError('Stock count cannot be negative')
        return price