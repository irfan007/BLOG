
from django.conf.urls import patterns,url



urlpatterns = patterns('auth.views',
        
    #url(r'^$','authenticate.v_home'),
    url(r'^login/$','authenticate.v_login'),
    url(r'^logout/$','authenticate.v_logout'),
    url(r'^forgotPassword/$','authenticate.v_forgotPassword'),
    url(r'^resetPassword/$','authenticate.v_resetPassword'),
    
    url(r'^signup/$','user.v_add_user'),
    url(r'^setting/$','user.v_edit_user'),      
 
)