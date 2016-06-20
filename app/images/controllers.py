from flask import Blueprint, request, render_template
from docker import Client

cli = Client(base_url='unix://var/run/docker.sock')

images = Blueprint('images', __name__, url_prefix='/images')

@images.route('/list/', methods=['GET'])
def list():
    images = cli.images(all=True)
    return images_list('images/list.html', images)

def images_list(template, images_list):
    search = request.args.get('q')
    images_filtered = images_list
    if search:
        images_filtered = []
        for image in images_list:
            print image
            if search in str(image["RepoTags"][0].split(':')[0]):
                images_filtered.append(image)
    return render_template(template, images=images_filtered)
