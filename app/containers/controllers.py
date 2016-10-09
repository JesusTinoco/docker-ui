from flask import Blueprint, flash, request, render_template, redirect, url_for
from .. import cli
from .. import tcp_url
from models import Container, ContainerInspect

containers = Blueprint('containers', __name__, url_prefix='/containers')

print('rwetdfasdfasdfss')

@containers.route('/list/', methods=['GET'])
def list():
    print "================================="
    print tcp_url
    print "================================="
    containers = [Container(container) for container in cli.containers(all=True)]
    return containers_list('containers/list.html', containers)

@containers.route('/<string:container_id>', methods=['GET'])
def container_info(container_id):
    container = ContainerInspect(cli.inspect_container(container_id))
    processes = []
    print container.links()
    try:
        processes = cli.top(container_id)
    except Exception as err:
        print err
    return render_template('containers/info.html', container = container, processes=processes)

@containers.route('/<string:container_id>/start', methods=['POST'])
def start_container(container_id):
    try:
        cli.start(container_id)
        flash('Container "%s" has been started successfully.' % container_id, 'success')
    except Exception as err:
        print err
        flash(str(err), 'warning')
    return redirect(url_for('containers.list'))

@containers.route('/<string:container_id>/restart', methods=['POST'])
def restart_container(container_id):
    try:
        cli.restart(container_id)
        flash('Container "%s" has been restarted successfully.' % container_id, 'success')
    except Exception as err:
        print err
        flash(str(err), 'warning')
    return redirect(url_for('containers.list'))

@containers.route('/<string:container_id>/stop', methods=['POST'])
def stop_container(container_id):
    try:
        cli.stop(container_id)
        flash('Container "%s" has been stopped successfully.' % container_id, 'success')
    except Exception as err:
        print err
        flash(str(err), 'warning')
    return redirect(url_for('containers.list'))

@containers.route('/<string:container_id>/delete', methods=['POST'])
def remove_container(container_id):
    try:
        cli.remove_container(container_id)
        flash('Container "%s" has been deleted successfully.' % container_id, 'success')
    except Exception as err:
        print err
        flash(str(err), 'warning')
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
    return render_template(template, containers=containers_filtered, container_active="active")
