from flask import Flask, render_template
import docker
import platform
import sys

app = Flask(__name__)

app.config.from_object('config')

cli = docker.Client(base_url='unix://var/run/docker.sock')
system = platform.system()
tcp_url = ''

for parameter in sys.argv:
    print(parameter)
    if "host" in parameter:
        tcp_url = parameter.split('=')[1]

if system == 'Darwin' or system == 'Windows':
    cli = docker.from_env(assert_hostname=False)

if tcp_url != '':
    cli = docker.Client(base_url=tcp_url)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.containers.controllers import containers as containers_module
from app.images.controllers import images as images_module
from app.volumes.controllers import volumes as volumes_module
from app.networks.controllers import networks as networks_module

app.register_blueprint(containers_module)
app.register_blueprint(images_module)
app.register_blueprint(volumes_module)
app.register_blueprint(networks_module)