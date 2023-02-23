from django.shortcuts import render , reverse
from django.contrib.auth import authenticate , login as auth_login , logout as auth_logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


from users.forms import UserForm
from main.functions import generate_form_errors




def custom_page_not_found_view(request, exception):
    return render(request, "users/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "users/404.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "users/404.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "users/404.html", {})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return HttpResponseRedirect(reverse("web:view_all_created"))
            else:
                context = {
                    "title" : "Login",
                    "error" : True,
                    "message" : "Invalid username or password"
                }
                return render(request,"users/login.html",context=context)
        else:
            context = {
                "title" : "Login",
                "error" : True,
                "message" : "Invalid username or password"
            }
            return render(request,"users/login.html",context=context)
    context = {
        "title" : "Log inned"
    }
    return render(request,"users/login.html",context=context)




from django.shortcuts import render , reverse
from django.http.response import HttpResponseRedirect

@csrf_exempt
def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse("web:index"))


@csrf_exempt
def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)

			User.objects.create_user(
						username=instance.username,
						password=instance.password,
						email=instance.email,
			)

			user = authenticate(request,username=instance.username,password=instance.password)
			auth_login(request,user)
				
			return HttpResponseRedirect(reverse("web:view_all_created"))
		else:
			message = generate_form_errors(form)
			form = UserForm()    
			context = {
					"title" : "Signup" ,
					"error" : True,
					"message" : message,
					"form" : form,
			}
			return render(request,"users/signup.html",context=context)

	else:
		form = UserForm()   
		context = {
				"title" : "SIgnup",
				"form" : form,
		}
		return render(request,"users/signup.html",context=context)






from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random


@csrf_exempt
def generateOTP() :
	digits = "0123456789"
	OTP = ""
	for i in range(4) :
		OTP += digits[math.floor(random.random() * 10)]
	return OTP

@csrf_exempt
def send_otp(request):
	# email=request.POST.get("email")
	gmail=request.POST.get("email")
	email=request.GET.get("email")
	o=generateOTP()
	htmlgen = f'<p>Your OTP is <strong>{o}</strong></p>'
	result = send_mail('OTP request',o,'wikipageverify@gmail.com',[gmail],  fail_silently=False, html_message=htmlgen)

	return HttpResponse(o)




def t_and_c(request):
	context = {
		"title" : "Terms and conditions page",
	}
	return render(request,'users/terms.html')