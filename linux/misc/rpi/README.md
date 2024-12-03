### serial: noir jaune orange
echo enable_uart=1 : /boot/config.txt
stty -F /dev/ttyUSB0 115200 raw -echo -parenb
cat /dev/ttyUSB0
busybox microcom -s 115200 /dev/ttyUSB0


### FLASH
sudo dd bs=4M if=2020-12-02-raspios-buster-armhf-lite.img of=/dev/sdd conv=fsync status=progress


### SSH
nmap -sn 192.168.3.0/24

touch boot/ssh

ssh pi@10.42.0.134

host = rpi = server ssh

    ls -l /etc/hosts/
    ls -l /etc/hosts/ssh_host_ecdsa_key.pub
    ls -l /etc/ssh/sshd_config
    ssh-keygen -lf /etc/ssh/ssh_host_ecdsa_key.pub
    sudo ssh-keygen -y -f /etc/ssh/ssh_host_ecdsa_key
    

laptop = client ssh

    ls -l ~/.ssh/known_host
    ssh-keygen -F 10.42.0.134
    ssh-keygen -F 192.168.3.9
    sudo ssh-keyscan 192.168.3.9


    simon@simon-Aspire-V3-571G:~$ cat .ssh/known_hosts
        |1|J1AnP8SmJTVlHU/J+FBSkzpyhCg=|/Pykv14uNNpt0QcajQdCCSllRwo= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJOBxkc90DpeTvWU8bXqTudbX8mtronq1hxgyAZnWEb83/oXUqI3a3p+1UsEzBdWs/3SNCUZ4SRgA5Q5wOkBRGc=

    key=`echo J1AnP8SmJTVlHU/J+FBSkzpyhCg= | base64 -d | xxd -p`
    echo -n "192.168.3.9" | openssl sha1 -mac HMAC -macopt hexkey:$key|awk '{print $2}' | xxd -r -p|base64


pi@raspberrypi:~ $ ssh simon@simon-Aspire-V3-571G
The authenticity of host 'simon-aspire-v3-571g (127.0.1.1)' can't be established.
ECDSA key fingerprint is SHA256:mAVVy3csDLL6/eT0InN7JWAaCyRLZaQyrk0tJzRIsNQ.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'simon-aspire-v3-571g' (ECDSA) to the list of known hosts.
simon@simon-aspire-v3-571g's password:


LAPTOP: server ssh

dpkg -l | grep openssh-server
sudo apt-get install openssh-server
/etc/init.d/ssh status

pi@raspberrypi:~$ ssh simon@192.168.3.5
The authenticity of host '192.168.3.5 (192.168.3.5)' can't be established.
ECDSA key fingerprint is SHA256:vmvTx1bV3zMmsF6HOfbJfqA7tsIJExgz6q6GkAZI8gM.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.3.5' (ECDSA) to the list of known hosts.


trouble shoot ssh
nmap 192.168.3.5: opened port on server machine
nc -v -nn 192.168.3.5 22: wich service on port 22
cat /etc/ssh/sshd_config
sudo arp-scan 192.168.3.1/24


ssh protocol exchange key
simon@simon-Aspire-V3-571G:~$ cat /etc/ssh/ssh_host_ecdsa_key.pub
    ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHGo5NHU9cW2yl6k/lKw3exL1iMb03HkwKiy+zI3RfKIhh5R5QW1LqPKSXUUQacYQyc0TtI78oxoqmtbhgAYnPM= root@simon-Aspire-V3-571G

