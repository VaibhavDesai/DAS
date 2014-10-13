from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'audit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'home/','daudit.views.home',name="home"),

    url(r'DOSignUP/','daudit.views.SignUp',{'role':'DO'},name="DOSignUP"),
    url(r'DSignIn/','daudit.views.SignIn',{'role':'DO'},name="DSignIn"),
    url(r'DOHome/(?P<username>\w+)','daudit.views.DOHome',name="DOHome"),
    url(r'UploadFile/(?P<username>\w+)','daudit.views.UploadFile',name="uploadFile"),
    url(r'FileDetails/(?P<username>\w+)','daudit.views.FileDetails',name="FileDetails"),

    url(r'UserSignUP/','daudit.views.SignUp',{'role':'User'},name="UserSignUP"),
    url(r'USignIn/','daudit.views.SignIn',{'role':'User'},name="USignIn"),

    url(r'TPASignIn/','daudit.views.TPASignIn',name="TPASignIn"),
    url(r'TPAHome/','daudit.views.TPAHome',name="TPAHome"),
    url(r'TPAListFiles/','daudit.views.TPAListFiles',name="TPAListFiles"),
    url(r'TPAVerified/','daudit.views.TPAVerified',name="TPAVerified"),
    url(r'TPAVerify/(?P<file_id>\d+)','daudit.views.TPAVerify',name="TPAVerify"),
)
