from flask import Blueprint, flash, request, render_template, redirect, url_for
from docker import Client
from models import Network

cli = Client(base_url='unix://var/run/docker.sock')

networks = Blueprint('networks', __name__, url_prefix='/networks')

@networks.route('/list', methods=['GET'])
def list():
    networks_aux = cli.networks()
    networks = [] if networks_aux is None else [Network(network) for network in networks_aux]
    return networks_list('networks/list.html', networks)

def networks_list(template, network_list):
    search = request.args.get('q')
    networks_filtered = network_list
    if search:
        networks_filtered = []
        for network in network_list:
            if search in network.name():
                networks_filtered.append(network)
    return render_template(template, networks=networks_filtered)