pi@raspberrypi:~ $ cat .ssh/known_hosts
    |1|2e6McTYhhk78rALiYPjSMjRcd7A=|cF+zUSKAVp+WfZJxhmqWRpYIBTw= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJOBxkc90DpeTvWU8bXqTudbX8mtronq1hxgyAZnWEb83/oXUqI3a3p+1UsEzBdWs/3SNCUZ4SRgA5Q5wOkBRGc=
    |1|t1ieJ8+DcF8k1eT6HTEk5xXfBXY=|5fQfOAEneer6iDuwBEVPwhTRyWs= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHGo5NHU9cW2yl6k/lKw3exL1iMb03HkwKiy+zI3RfKIhh5R5QW1LqPKSXUUQacYQyc0TtI78oxoqmtbhgAYnPM=

    key=`echo 2e6McTYhhk78rALiYPjSMjRcd7A= | base64 -d | xxd -p`
        echo -n "simon-aspire-v3-571g" | openssl sha1 -mac HMAC -macopt hexkey:$key|awk '{print $2}' | xxd -r -p|base64

    key=`echo t1ieJ8+DcF8k1eT6HTEk5xXfBXY= | base64 -d | xxd -p`
        echo -n "192.168.3.5" | openssl sha1 -mac HMAC -macopt hexkey:$key|awk '{print $2}' | xxd -r -p | base64



### wpa_supplicant
sudo iwlist wlan0 scan
cat /etc/wpa_supplicant/wpa_supplicant.conf
wpa_supplicant -d -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf

network={
    ssid="testing"
    psk="testingPassword"
}

wpa_cli -i wlan0 reconfigure



pkill wpa_supplicant
wpa_supplicant -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf

rfkill list
rfkill unblock wifi


wpa_passphrase votre-ssid votre-mot-de-passe >> /etc/wpa_supplicant/wpa_supplicant.conf
sudo wpa_passphrase HUAWEI-42QXX9 88403B459283 >> /etc/wpa_supplicant/wpa_supplicant.conf

dhcpd -w -q
cat /etc/resolv.conf : 192.168.3.1, DNS

iwconfig
ip a


List_of_ISO_3166_country_codes


### static ip
ip route | grep wlan0


### CUPS
sudo apt-get install cups

   43  sudo usermod -aG lpadmin pi
   44  groups 
   45  groups lp 
   46  group pi
   47  groups pi
   48  sudo /etc/init.d/cups start

sudo cupsctl --remote-any
sudo /etc/init.d/cups restart

http://192.168.3.9:631/admin


### SCANNER
#### 2021 09 11
https://perhonen.fr/blog/2012/09/partager-un-scanner-via-sane-544


scanimage accesses image acquisition devices through the SANE (Scanner Access Now Easy) interface and can thus support any device for which there exists a SANE backend (try apropos sane- to get a list of available backends).

rpi:
sudo sane-find-scanner
sudo scanimage -L
apropos sane-
sudo scanimage >image.pnm

sudo nano /etc/default/saned
sudo nano /etc/sane.d/saned.conf
ls -l /dev/bus/usb/001
sudo adduser saned lp
sudo service saned restart
sudo systemctl start saned.socket
sudo systemctl enable saned.socket
    Created symlink /etc/systemd/system/sockets.target.wants/saned.socket → /lib/systemd/system/saned.socket.
sudo systemctl status saned.socket
sudo adduser $USER saned
sudo -s
su -s /bin/bash saned
scanimage -L


cat /etc/services|grep san
sudo apt-get install xinetd 
sudo nano  /etc/xinetd.d/sane-port
sudo nano /etc/udev/rules.d/40-scanner-permissions.rules
sudo /etc/init.d/udev restart
sudo /etc/init.d/xinetd restart
netstat -lnt: port 6566 sane

sur laptop : sudo nano /etc/sane.d/net.conf
>## saned hosts
>192.168.3.9

xsane net:192.168.3.9:pixma

/sbin/ldconfig -p | grep sane : libsane is installed


