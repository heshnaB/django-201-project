from django.urls import path
from .views import EditProfileView, ProfileDetailView, FollowView


app_name = "profiles"

urlpatterns = [
    path('edit/', EditProfileView.as_view(), name='edit_profile'),
    path("<str:username>/", ProfileDetailView.as_view(), name="detail"),
    path("<str:username>/follow/", FollowView.as_view(), name="follow"),
]
