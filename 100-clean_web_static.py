from fabric.api import env, run, local
from datetime import datetime
import os

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = '<username>'
env.key_filename = '<path to SSH key>'

def do_clean(number=0):
    number = int(number)
    if number < 0:
        return
    if number == 0 or number == 1:
        number = 1
    else:
        number += 1

    local("ls -1t versions/ | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number))
    run("ls -1t /data/web_static/releases/ | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number))
