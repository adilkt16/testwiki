from django.urls import path , include
from users import views


app_name = "users"

urlpatterns = [
    path('login/',views.login,name="login"),
    path('logout/', views.logout,name="logout"),
    path('signup/', views.signup,name="signup"), 
    path('terms_and_conditions/', views.t_and_c,name="t_and_c"), 

    path("send_otp",views.send_otp,name="send otp"),
]

