from django.conf.urls.defaults import patterns

urlpatterns = patterns('upload.views',
    (r'^$', 'index'),
)
