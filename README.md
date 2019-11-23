# RASPBERRY_PI_SMS_EXCHANGE
## Features
- Receive and update SMS content on web page.
- Send SMS to Phone number via web.
- Management all received SMS.

Link demo: https://youtu.be/GVYldJEaf5g

## Hardware
- Raspberry Pi (Wifi/LAN support).
- Module SIM 900.

## Setup

### Raspberry Pi connect to wifi
```
sudo iwlist wlan0 scan
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

network={
    ssid="testing"
    psk="testingPassword"
}
```
Reference: https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

### Connect SIM900 Module with UART
Reference:
- https://programmingadvent.blogspot.com/2012/12/raspberry-pi-uart-with-pyserial.html
- https://hallard.me/enable-serial-port-on-raspberry-pi/
- https://github.com/InitialState/rpi-gps/wiki/2-Part-1.-Raspberry-Pi-Setup
- https://table-info.blogspot.com/2013/06/gsm-shield-icomsat.html

### Setup HTTP Server on Raspberry Pi
```
sudo apt-get install git-core
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install apache2 php5
sudo apt-get install lighttpd php5
sudo apt-get install git-core
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
```
#### Fix error:
- PHP 403 Forbidden - http://stackoverflow.com/questions/11537888/lighttpd-403-forbidden-for-php-files
