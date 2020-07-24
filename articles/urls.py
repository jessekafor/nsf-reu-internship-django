from django.urls import path
from django.conf.urls import url
from . import views
from haystack.forms import FacetedSearchForm
from haystack.views import FacetedSearchView
from haystack.query import SearchQuerySet

sqs = SearchQuerySet().facet('article_subject')

urlpatterns = [
	path('', views.index, name='index'),
	path('search/', views.faceted_search_view, name='faceted_search_view'),
	path('<int:id>/', views.details, name='details'),
	path('search/',views.search_view, name='search_view'),
]

