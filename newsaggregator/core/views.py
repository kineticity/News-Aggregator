from django.shortcuts import render
from .models import NewsArticle

def home(request):
    # Get the selected category from the query parameter (default to 'General' if not provided)
    category = request.GET.get('category', 'General')
    
    # Fetch articles filtered by the selected category, ordered by the most recent published date
    articles = NewsArticle.objects.filter(category=category).order_by('-published_at')
    
    # Return the context to the template for rendering
    return render(request, 'core/home.html', {'articles': articles, 'category': category})
