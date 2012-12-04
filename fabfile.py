""" Vagrant set-up for Diazo traning """

from fabric.api import env, local, run, cd
from utils import list_dir

plone_installer_url = 'https://launchpad.net/plone/4.2/4.2.1/+download/Plone-4.2.1-UnifiedInstaller.tgz'
gw20e_buildout = 'git://github.com/Goldmund-Wyldebeast-Wunderliebe/gw20e.buildout'
diazo_plone = 'git://github.com/Goldmund-Wyldebeast-Wunderliebe/diazo-training-plone.git'


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
        run('wget {0}'.format(plone_installer_url))
        run('tar -zxf Plone-4.2.1-UnifiedInstaller.tgz')
        run('rm Plone-4.2.1-UnifiedInstaller.tgz')
        run('mv Plone-4.2.1-UnifiedInstaller {0}'.format(plone_dir))

    with cd(plone_dir):
        run('./install.sh standalone')


def install_plone_gw20e():
    
    plone_dir = 'plone'
    if plone_dir not in list_dir():
        run('git clone {0}'.format(gw20e_buildout))

    with cd(plone_dir):
        # First get prerequisites
        run('git clone {0} diazo'.format(diazo_plone))
        run('wget http://cobain.gw20e.com/leong/local-diazo.cfg -O local.cfg')
        run('wget http://cobain.gw20e.com/leong/gw20e.buildout-eggs.tgz')
        run('tar -zxf gw20e.buildout-eggs.tgz && rm gw20e.buildout-eggs.tgz')
        # Set-up buildout
        run('virtualenv .')
        run('./bin/python bootstrap.py -c local.cfg')
        run('./bin/buildout -c diazo/local.cfg')
        run('./bin/instance run diazo/structure.py')
        run('./bin/instance start')
