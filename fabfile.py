from fabric.api import env, local, run, cd
 
def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['127.0.0.1:2222']
 
    # use vagrant ssh key
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]
 
def all():
    upgrade()
    install_base()
    install_plone()

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
    #run('mkdir -p $HOME/.buildout/eggs')
    #run('mkdir -p $HOME/.buildout/download')
    #run('mkdir -p $HOME/.buildout/extends')
    #run('cat > $HOME/.buildout/default.cfg')
    
    run('git clone git://github.com/Goldmund-Wyldebeast-Wunderliebe/gw20e.buildout.git plone')
    with cd('$HOME/plone'):
        run('virtualenv .')
        run('./bin/python bootstrap.py -c buildout-dvl.cfg')
        run('./bin/buildout -c buildout-dvl.cfg')

