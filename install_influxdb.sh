#!/bin/bash

curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
 
sudo apt update
sudo apt install influxdb  
sudo systemctl enable influxdb
sudo systemctl start influxdb 

sleep 20s

echo "CREATE DATABASE contapersone" | influx
 
