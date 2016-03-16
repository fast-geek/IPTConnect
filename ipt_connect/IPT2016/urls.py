from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
    url(r'^$', home),
	url(r'^tournament$', tournament_overview),
    url(r'^participants$', participants_overview, name='participants_overview'),
    url(r'^participants/(?P<pk>[0-9]+)/$', participant_detail, name='participant_detail'),
    url(r'^jurys$', jurys_overview, name='jurys_overview'),
    url(r'^jurys/(?P<pk>[0-9]+)/$', jury_detail, name='jury_detail'),
	url(r'^problems$', problems_overview, name="problems_overview"),
	url(r'^problems/(?P<pk>[0-9]+)/$', problem_detail, name="problem_detail"),
	url(r'^physics_fights$', physics_fights, name="physics_fights"),
	url(r'^physics_fights/(?P<pk>[0-9]+)/$', physics_fight_detail, name="physics_fight_detail"),
	url(r'^teams$', teams_overview, name="teams"),
	url(r'^teams/(?P<team_name>[A-Za-z]+)/$', team_detail, name='team_detail')

)
