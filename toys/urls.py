from django.urls import path
from . import views

urlpatterns = [
    path('toy/', views.ToyList.as_view(), name='toy'),
    path('toy/<int:id>/', views.ToyDetail.as_view(), name='toy-detail')
]