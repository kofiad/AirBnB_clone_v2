from fabric.api import env, run, put
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = '<username>'
env.key_filename = '<path to SSH key>'

def do_pack():
    # Your implementation of the do_pack function goes here

def do_deploy(archive_path):
    # Your implementation of the do_deploy function goes here

def deploy():
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
