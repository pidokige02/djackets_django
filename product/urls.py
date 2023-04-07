from django.urls import path, include

from product import views  # directory 에서 file import 하는 것이 가능함

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]