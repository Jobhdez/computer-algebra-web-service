from django.urls import path
from api import views
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('request/', views.request_friend, name='request'),
    path('accept/', views.accept_friend_request, name='accept'),
    path('computeDiff/', views.compute_diff_expression, name='diff'),
    path('computeAlg/', views.compute_lalg_expression, name='lalg'),
    path('computePoly/', views.compute_poly_expression, name='poly'),
]