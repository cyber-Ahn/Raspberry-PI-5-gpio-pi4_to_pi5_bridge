#!/bin/bash
echo -e "\n\e[33m>> \e[31mEnter Your Python Version '3.11'?\e[32m"
read ver
sudo mv /home/pi/gpio_pi4_to_pi5_bridge/TGNgpio.py /usr/local/lib/python"$ver"/dist-packages/
echo -e "\n\e[33m>> \e[31minstallation successful\e[32m"
sleep 3