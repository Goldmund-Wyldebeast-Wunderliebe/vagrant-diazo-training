""" Vagrant set-up for Diazo traning """

from fabric.api import env, local, run, cd
from utils import list_dir


def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['127.0.0.1:2222']
 
    # use vagrant ssh key
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]


def init():
    upgrade()
    install_base()
    install_plone_gw20e()


def upgrade():
    run('sudo apt-get update')
    run('sudo apt-get -y upgrade')


def install_base():
    run('sudo apt-get -y install build-essential')
    run('sudo apt-get -y install python-dev')
    run('sudo apt-get -y install python-virtualenv')
    run('sudo apt-get -y install libjpeg-dev')
    run('sudo apt-get -y install libxslt1-dev')
    run('sudo apt-get -y install libxml2-dev')
    run('sudo apt-get -y install git-core')


def install_plone():

    plone_dir = 'plone-4.2.1'
    if plone_dir not in list_dir():
        run('wget https://launchpad.net/plone/4.2/4.2.1/+download/Plone-4.2.1-UnifiedInstaller.tgz')
        run('tar -zxvf Plone-4.2.1-UnifiedInstaller.tgz')
        run('rm Plone-4.2.1-UnifiedInstaller.tgz')
        run('mv Plone-4.2.1-UnifiedInstaller {0}'.format(plone_dir))

    with cd(plone_dir):
        run('./install.sh standalone')


def install_plone_gw20e():
    
    plone_dir = 'gw20e.buildout'
    if plone_dir not in list_dir():
        run('git clone git://github.com/Goldmund-Wyldebeast-Wunderliebe/gw20e.buildout')

    with cd(plone_dir):
        run('wget http://cobain.gw20e.com/leong/gw20e.buildout-eggs.tgz')
        run('tar -zxvf gw20e.buildout-eggs.tgz')
        run('virtualenv .')
        run('./bin/python bootstrap.py -c buildout-dvl.cfg')
        run('./bin/buildout -c buildout-dvl.cfg')
