from django.urls import path
from . import views

# localhost:8000/chai
# localhost:8000/chai/order
urlpatterns = [
    path('', views.hello, name = 'hello'),
    
    path('<int:chai_id>/', views.chai_detail, name = 'chai_detail')
    # path('order/', views.order, name='order'),
]