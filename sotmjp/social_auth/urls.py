from django.conf.urls import patterns, url

from symposion.social_auth.views import SocialAuths

urlpatterns = patterns("", url(r"^$", SocialAuths.as_view(),
                               name="social_auth_associations"))
