from fabric.api import env, local, run, cd
 
def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['127.0.0.1:2222']
 
    # use vagrant ssh key
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]
 
def uname():
    run('uname -a')

def install_base():
    run('sudo apt-get -y install build-essential')
    run('sudo apt-get -y install python-dev')
    run('sudo apt-get -y install libjpeg-dev')
    run('sudo apt-get -y install git-core')
    run('sudo apt-get -y install libxslt-dev')

def install_plone():
    run('git clone git://github.com/Goldmund-Wyldebeast-Wunderliebe/gw20e.buildout.git plone')
    with cd('$HOME/plone'):
        with cd('$HOME/plone'):
            run('virtualenv .')
            run('./bin/python bootstrap.py -c buildout-dvl.cfg')
        run('./bin/buildout -c buildout-dvl.cfg')

