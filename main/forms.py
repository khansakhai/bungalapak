from django.forms import ModelForm
from main.models import Product

class ItemForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]