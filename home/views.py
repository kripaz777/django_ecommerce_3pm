from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()


class HomeView(BaseView):
    def get(self,request):
        self.views
        self.views['subcategories'] = SubCategory.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['reviews'] = Review.objects.all()
        self.views['new_products'] = Product.objects.filter(labels = 'new')
        self.views['hot_products'] = Product.objects.filter(labels='hot')
        self.views['sale_products'] = Product.objects.filter(labels='sale')
        return render(request,'index.html',self.views)