:(
cat /etc/sane.d/dll.conf
cat /etc/sane.d/net.conf


convert image laptop:
scp -p pi@raspberrypi.local:~/image.pnm /home/simon/Desktop/
display image.pnm
pnmtopng image.pnm > image.png
sudo nano /etc/ImageMagick-6/policy.xml
gs --version
convert image.pnm image.pdf
xreader image.pdf


### SANE
cat /etc/passwd : list users 
cat /etc/group : list groups
/sbin/ldconfig -p | grep sane : libsane is installed


sudo -s : run shell with root
su root
> Password: root
su -s /bin/bash saned


id -Gn : current group i belong to

scanimage -A : all scanimage option
scanimage --format=png --output-file test.png --progress
scanimage -d "net:192.168.3.9:pixma" --format=png --output-file test.png --progress

conf file :
> cat /etc/sane.d/pixma.conf
> ll /lib/udev/rules.d/60-libsane.rules
> cat /etc/sane.d/dll.conf : list dynamic driver from /usr/lib/x86_64-linux-gnu/sane/libsane-pixma.so.1
> cat /etc/default/saned
> cat /etc/sane.d/saned.conf 

https://doc.ubuntu-fr.org/scanner_usb_non_reconnu
https://wiki.debian.org/fr/SaneOverNetwork
https://doc.ubuntu-fr.org/tutoriel/utiliser_un_scanner_en_reseau#configuration_simple

MAC os X
dscl . list /groups : list all groups
dscacheutil -q group -a name admin : list members of admin 



### avahi
sudo cp /usr/share/doc/avahi-deamon/examples/ssh.service /etc/avahi/services/
ping raspberrypi.local
avahi-browse --all --ignore-local --resolve --terminate
avahi-resolve -4a 192.168.3.5
avahi-resolve -4n simon-Aspire-V3-571G.local




### certidicat: Roberto Pozzi
cat /etc/ca-certificates.conf: on LAPTOP
/etc/ssl/certs/IdenTrust_Public_Sector_Root_CA_1.pem: on raspberry pi

LAPTOP: sudo nano /etc/hosts
192.168..3.9   simonbataille.com

sudo mkdir -p /etc/ssl/mycerts
sudo openssl req -new -x509 -days 365 -nodes -out /etc/ssl/mycerts/apache.pem -keyout /etc/ssl/mycerts/apache.key
sudo openssl x509 -noout -text -in /etc/ssl/mycerts/apache.pem

sudo a2enmod ssl
sudo vi /etc/apache2/sites-available/default-ssl.conf
sudo a2ensite default-ssl
sudo service apache2 reload


# 10.42.0.x
for i in `seq 2 255` ; do ping -w 1 -c 1 10.42.0.$i ; done



hostname -I
sudo apt install nmap
nmap -sn 10.42.0.0/24

ip a

ssh pi@10.42.0.134


```
As shown by the ip commands the wired connection with interface enp7s0 is using subnet 10.42.0.0/24 and the Laptop has ip address 10.42.0.1/24 on the wired port to the RasPi. If there is a DHCP-server available on the Laptop then the RasPi will have an ip address in the range 10.42.0.2 to 10.42.0.254. To find its ip address you should execute:

laptop ~$ nmap -sn 10.42.0.0/24

This will ping test the subnet and it always show you its own ip address 10.42.0.1 and it should in addition find the RasPis ip address if it has got an ip address from the Laptop. If not (no DHCP server available) then you should give the RasPi a static ip address or ensure that link local addressing is working on the Laptop. The link local address subnet is already available as shown by **ip route**:

169.254.0.0/16 dev wlp6s0 scope link metric 1000
```


simon@simon-Aspire-V3-571G:~$ ps -aux | grep dhc
root         195  0.0  0.0      0     0 ?        I<   05:56   0:00 [sdhci]
nobody      3197  0.0  0.0  14784  3976 ?        S    07:23   0:00 /usr/sbin/dnsmasq --conf-file=/dev/null --no-hosts --keep-in-foreground --bind-interfaces --except-interface=lo --clear-on-reload --strict-order --listen-address=10.42.0.1 --dhcp-range=10.42.0.10,10.42.0.254,60m --dhcp-lease-max=50 --dhcp-leasefile=/var/lib/NetworkManager/dnsmasq-enp2s0f0.leases --pid-file=/run/nm-dnsmasq-enp2s0f0.pid --conf-dir=/etc/NetworkManager/dnsmasq-shared.d


### network manager and 10.42.0.1

nmcli default 10.42.0.1

Hi,

The value can be changed using the 'IPv4 address' property, but
unfortunately nm-applet doesn't support it. However you can use nmcli:

 $ nmcli connection modify Hotspot ipv4.address 172.25.16.1/24

as you did, and then re-activate the connection to apply the change:

 $ nmcli connection up Hotspot



### OPENVPN
gunzip -c /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz > /etc/openvpn/server.conf
