from flask import Blueprint, flash, request, render_template, redirect, url_for
from .forms import BuildImageForm
from docker import Client
from io import BytesIO

cli = Client(base_url='unix://var/run/docker.sock')

images = Blueprint('images', __name__, url_prefix='/images')

@images.route('/list/', methods=['GET'])
def list():
    images = cli.images(all=True)
    return images_list('images/list.html', images)

@images.route('/<string:image_id>/delete', methods=['POST'])
def delete_image(image_id):
    try:
        cli.remove_image(image_id)
        flash('Image "%s" has been deleted successfully.' % image_id, 'success')
    except Exception as err:
        print err
        flash(str(err), 'warning')
    return redirect(url_for('images.list'))

@images.route('/build/', methods=['GET', 'POST'])
def build():
    form = BuildImageForm()
    
    if form.validate():
        print 'Valid form'

    if form.is_submitted() and len(form.errors) != 0:
        flash(form.errors, 'danger')

    if form.validate_on_submit():
        build_image(form)
        flash('Image was created...', 'warning')
        return redirect(url_for('images.list'))
 
    return render_template('images/build.html', form=form)

def build_image(form):
    try:
        dockerfile = BytesIO(form.dockerfile.data.encode('utf-8'))
        response = [line for line in cli.build(
            fileobj=dockerfile, 
            rm=form.rm.data, 
            tag=form.tag.data,
            nocache=form.nocache.data,
            pull=form.update.data
            )]
    except Exception as err:
        print err

def images_list(template, images_list):
    search = request.args.get('q')
    images_filtered = images_list
    if search:
        images_filtered = []
        for image in images_list:
            print image
            if search in str(image["RepoTags"][0].split(':')[0]):
                images_filtered.append(image)
    return render_template(template, images=images_filtered, image_active="active")
