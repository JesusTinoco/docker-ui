from flask import Blueprint, request, render_template, redirect, url_for
from docker import Client
from models import Container

cli = Client(base_url='unix://var/run/docker.sock')

containers = Blueprint('containers', __name__, url_prefix='/containers')

@containers.route('/list/', methods=['GET'])
def list():
    containers = [Container(container) for container in cli.containers(all=True)]
    return containers_list('containers/list.html', containers)

@containers.route('/<string:container_id>', methods=['GET'])
def container_info(container_id):
    print(container_id)
    container = cli.inspect_container(container_id)
    return render_template('containers/info.html', container = container)

@containers.route('/<string:container_id>/start', methods=['POST'])
def start_container(container_id):
    # TODO: Add flash message throwing an error if the start method fails
    try:
        cli.start(container_id)
    except Error:
        print "Oops!"
    return redirect(url_for('containers.list'))

@containers.route('/<string:container_id>/restart', methods=['POST'])
def restart_container(container_id):
    # TODO: Add flash message throwing an error if the restart method fails
    try:
        cli.restart(container_id)
    except Error:
        print "Oops!"
    return redirect(url_for('containers.list'))

@containers.route('/<string:container_id>/stop', methods=['POST'])
def stop_container(container_id):
    # TODO: Add flash message throwing an error if the stop method fails
    try:
        cli.stop(container_id)
    except Error:
        print "Oops!"
    return redirect(url_for('containers.list'))

@containers.route('/<string:container_id>/delete', methods=['POST'])
def remove_container(container_id):
    # TODO: Add flash message throwing an error if the remove method fails
    try:
        cli.remove_container(container_id)
    except Error:
        print "Oops!"
    return redirect(url_for('containers.list'))


def containers_list(template, containers_list):
    search = request.args.get('q')
    containers_filtered = containers_list
    if search:
        containers_filtered = []
        for container in containers_list:
            if (search in container.name()
                or search in container.image()
                or search in container.id()):
                containers_filtered.append(container)
    return render_template('containers/list.html', containers=containers_filtered)
