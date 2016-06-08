from flask import Blueprint, request, render_template
from docker import Client

cli = Client(base_url='unix://var/run/docker.sock')

containers = Blueprint('containers', __name__, url_prefix='/containers')

@containers.route('/list/', methods=['GET'])
def list():
    containerList = cli.containers(all=True)
    return render_template('containers/list.html', containers=containerList)