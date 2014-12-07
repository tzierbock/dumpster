from django.shortcuts import render, get_object_or_404
from publisher.models import Article


def home(request):
	articles = Article.objects.all()

	if len(articles) > 0:
		return render(request, 'publisher/home.html', {'articles':articles, 'no_content':False})
	else:
		return render(request, 'publisher/home.html', {'no_content':True})