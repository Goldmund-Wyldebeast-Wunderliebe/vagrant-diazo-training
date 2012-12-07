""" Vagrant set-up for Diazo traning """

from fabric.api import env, local, run, cd
from utils import list_dir, add_cronjob

plone_buildout = 'https://github.com/kcleong/buildout'
diazo_plone = 'git://github.com/Goldmund-Wyldebeast-Wunderliebe/diazo-training-plone.git'
diazo_django = 'git://github.com/Goldmund-Wyldebeast-Wunderliebe/diazo-training-django.git'


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
    run('sudo apt-get -y install python-imaging')
    run('sudo apt-get -y install python-virtualenv')
    run('sudo apt-get -y install libjpeg-dev')
    run('sudo apt-get -y install libxslt1-dev')
    run('sudo apt-get -y install libxml2-dev')
    run('sudo apt-get -y install git-core')
    run('sudo apt-get -y install vim')


def install_plone():
    
    plone_dir = 'plone'

    if plone_dir not in list_dir():
        run('git clone {0} {1}'.format(plone_buildout, plone_dir))

    with cd(plone_dir):
        run('git checkout diazo-training')

        # Get prerequisites
        run('wget http://cobain.gw20e.com/leong/gw20e.buildout-eggs.tgz')
        run('tar -zxf gw20e.buildout-eggs.tgz')

        run('wget http://cobain.gw20e.com/leong/training-zodb.tgz')
        run('tar -zxf training-zodb.tgz')
        run('mv filestorage var && mv blobstorage var')

        # Set-up buildout
        run('virtualenv .')
        run('./bin/python bootstrap.py')
        run('./bin/buildout')
        run('./bin/instance start')
        add_cronjob('@reboot ~/plone/bin/instance start')

def cron():
    import pdb; pdb.set_trace()

def install_django():
    django_dir = 'django'

    if django_dir not in list_dir():
        run('git clone {0} {1}'.format(django_buildout, django_dir))

