from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('generate_result/<int:fileid>', views.generate_result, name="generate_result"),
    path('delete_record/<int:id>', views.delete_record, name="delete_record")
]