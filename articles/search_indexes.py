import datetime
from haystack import indexes
from articles.models import Articles
#from models import Articles

class ArticlesIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	author = indexes.CharField(model_attr='user')
	title = indexes.CharField(model_attr='title', boost=1.125)
	article_title = indexes.CharField(model_attr='article_title')
	article_subject = indexes.CharField(model_attr='article_subject', faceted=True)
	journal_title = indexes.CharField(model_attr='journal_title', faceted=True)
	keywords = indexes.CharField(model_attr='keywords',faceted=True)
	publisher_name = indexes.CharField(model_attr='publisher_name')
	created_at = indexes.DateTimeField(model_attr='created_at')
	title_auto = indexes.EdgeNgramField(model_attr='title')	
	def get_model(self):
		return Articles

	def index_queryset(self, using=None):
		return self.get_model().objects.filter(created_at__lte=datetime.datetime.now())
