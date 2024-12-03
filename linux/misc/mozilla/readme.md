https://www.fossmint.com/backup-and-restore-a-firefox-profile-on-linux/

# Firefox Profile Backup

cd ~/.mozilla
tar -jcvf firefox-browser-profile.tar.bz2 .mozilla
mv firefox-browser-profile.tar.bz2 ~/Desktop


# Firefox Profile Restore

rm -rf ~/.mozilla
tar -xvf firefox-browser-profile.tar.bz2


# Encrypt Firefox Profile Backup

gpg -c firefox-browser-profile.tar.bz2 //encrypt symetrical
gpg firefox-browser-profile.tar.bz2.gpg //decrypt (simon20)

# Password

cd firepwd-master/
python3 firepwd.py -d ~/.mozilla/firefox/9ixe5yve.default-release-1614477526460/


