from django.db import models

# Create your models here.



class Brand(models.Model):

    name=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.name


class Car(models.Model):

    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="car_images",default="car.jpg")
    brand_object=models.ForeignKey(Brand,on_delete=models.CASCADE)
    price=models.CharField(max_length=200)
    options=(
        ("diesel","diesel"),
        ("petrol","petrol")
    )

    fuel=models.CharField(max_length=200,choices=options,default="diesel")



