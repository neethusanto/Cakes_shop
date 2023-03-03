from django import forms
from.models import Cake

class CakeForm(forms.ModelForm):
    class Meta:
        model=Cake
        fields=['cake_name','cake_flavour','cake_desc','cake_price','cake_img']