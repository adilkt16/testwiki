from django.urls import path , include

from web import views


app_name = "web"

urlpatterns = [
	path('', views.index,name="index"),
    path('adil/', views.adil, name='adil'),
    path('view/', views.view_all_created, name='view_all_created'),
    path("view/add_wiki/", views.add_wiki, name="add_wiki"),
    path('<int:id>/<slug:slugged>/', views.wikidetail, name='wiki_detail'),
    path('delete/', views.view_after_delete,name="view_after_delete"),
    path("view/delete_post/<int:id>/", views.delete_post, name="delete_post")
]