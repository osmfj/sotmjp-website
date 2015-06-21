from django.conf.urls import url, patterns


urlpatterns = patterns("sotmjp.profile.views",
    url(r"^edit/$", "profile_edit", name="profile_edit"),
)
