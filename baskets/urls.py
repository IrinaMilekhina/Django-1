from django.urls import path

from baskets.views import baskets_add

app_name = 'baskets'
urlpatterns = [
    path('add/<int:product_id>', baskets_add, name='baskets_add'),
]