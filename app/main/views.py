from flask import render_template,redirect,url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment,Upvote,Downvote
from .. import db,photos
from .form import IdeaForm,CommentForm,UpdateProf

@main.route('/')
def index():
    pitches = Pitch.query.all()
    event = Pitch.query.filter_by(category = 'Event').all()
    interview = Pitch.query.filter_by(category='Interview').all()
    job = Pitch.query.filter_by(category='Job')
    
    return render_template('index.html',job=job,event=event,interview=interview,pitches=pitches)


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