from django.urls import path
from .views import loadtemplateview, registrationview, details_view 

urlpatterns = [
    path('', loadtemplateview.as_view(), name="Home"),
    path('login/', loadtemplateview.as_view(template_name='Home/login.html'), name='login'),
    path('submit_details/', registrationview, name='submit_details'),
    path('details/', details_view, name='details'),
]
