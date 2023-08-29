
from django.urls import path, include
from core.views import CorePageView, MainView

#@[p_core_urls_01]

core_patterns = ([
	path('',MainView.as_view(),name='main'),
#@[p_core_urls_02]
	path('home/',CorePageView.as_view(),name='home'),
],'core')

#@[p_core_urls_03]


