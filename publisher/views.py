from django.shortcuts import render
from django.http import HttpResponse
from models import Article
import markdown

def md(text):
    return markdown.markdown(text, ['codehilite(force_linenos=True)', 'fenced_code', 'wikilinks(end_url=)'])

# Create your views here.
def get_article(response, article_id):
	articles = Article.objects.filter(heading=article_id)
	
	if articles:
		article = articles[0]
		return HttpResponse("{0}<br>{1}".format(str(article.heading), str(md(article.content)))
)
	r = HttpResponse("Not found")
	r.code = 404
	return r
