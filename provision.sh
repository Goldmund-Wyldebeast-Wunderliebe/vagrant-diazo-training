sudo apt-get update
sudo apt-get -y upgrade

sudo apt-get -y install build-essential
sudo apt-get -y install python-dev
sudo apt-get -y install python-imaging
sudo apt-get -y install python-virtualenv
sudo apt-get -y install libjpeg-dev
sudo apt-get -y install libxslt1-dev
sudo apt-get -y install libxml2-dev
sudo apt-get -y install git-core
sudo apt-get -y install vim

su - vagrant 
git clone https://github.com/kcleong/buildout plone
cd plone
git checkout diazo-training

wget http://cobain.gw20e.com/leong/gw20e.buildout-eggs.tgz
tar -zxf gw20e.buildout-eggs.tgz

wget http://cobain.gw20e.com/leong/training-zodb.tgz
tar -zxf training-zodb.tgz
mv filestorage var && mv blobstorage var

virtualenv . 
git checkout diazo-training

#wget http://cobain.gw20e.com/leong/gw20e.buildout-eggs.tgz
#tar -zxf gw20e.buildout-eggs.tgz

wget http://cobain.gw20e.com/leong/training-zodb.tgz
tar -zxf training-zodb.tgz
mv filestorage var && mv blobstorage var

virtualenv . 
./bin/python bootstrap.py
./bin/buildout

cd ~/
git clone git://github.com/Goldmund-Wyldebeast-Wunderliebe/diazo-training-django.git django
