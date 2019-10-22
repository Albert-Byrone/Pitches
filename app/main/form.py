from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProf(FlaskForm):
    bio = TextAreaField('Write something about you',validators=[Required()])
    submit = SubmitField('Update')

class IdeaForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    category = SelectField('Category',choices=[('Interview','Interview'),('Events','Events'),('Job','Job')],validators=[Required()])
    post = TextAreaField('Your idea',validators=[Required()])
    submit = SubmitField('Share your idea')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')
    