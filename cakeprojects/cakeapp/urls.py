from django.urls import path
from .import views
app_name='cakeapp'

urlpatterns=[
    path('',views.home,name='home'),
    path('cake/<int:cake_id>/',views.details,name='details'),
    path('add/',views.add_cake,name='add_cake'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]