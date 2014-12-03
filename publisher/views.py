from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Article
import markdown

def md(text):
    return markdown.markdown(text, ['codehilite(force_linenos=True)', 'fenced_code', 'wikilinks(end_url=)'])

# Create your views here.
def get_article(request, article_id):
	article = get_object_or_404(Article, pk=article_id)

	options = {
		'author': article.getAuthor(),
		'heading': article.heading,
		'pub_date': article.date_published,
		'content': md(article.content)
	}
	
	return render(request, 'publisher/article_basic.html', options)