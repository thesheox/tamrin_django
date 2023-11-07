
from django.urls import path
from website.views import home_view,contact_view,about_view
app_name="website"
urlpatterns = [
    
    path('',home_view ),
    path('contact/',contact_view),
    path('about/',about_view )
]
