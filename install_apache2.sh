#!/bin/bash

sudo apt install apache2 php7.0 libapache2-mod-php7.0 -y
sudo a2enmod userdir
sudo a2enmod php7.0
sudo sed -i 's/php_admin_flag engine Off/php_admin_flag engine On/g' /etc/apache2/mods-enabled/php7.0.conf
sudo service apache2 restart
