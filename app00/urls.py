from django.urls import path
from . import views

urlpatterns = [
    path('register/<str:usr_id>/', views.register_user, name='register_user'),
    path('noo/', views.members, name='noo'),
    path('register/<str:prnt_id>/<str:usr_id>/', views.register_printer, name='register_printer '),
    path('printouts/<str:po>/<str:usr>/', views.printouts, name='printouts')
]
