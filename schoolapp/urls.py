from django.urls import path
from schoolapp import views, HodViews
from school import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ShowLoginPage, name='login_page'),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
    path('admin_home',HodViews.admin_home,name="admin_home"),
    path('add_staff',HodViews.add_staff,name="add_staff"),
    path('add_staff_save',HodViews.add_staff_save,name="add_staff_save"),
    path('add_course',HodViews.add_course,name="add_course"),
    path('add_course_save',HodViews.add_course_save,name="add_course_save"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
