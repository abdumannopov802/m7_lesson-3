from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('', CRUD_In_Generic_View.as_view(), name='crud'),
]
