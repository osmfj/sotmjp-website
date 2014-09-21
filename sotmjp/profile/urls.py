from django.conf.urls.defaults import *


urlpatterns = patterns("sotmjp.profile.views",
    url(r"^edit/$", "profile_edit", name="profile_edit"),
)
