apt-get update
apt-get -y upgrade

apt-get -y install build-essential
apt-get -y install python-dev
apt-get -y install python-imaging
apt-get -y install python-virtualenv
apt-get -y install libjpeg-dev
apt-get -y install libxslt1-dev
apt-get -y install libxml2-dev
apt-get -y install git-core
apt-get -y install vim

sudo -u vagrant bash <<EOF
    cd /home/vagrant
    if [ ! -d "/home/vagrant/plone" ]; then
		git clone https://github.com/kcleong/buildout plone
	fi
	cd plone
	git checkout diazo-training

    if [ ! -f "plone-4.2.1-eggs.tgz" ]; then
		wget --quiet http://cobain.gw20e.com/leong/plone-4.2.1-eggs.tgz
		tar -zxf plone-4.2.1-eggs.tgz
	fi
	
	if [ ! -f "training-zodb.tgz" ]; then
		wget --quiet http://cobain.gw20e.com/leong/training-zodb.tgz
		tar -zxf training-zodb.tgz
		rm -r var/filestorage var/blobstorage 
		mv filestorage var && mv blobstorage var
	fi

	if [ ! -f "./bin/python" ]; then
		virtualenv .
	fi
	 
	./bin/python bootstrap.py
	./bin/buildout

	cd /home/vagrant
	if [ -d "/home/vagrant/django" ]; then
		git clone git://github.com/Goldmund-Wyldebeast-Wunderliebe/diazo-training-django.git django
	fi
EOF
exit 0
