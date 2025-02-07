from django.urls import path
from .views import range_followers,emails_by_domain,reset_followers_followings,update_followers_followings

urlpatterns = [
    path('range_followers/', range_followers),
    path('emails_by_domain/', emails_by_domain),
    path('reset_followers_followings/', reset_followers_followings),
    path('update_followers_followings/', update_followers_followings),
]