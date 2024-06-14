#!/bin/bash 
cd /dev
echo 'mic-711on' | sudo -S chmod 777 ttyUSB0
timeout 20s cat ttyUSB0 > /home/mic-711on/Desktop/dataUpload/input.txt

cd /home/mic-711on/Desktop/dataUpload


python firebaseDataUpload.py
python mongoDBDataUpload.py
