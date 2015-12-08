from mezzanine import template
from mezzanine.utils.models import get_user_model
from newtest00.models import Programming

User = get_user_model()
register = template.Library()

@register.as_tag
def programming_recent_post(limit=5, username=None):
	"""
	Put a list of recently publushed programming articles into the template context.
	"""

	articles = Programming.objects.published().select_related().filter(add_toc=False).order_by('-publish_date')
	if username is not None:
		try:
			author = User.objects.get(username=username)
			articles = articles.filter(user=author)
		except User.DoesNotExist:
			return []
	return list(articles[:limit])