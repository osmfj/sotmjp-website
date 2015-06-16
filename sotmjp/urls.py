from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from sitetree.sitetreeapp import register_i18n_trees

admin.autodiscover()

import symposion.views
import sotmjp.views
import sotmjp.profile.views

URL_PREFIX = settings.CONFERENCE_URL_PREFIXES[settings.CONFERENCE_ID]

urlpatterns = patterns("",
    url(r"^$", RedirectView.as_view(url="/%s/" % URL_PREFIX)),
    url(r"^%s/" % URL_PREFIX, include(patterns("",
        url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
        url(r"^admin/", include(admin.site.urls)),
        url(r"^account/signup/$", sotmjp.profile.views.SignupView.as_view(), name="account_signup"),
        url(r"^account/login/$", symposion.views.LoginView.as_view(), name="account_login"),
        #url(r"^account/social/", include("social_auth.urls")),
        #url(r"^account/associations/", include("social_auth.urls")),
        url(r"^account/", include("account.urls")),
        url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),
        url(r"^blog/", include("pynax.blog.urls")),
        url(r"^registration/", include("sotmjp.registration.urls")),

        url(r"^venue/$", TemplateView.as_view(template_name="venue/detail.html"), name="venue_detail"),

        url(r"^profile/", include("sotmjp.profile.urls")),
        url(r"^speaker/", include("symposion.speakers.urls")),
        url(r"^proposals/", include("symposion.proposals.urls")),
        url(r"^reviews/", include("symposion.reviews.urls")),
        url(r"^teams/", include("symposion.teams.urls")),
        url(r"^schedule/", include("symposion.schedule.urls")),
        url(r"^conference/", include("symposion.conference.urls")),

        url(r"^sponsors/", include("sotmjp.sponsorship.urls")),

        url(r"^boxes/", include("symposion.boxes.urls")),
        url(r"^sitemap/", TemplateView.as_view(template_name="static/sitemap.html"), name="sitemap"),
        url(r'^selectable/', include('selectable.urls')),
        url(r"^change_language/", symposion.views.change_language, name="change_language"),
        url('program_export/', sotmjp.views.program_export, name='program_export'),


        # This should be last, because it will create a new CMS page for
        # any unrecognized URL.
        url(r"^", include("restcms.urls")),
    )))
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# site uses "main" sitetree. so the name of internationalized one must_be "main_${lang_code}"
register_i18n_trees(['main'])
