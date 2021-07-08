from django.urls import path

from baskets.views import baskets_add, basket_remove

app_name = 'baskets'
urlpatterns = [
    path('add/<int:product_id>', baskets_add, name='baskets_add'),
path('remove/<int:id>', basket_remove, name='basket_remove'),
]