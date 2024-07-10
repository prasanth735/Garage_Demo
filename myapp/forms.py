from django import forms 

from myapp.models import Car

class BrandForm(forms.Form):

    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))




class CarForm(forms.ModelForm):

    class Meta:
        model=Car
        fields=["name","image","price","fuel","brand_object"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control form-select"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "fuel":forms.Select(attrs={"class":"form-control form-select"}),
            "brand_object":forms.Select(attrs={"class":"form-control form-select"})
        }