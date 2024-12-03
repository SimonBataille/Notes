https://sandilands.info/sgordon/capturing-wifi-in-monitor-mode-with-iw

sudo tcpdump -n -i wlp3s0 host 192.168.8.102
tls.handshake.type == 11

http://hilsz.com/wp/parfaire-installation-tiny-core/ => CONF TINYcORE

# IW

## Getting started with iw
iw dev
iw phy phy0 info

## Capturing in monitor mode
sudo iw phy phy0 interface add mon0 type monitor
iwconfig wlp3s0 : GET FREQUENCY 2.452 GHz
sudo iw dev wlan0 del
sudo ifconfig mon0 up
sudo iw dev mon0 set freq 2437
iwconfig mon0
sudo tcpdump -i mon0 -n -w wireless.cap

## Returning to Managed Mode
sudo iw dev mon0 del
sudo iw phy phy0 interface add wlan0 type managed
iw dev
iwconfig wlan0
