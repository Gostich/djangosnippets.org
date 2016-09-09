from django.conf.urls import url

from ..views import snippets

urlpatterns = [
    url(r'^$',
        snippets.snippet_list,
        name='cab_snippet_list'),
    url(r'^(?P<snippet_id>\d+)/$',
        snippets.snippet_detail,
        name='cab_snippet_detail'),
    url(r'^(?P<snippet_id>\d+)/rate/$',
        snippets.rate_snippet,
        name='cab_snippet_rate'),
    url(r'^(?P<snippet_id>\d+)/download/$',
        snippets.download_snippet,
        name='cab_snippet_download'),
    url(r'^(?P<snippet_id>\d+)/raw/$',
        snippets.raw_snippet,
        name='cab_snippet_raw'),
    url(r'^(?P<snippet_id>\d+)/edit/$',
        snippets.edit_snippet,
        name='cab_snippet_edit'),
    url(r'^(?P<snippet_id>\d+)/flag/$',
        snippets.flag_snippet,
        name='cab_snippet_flag'),
    url(r'^add/$',
        snippets.edit_snippet,
        name='cab_snippet_add'),
    url(r'^tag-hint/$',
        snippets.tag_hint,
        name='cab_snippet_tag_hint'),
]