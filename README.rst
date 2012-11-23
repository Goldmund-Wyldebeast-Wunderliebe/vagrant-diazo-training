Vagrant Diazo training
======================

Vagrant set-up including Django and Plone

... what is vagrant

Getting started
---------------

1. Setup vagrant project structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a directory to store the vagrant virtual machines:

    mkdir ~/vm

Create a data directory, this directory is shared to the guest vm:

    mkdir -p ~/vm/data

Clone the 'Diazo training' vagranti using git:

    cd ~/vm
    git clone git://github.com/Goldmund-Wyldebeast-Wunderliebe/vagrant-diazo-training.git

Create a virtual environment to hold fabric:

    virtualenv venv && source venv/bin/activate

Fabric is used to install system and Python packages on the virtual machine.

    pip install -r requirements.txt


2. Install and set-up Vagrant
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download and install Vagrant:

    http://vagrantup.com/

Upgrade system:    

    fab vagrant upgrade

Install buildout tools and dependencies:

    fab vagrant install_base







    

