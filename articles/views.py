from django.shortcuts import render
from django.http import HttpResponse
from . models import Articles
from django.views.generic import TemplateView
from haystack.views import SearchView
from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet
from haystack.forms import FacetedSearchForm
from haystack.generic_views import FacetedSearchView as BaseFacetedSearchView
from django.core.paginator import Paginator
from haystack.utils import Highlighter

# Create your views here.

def index(request):
	articles = Articles.objects.all()[:10]
	context = {
		'title': 'Latest Articles',
		'articles': articles
	}

	# return HttpResponse('Hello World')
	return render(request, 'articles/index.html', context)

def details(request, id):
	article = Articles.objects.get(id=id)

	context = {
		'article': article
	}

	return render(request, 'articles/details.html', context)

"""
class SearchView(SearchView):
	def create_response(self):
		(paginator, page) = self.build_page()
		context = {
			'query': self.query,
			'form': self.form,
			'page': page,
			'suggestion': None,
			'paginator': paginator,
			'results': self.results
		}

"""

class SearchView(TemplateView):
    template_name = 'articles/search.html'

search_view = SearchView.as_view()


class FacetedSearchView(BaseFacetedSearchView):
	form_class = FacetedSearchForm
	facet_fields = ['article_subject','journal_title','keywords']
	paginate_by = 10
	context_object_name = 'object_list'
	template_name = 'articles/search.html'

faceted_search_view = FacetedSearchView.as_view()
