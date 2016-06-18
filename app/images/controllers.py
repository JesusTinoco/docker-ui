from flask import Blueprint, request, render_template
from docker import Client

cli = Client(base_url='unix://var/run/docker.sock')

images = Blueprint('images', __name__, url_prefix='/images')

@images.route('/list/', methods=['GET'])
def list():
    imagesList = cli.images(all=True)
    return render_template('images/list.html', images=imagesList)
