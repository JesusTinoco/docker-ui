from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class BuildImageForm(Form):
	# tag (str): A tag to add to the final image
	tag = StringField('tag', validators=[DataRequired()])
	# dockerfile: A file object to use as the Dockerfile. (Or a file-like object)
	dockerfile = StringField('fileobj', validators=[DataRequired()], widget=TextArea())
	# rm (bool): Remove intermediate containers.
	rm = BooleanField('rm', default=True)
	# nocache (bool): Don't use the cache when set to True
	nocache = BooleanField('nocache', default=False)
	# update (bool): Downloads any updates to the FROM image in Dockerfile
	update = BooleanField('pull', default=False)