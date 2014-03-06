
from django.conf.urls import patterns,url
from django.http.response import HttpResponse



urlpatterns = patterns('auth.views',
        
    #url(r'^$','authenticate.v_home'),
    
    url(r'^login/$','authenticate.v_login'),
    url(r'^logout/$','authenticate.v_logout'),
    url(r'^forgotPassword/$','authenticate.v_forgotPassword'),
    url(r'^resetPassword/$','authenticate.v_resetPassword'),
    
    url(r'^signup/$','user.v_add_user'),
    url(r'^setting/$','user.v_edit_user'),
    
    url(r'^validate$','authenticate.v_validate'),
    url(r'^recoverPassword$','authenticate.v_recoverPassword'),
    url(r'^webo$',lambda req:HttpResponse("done")),
    #url(r'^validate2/$','authenticate.v_validate2'),      
    #url(r'^test$','authenticate.v_test'),
)