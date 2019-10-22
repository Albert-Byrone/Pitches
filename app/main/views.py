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

@main.route('/create_new',methods=['GET','POST'])
@login_required
def new_pitch():
    form = IdeaForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_pitches()
        return redirect(url_for('main.index'))
    return render_template('pitch.html',form = form)

@main.route('/comment/<int:pitch_id>',methods=['GET','POST'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_comments()
        return redirect(url_for('.comment',pitch_id=pitch_id))
    return render_template('comment.html',form=form,pitch=pitch,all_comments=all_comments)

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username =name).first()
    user_id = current_user._get_current_object().id
    posts = Pitch.query.filter_by(user_id=user_id).all()
    if user is None:
        abort(404)
    return render_template("profile/profile.html",user= user,posts=posts)


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