from flask import Blueprint, flash, request, render_template, redirect, url_for
from docker import Client
from models import Volume

cli = Client(base_url='unix://var/run/docker.sock')

volumes = Blueprint('volumes', __name__, url_prefix='/volumes')

@volumes.route('/list', methods=['GET'])
def list():
    volumes_aux = cli.volumes()["Volumes"]
    volumes = [] if volumes_aux is None else [Volume(volume) for volume in volumes_aux]
    return volumes_list('volumes/list.html', volumes)

@volumes.route('/<string:volume_name>/delete', methods=['POST'])
def remove_volume(volume_name):
    try:
        cli.remove_volume(volume_name)
        flash('Volume "%s" has been removed successfully.' % volume_name, 'success')
    except Exception as err:
        print err
        flash(str(err), 'warning')
    return redirect(url_for('volumes.list'))

def volumes_list(template, volume_list):
    search = request.args.get('q')
    volumes_filtered = volume_list
    if search:
        volumes_filtered = []
        for volume in volume_list:
            if search in volume.name():
                volumes_filtered.append(volume)
    return render_template(template, volumes=volumes_filtered)
