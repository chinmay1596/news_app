# news/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Search, Article
from .forms import SearchForm
from .news_api import fetch_news
from datetime import datetime, timedelta

@login_required
def search(request):
    """
    Handle the search functionality.

    If the request method is POST, processes the SearchForm with the submitted data.
    If the form is valid, checks if a recent search for the same keyword exists within the last 15 minutes.
    If a recent search exists, redirects to the results page of that search.
    If not, creates a new search, fetches articles from the news API, saves them, and redirects to the results page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered search page if the request method is GET, 
                      or a redirect to the results page if the form is valid and the search is created.
    """

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            # Check if the search was performed in the last 15 minutes
            threshold_time = datetime.now() - timedelta(minutes=15)
            recent_search = Search.objects.filter(keyword=keyword, user=request.user, created_at__gte=threshold_time).first()
            if recent_search:
                return redirect('results', search_id=recent_search.id)

            search, created = Search.objects.get_or_create(
                keyword=keyword,
                user=request.user,
            )
            
            articles = fetch_news(keyword)
            for article in articles:
                Article.objects.create(
                    search=search,
                    title=article['title'],
                    description=article['description'],
                    url=article['url'],
                    published_at=article['publishedAt'],
                    source_name=article['source']['name'],
                    category=article.get('category', ''),
                    language=article.get('language', '')
                )
            return redirect('results', search_id=search.id)
    else:
        form = SearchForm()
    return render(request, 'news/search.html', {'form': form})

@login_required
def results(request, search_id):
    """
    Display the search results with optional filters.

    Fetches the search object and its associated articles. 
    Applies filters for date and source name if provided in the request.
    Renders the results page with the filtered articles.

    Args:
        request: The HTTP request object.
        search_id: The ID of the search object.

    Returns:
        HttpResponse: The rendered results page.
    """

    search = Search.objects.get(id=search_id, user=request.user)
    articles = Article.objects.filter(search=search).order_by('-published_at')

     # Apply filters
    date_filter = request.GET.get('date')
    source_filter = request.GET.get('source')

    if date_filter:
        articles = articles.filter(published_at__date=date_filter)
    if source_filter:
        articles = articles.filter(source_name__icontains=source_filter)
    

    return render(request, 'news/results.html', {'search': search, 'articles': articles})



@login_required
def refresh_results(request, search_id):
    """
    Refresh search results by fetching new articles from the news API.

    Fetches new articles published after the last stored article's publication date.
    Saves the new articles and updates the search object.

    Args:
        request: The HTTP request object.
        search_id: The ID of the search object.

    Returns:
        HttpResponse: Redirect to the results page.
    """

    search = get_object_or_404(Search, id=search_id, user=request.user)
    last_published_article = search.article_set.order_by('-published_at').first()
    if last_published_article:
        last_published_date = last_published_article.published_at
    else:
        last_published_date = datetime.min

    articles = fetch_news(search.keyword, last_published_date)
    new_articles = [article for article in articles if datetime.fromisoformat(article['publishedAt'].replace('Z', '+00:00')) > last_published_date]
    
    for article in new_articles:
        Article.objects.create(
            search=search,
            title=article['title'],
            description=article['description'],
            url=article['url'],
            published_at=article['publishedAt'],
            source_name=article['source']['name'],
            category=article.get('category', ''),
            language=article.get('language', '')
        )
    return redirect('results', search_id=search.id)


@login_required
def search_list(request):
    """
    Display a list of searches made by the user.

    Fetches all searches made by the logged-in user and orders them by creation date.
    Renders the search list page with the user's searches.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered search list page.
    """
    
    searches = Search.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'news/search_list.html', {'searches': searches})