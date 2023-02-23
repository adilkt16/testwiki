from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path as url
from django.views.static import serve

from users import views 


handler404 = 'users.views.custom_page_not_found_view'
handler500 = 'users.views.custom_error_view'
handler403 = 'users.views.custom_permission_denied_view'
handler400 = 'users.views.custom_bad_request_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include("users.urls",namespace="users")),
    path('', include("web.urls",namespace="web")),
    path("send_otp",views.send_otp,name="send otp"),
    # path('posts/', include("posts.urls",namespace="posts")),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]
if settings.DEBUG:
	urlpatterns += (
	static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) +
	static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
)