#!/bin/bash

wget https://github.com/fg2it/grafana-on-raspberry/releases/download/v5.1.4/grafana_5.1.4_armhf.deb
 
sudo dpkg -i grafana_5.1.4_armhf.deb
 
sudo systemctl enable grafana-server 

sudo systemctl start grafana-server

rm grafana_5.1.4_armhf.deb
 
