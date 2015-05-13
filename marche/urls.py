from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'marche.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'collections/', include('collection.urls')),
    url(r'', include('collection.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^done/$', 'collection.views.post_list', name='done')
]
