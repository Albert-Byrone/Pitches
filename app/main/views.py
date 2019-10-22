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

@main.route('/user/<name>/updateprof',methods=['GET','POST'])
@login_required
def updateprof(name):
    form = UpdateProf()
    user= User.query.filter_by(username = name).first()
    if user is None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_user()
        return redirect(url_for('.profile',name=name))
    return render_template('profile/update.html' ,form=form)

@main.route('/user/<name>/update/pic',methods=['GET','POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username=name).first()
    if 'photo' is request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path =path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))

@main.route('/like/<int:id>',methods=['GET','POST'])
@login_required
def like(id):
    get_pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pit in get_pitches:
        to_str = f'{pit}'
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user=current_user,pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods=['GET','POST'])
@login_required
def dislike(id):
    pitch = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in pitch:
        to_str = f'{p}'
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user=current_user,pitch_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id=id))


