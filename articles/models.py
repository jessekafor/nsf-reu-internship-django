from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Articles(models.Model):
	user = models.ForeignKey(User,default=1, on_delete=models.CASCADE)
	title = models.CharField(max_length=9999)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	journal_id = models.CharField(max_length=9999)
	journal_title = models.CharField(max_length=9999)
	issn_ppub = models.CharField(max_length=9999)
	issn_epub = models.CharField(max_length=9999)
	publisher_name = models.CharField(max_length=9999)
	publisher_loc = models.CharField(max_length=9999)
	article_id_pmid = models.CharField(max_length=9999)
	article_id_pmc = models.CharField(max_length=9999)
	article_id_publisher_id = models.CharField(max_length=9999)
	article_id_doi = models.CharField(max_length=9999)
	article_subject = models.CharField(max_length=9999)
	article_title = RichTextField()
	contrib_group = RichTextField()
	aff1 = RichTextField()
	aff2 = RichTextField()
	aff3 = RichTextField()
	pub_date_ppub = RichTextField()
	pub_date_epub = RichTextField()
	volume = models.CharField(max_length=9999)
	issue = models.CharField(max_length=9999)
	fpage = models.CharField(max_length=9999)
	lpage = models.CharField(max_length=9999)
	history = RichTextField()
	copyright_statement = RichTextField()
	abstract = RichTextField()
	keywords = RichTextField()
	sec_methods = RichTextField()
	body = RichTextField()
	ref_list = RichTextField()
	sec_display_objects = RichTextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/Project/articles/%s/" % self.id

	class Meta:
		verbose_name_plural = "Articles"
