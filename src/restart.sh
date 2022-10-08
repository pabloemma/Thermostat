#!/bin/bash
 


if [ $(ps -efa | grep -v grep | grep Tmeasure.py -c) -gt 0 ] ;
then
    echo "Process running ...";
else
#temporary if program dies download all the necessary programs
#cd /home/pi/git/speedtest/src
#./update_speedtest
#cd ~

python3 -u /home/pi/git/Thermostat/src/Tmeasure.py  &


echo "Starting the process Tmeasure";
fi;
if [ $(ps -efa | grep -v grep | grep ReadValue.py -c) -gt 0 ] ;
then
    echo "Process running ...";
else
#temporary if program dies download all the necessary programs
#cd /home/pi/git/speedtest/src
#./update_speedtest
#cd ~

python3 -u /home/pi/git/Thermostat/src/ReadValue.py  &


echo "Starting the process ReadValue";
fi;
