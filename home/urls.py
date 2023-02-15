from .views import   *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('brand/<slug>', BrandView.as_view(), name='brand'),
    path('search', SearchView.as_view(), name='search'),
    path('product_detail/<slug>', ProductDetailView.as_view(), name='product_detail'),
    path('signup', signup, name='signup'),
    path('product_review/<slug>', product_review, name='product_review'),
    path('cart', CartView.as_view(), name='cart'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('reduce_quantity/<slug>', reduce_quantity, name='reduce_quantity'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
]
