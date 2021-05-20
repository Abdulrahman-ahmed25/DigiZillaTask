"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from signup.views import signup_view
from profiles.views import view_profile,file_list,file_upload,GenericsList,GenericsBk
from home.views import calculate_distance
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),

#for RESTFUL API about UploadFile model
    path('api-auth/', include('rest_framework.urls')),
#GET POST from REST framework by class based views using Mixins
    path('rest/genericslist/', GenericsList.as_view()), 
#GET PUT DELETE from REST framework by class based views using Mixins
    path('rest/genericslist/<int:pk>', GenericsBk.as_view()),


#for user profile page
    path('',calculate_distance ,name='calculateDistance'),
    path('profile/',view_profile, name='profile'),
    path('profile/files/',file_list, name='file_list'),
    path('profile/files/upload',file_upload, name='file_upload'),

# authentications urls
    path('signup/',signup_view, name='signup'),
    path('accounts/',include("django.contrib.auth.urls")),
    path('change_password', auth_view.PasswordChangeView.as_view(
        template_name = 'registration/password_change.html',
        success_url = '/'
    ), name='change_password' ),

# for resent password urls
    path('reset_password', auth_view.PasswordResetView.as_view(
    template_name = 'registration/reset_password.html',)
    , name='reset_password' ),

    path('reset_password/done/',auth_view.PasswordResetDoneView.as_view(
        template_name = 'registration/reset_password_done.html',)
        ,name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(
        template_name = 'registration/reset_password_confirm.html',)
        ,name='password_reset_confirm'),

    path('reset/done/',auth_view.PasswordResetCompleteView.as_view(
        template_name = 'registration/reset_password_complete.html',),
        name='password_reset_complete'),

]
# media_url and static_url
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

