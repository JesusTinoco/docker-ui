from flask import Blueprint, request, render_template
from docker import Client
from models import Container

cli = Client(base_url='unix://var/run/docker.sock')

containers = Blueprint('containers', __name__, url_prefix='/containers')

@containers.route('/list/', methods=['GET'])
def list():
    containerList = [Container(container) for container in cli.containers(all=True)]
    return render_template('containers/list.html', containers=containerList)

@containers.route('/<string:container_id>', methods=['GET'])
def container_info(container_id):
    print(container_id)
    container = cli.inspect_container(container_id)
    return render_template('containers/info.html', container = container)
