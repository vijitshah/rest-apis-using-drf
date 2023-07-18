from django.urls import path
from .views import CartItemsViews

urlpatterns = [
    path("cart-items/", CartItemsViews.as_view()),
    path("cart-items/<int:id>", CartItemsViews.as_view())
]