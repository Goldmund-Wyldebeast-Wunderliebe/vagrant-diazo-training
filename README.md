vagrant-diazo-training
======================

Vagrant set-up including Django and Plone

... what is vagrant

Getting started
---------------

Download and install Vagrant:

    http://vagrantup.com/

Create a directory to store the vagrant virtual machines:

    mkdir ~/vm

Clone the 'Diazo training' vagranti using git:

    git clone git://github.com/Goldmund-Wyldebeast-Wunderliebe/vagrant-diazo-training.git


Vagrant development
-------------------

-- explain audience!

Fabric is used to install system and Python packages on the virtual machine.

    pip install -r requirements

Upgrade system:    

    fab vagrant upgrade

Install buildout tools and dependencies:

    fab vagrant install_base







    

