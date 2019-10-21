from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles,article_source,search_article
from ..model import Articles,Sources

#Views 
@main.route('/')
def index():
    '''
    Views thats renders news sources to the home page
    '''
    general_news = get_sources('general')
    business_news = get_sources('business')
    sport_news = get_sources('sports')
    # tech_news = get_sources('technology')
    # health_news = get_sources('health')
    
    return render_template('index.html',general = general_news,business=business_news,sports=sport_news)

@main.route('/articles/<id>')
def sourceArticle(id):
    '''
    Views thats renders news sources to the home page
    '''
    all_articles = article_source(id)
    print(all_articles)
    source = id
    return render_template('sourcearticles.html', articles = all_articles, source = source)

@main.route('/News-Articles')
def NewsArticle():
    '''
    views that returns the news article
    '''
    education_article = get_articles('education')
    health_article = get_articles('health')

    return render_template('article.html', education = education_article,health=health_article)

@main.route('/search/<articl>')
def articleSearch(article_name):
    '''
    a function that returns the searched articles
    '''
    search_article_name = article_name.split(" ")
    search_name_format = "+".join(search_article_name)
    searched_articles = search_article(search_name_format)

    return render_template('search.html',articles = searched_articles   )