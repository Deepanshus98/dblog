from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^degree/$',views.DegreeView.as_view(),name='degree'),
    url(r'^login/$',views.LoginView.as_view(),name='login'),
    url(r'^logout/$',views.LogoutView.as_view(),name='logout'),


    url(r'^education/$',views.EducationView.as_view(),name='education'),
    url(r'^industrialskills/$',views.IndustrialskillsView.as_view(),name='industrialskills'),
    url(r'^internships/$',views.InternshipsView.as_view(),name='internships'),
    url(r'^computerskills/$',views.ComputerskillsView.as_view(),name='computerskills'),
    url(r'^otherskills/$',views.OtherskillsView.as_view(),name='otherskills'),
    url(r'^volunteering/$',views.VolunteeringView.as_view(),name='volunteering'),
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^cvlists/$',views.CvlistView.as_view(),name='cvlists'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
