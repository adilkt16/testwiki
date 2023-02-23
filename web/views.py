import json
from multiprocessing import context

from django.views.generic import DeleteView
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator #import Paginator
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.core.exceptions import PermissionDenied
from django.contrib.messages import constants as messages
from django.views.decorators.csrf import csrf_exempt

from posts.forms import BlogPostForm
from posts.models import BlogPost


def index(request):
	context = {
		"title" : "HOme page",
	}
	return render(request,'web/index.html',context=context)


@login_required(login_url = "/users/login/")
def view_all_created(request):
	posts_all = BlogPost.objects.all()
	my_own = BlogPost.objects.filter()
	what = BlogPost.objects.filter()
	post_created = True
	current_user_posts = BlogPost.objects.filter( is_deleted=False, name=request.user.username)

	qs = BlogPost.objects.all()
	q = request.GET.get("q")
	
	paginator = Paginator(posts_all, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	if current_user_posts.exists() and not current_user_posts.first().is_deleted:	
		my_own = True
		posts_all = BlogPost.objects.filter()
		# my_own = BlogPost.objects.filter()
		what = BlogPost.objects.filter()
		post_created = True	
		current_user_post = current_user_posts	

		if q:	
			qs = BlogPost.objects.annotate(search=SearchVector("name", "occupation")).filter(search=SearchQuery(q))	
			context = {
				"queryset": qs,
				'post_created':post_created,
				'my_own': my_own,
				'posts_all': page_obj,
				'what': what,
				"title" : "View All users",
				'current_user_post': current_user_post
			}
			return render(request, "web/all_users.html", context=context)

		return render(request, 'web/all_users.html', {'post_created':post_created,'my_own': my_own,'posts_all': page_obj,'what': what, "title" : "View All users",'current_user_post': current_user_post,"queryset": qs})	
	else:	
		my_own = False
		what = "something"	
		return render(request, 'web/all_users.html', {'my_own': my_own, 'posts_all': page_obj,'what': what,"queryset": qs,})


@login_required(login_url = "/users/login/")
@csrf_exempt
def create_post(request):
	context = {
		"title" : "Create Your Wiki Page"
	}
	return render(request,"web/create.html",context=context)


@login_required(login_url = "/users/login/")
@csrf_exempt
def add_wiki(request):
	posts_created_by_user = BlogPost.objects.filter(name=request.user.username)
	if posts_created_by_user.exists():
		return redirect('web:view_after_delete')
	if request.method=="POST":
		form = BlogPostForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			blogpost = form.save(commit=False)
			blogpost.name = request.user.username
			blogpost.save()
			return redirect('web:view_all_created')
		else:
			print(form.errors)
	else:
		form=BlogPostForm()
	return render(request, "web/create.html", {'form':form})


@login_required(login_url = "/users/login/")
def view_after_delete(request):	
	posts_all = BlogPost.objects.filter()
	what = BlogPost.objects.filter()
	qs = BlogPost.objects.all()
	q = request.GET.get("q")

	if q:	
		qs = BlogPost.objects.annotate(search=SearchVector("name", "occupation")).filter(search=SearchQuery(q))	
		context = {
			"queryset": qs,
		}
		return render(request, "web/all_users.html", context=context)

	context = {
		"posts_all" : posts_all,
		"what" : what,
		"title" : "View AFter delete users",
		"queryset": qs,
	}
	return render(request,"web/after_delete.html",context=context)


@login_required(login_url = "/users/login/")
def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.user.username == post.name or request.user.is_staff:
    # if request.user == post.name or request.user.is_staff:
        post.delete()
        # messages.success(request, "The post was successfully deleted.")
        return redirect('web:view_after_delete')
    else:
        raise PermissionDenied


def wikidetail(request,id,slugged):
	post = get_object_or_404(BlogPost, id=id, slug=slugged)
	posts_all = BlogPost.objects.filter()
	paginator = Paginator(posts_all, 3)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	qs = BlogPost.objects.all()
	q = request.GET.get("q")

	if q:	
		qs = BlogPost.objects.annotate(search=SearchVector("name", "occupation")).filter(search=SearchQuery(q))	
		context = {
				"queryset": qs,
				'posts_all': page_obj,
				"posts_all" : page_obj,
				"instance" : post,
				"link" : str(id) ,
				"title" : "Wikipedia user name",
		}
		return render(request, "web/basil.html", context=context)


	context ={
		"posts_all" : page_obj,
		"instance" : post,
		"link" : str(id) ,
		"queryset": qs,
		# "post":post,
	}
	return render(request,'web/basil.html',context=context) 


def adil(request):
	context = {
		"title" : "Creator page",
	}
	return render(request,'users/creatorAdil.html',context=context)