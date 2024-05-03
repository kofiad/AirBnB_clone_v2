from fabric.api import env, put, run
import os

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = '<username>'
env.key_filename = '<path to SSH key>'

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Get the filename without extension
        filename = os.path.basename(archive_path)
        filename_no_ext = os.path.splitext(filename)[0]

        # Uncompress the archive to /data/web_static/releases/<archive filename without extension> on the web server
        run('mkdir -p /data/web_static/releases/{}'.format(filename_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(filename, filename_no_ext))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename))

        # Delete the symbolic link /data/web_static/current from the web server
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current on the web server
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(filename_no_ext))

        return True
    except:
        return False
