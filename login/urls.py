from django.conf.urls import url
from . import views
 
# urlpatterns = patterns('login.views',
#     url(r'^login/', 'loginView'),
#     url(r'^greeting/', 'formView'),
#     url(r'^logout/', 'logoutView')
# )

app_name = "login"
urlpatterns = [
    url(r'^login/', views.loginView, name="loginView"),
    url(r'^greeting/', views.formView),
    url(r'^logout/', views.logoutView)
]
