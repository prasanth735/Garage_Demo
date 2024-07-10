from django.shortcuts import render,redirect
from django.views  import View


from myapp.forms import BrandForm,CarForm
from myapp.models import Brand,Car

# Create your views here.


class BrandAddView(View):

    def get(self,request,*args,**kwargs):

        form=BrandForm()
         
        return render(request,"brand.html",{"form":form})
    
    def post(self,request,*args,**kwargs):

        form=BrandForm(request.POST)

        if form.is_valid():

            Brand.objects.create(**form.cleaned_data)

            return redirect("car")
        return render(request,"brand.html",{"form":form})
    

class CarAddView(View):

    def get(self,request,*args,**kwargs):

        form=CarForm()
         
        return render(request,"car.html",{"form":form})
    
    def post(self,request,*args,**kwargs):

        form=CarForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect("list")
        return render(request,"car.html",{"form":form})



class CarListView(View):

    def get(self,request,*args,**kwargs):

        data=Car.objects.all()

        brand=Brand.objects.all()

        return render (request,"list.html",{"data":data,"brand":brand})
    
    def post(self,request,*args,**kwargs):

        brand_obj=request.POST.get("brand")
        data=Car.objects.filter(brand_object__name=brand_obj)
        brand=Brand.objects.all()

        print(brand_obj)
        return render (request,"list.html",{"data":data,"brand":brand})

    

class carDetailView(View):


    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        data=Car.objects.get(id=id)

        return render (request,"detail.html",{"data":data})
    

class CarUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        car_obj=Car.objects.get(id=id)

        form=CarForm(instance=car_obj)
        

        return render(request,"update.html",{"form":form})

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        car_obj=Car.objects.get(id=id)

        form=CarForm(request.POST,request.FILES,instance=car_obj)

        if form.is_valid():

            form.save()
            return redirect("list")

        return render(request,"update.html",{"form":form})
        






        

        

    