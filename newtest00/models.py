from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.generic.fields import CommentsField
from mezzanine.pages.models import Page, RichText

class Author(Page):
	dob = models.DateField("Date of Birth")

class Book(models.Model):
	author = models.ForeignKey("Author")
	test_data = models.CharField(max_length=200)

class TestModel(models.Model):
	title = models.CharField(max_length=200)
	language = models.CharField(max_length=200)
	topic = models.CharField(max_length=200)

class DocPage(Page, RichText):
	"""Doc tree page"""
	add_toc = models.BooleanField(_("ADD TOC"), default=False, help_text=_("Include a list of child links"))
	allow_comments = models.BooleanField(verbose_name=_("Allow comments"), default=False)
	comments = CommentsField(verbose_name=_("Comments"))

	class Meta:
		verbose_name = _("Doc Page")
		verbose_name_plural = _("Doc Pages")

class Programming(Page, RichText):
	"""testing new model check if CharField needs to be entered"""
	add_toc = models.BooleanField(_("ADD TOC"), default=False, help_text=_("Include a list of child links"))
	allow_comments = models.BooleanField(verbose_name=_("Allow comments"), default=False)
	comments = CommentsField(verbose_name=_("Comments"))
	tutorial_url = models.URLField(max_length=100, blank=True, help_text=_("Add source of the tutorial"))
	program_language = models.CharField(max_length=100, blank=True, help_text=_("Add programming language of tutorial"))
	allow_toc = models.BooleanField(_("Add assist toc"), default=False, help_text=_("include a side bar of toc"))
	allow_content = models.BooleanField(_("Show content"), default=False, help_text=("include page content"))

class TestAssist(models.Model):
	main_tutorial = models.ForeignKey("Programming")
	topic = models.CharField(max_length=200, blank=True)
	# language = models.CharField(max_length=200, blank=True)
