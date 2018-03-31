## Disk Image [here](https://drive.google.com/file/d/1zVlfoxGsFtwZIYpvnRLcRFOTBBEWlb-O/view?usp=sharing)

___

### Setup notes

Installed Raspbian Stretch Full, copied to SD card via `Pi Filler` app

Open terminal and do some configuring via `sudo raspi-config`

Changed password to `3.14ispi`
Enabled SSH and I2C
Expand file system
Make to boot into desktop with auto-login

Updated pi via `sudo apt update && sudo apt upgrade -y`

Installed I2S adafruit sound driver stuff via `curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash`

Install Pure Data via `sudo apt-get update` then `$ sudo apt-get install puredata`

Test PD by SSH'ing a PD patch from a computer to the pi, i.e. `scp /Users/stilesj/Desktop/launch.pd pi@192.168.1.240:PD` then launch it on the pi via `sudo pd -nogui launch.pd`

Create a script to run on startup.  Make a directory for the script, i.e. `sudo mkdir launchscript` then create a textfile `sudo nano launchscript`.  In the file enter:

```
echo "Starting Pd..."
pd -nogui -rt /home/pi/PD/launch.pd &
```

You can save a backup version of this by doing `sudo nano launchscript` then writing out a back-up copy of the launchscript.

Make the script into an executable via:

`sudo chmod 755 launchscript`

Test the executable from the command line: `sudo launchscript/launchscript`

Make the script run on startup by adding it to the bottom of the `etc/profile`:

(do `sudo nano /etc/profile` then add `sudo launchscript/launchscript` to bottom of file)

Test that the script runs on startup by rebooting the pi: `sudo reboot`

SIDEBAR: This was all done on a RPi3, but I then moved the SD card to a Pi zero to test and it boots into the PD patch just fine, plays sound through the bonnet, etc.

NOW TO GET PYTHON AND OSC AND PWM HAPPENING

Installing Python PWM library:
```
sudo apt update && sudo apt upgrade -y
sudo pip install python-osc
sudo pip install adafruit-pca9685
```

Copy Python script for [simple LED chase display](https://github.com/jts3k/PiNotes/blob/master/Python/LED-chase.py) to Pi and test

copy: `scp /Users/stilesj/Documents/GitHub/PiNotes/Python/LED-chase.py pi@192.168.1.194:Python`
test: `python Python/LED-chase.py`

Add python script to startup script, the source now reads:

```
echo "Starting Pd..."
pd -nogui -rt /home/pi/PD/launch.pd &
python Python/LED-chase.py &
```

Hmm python-osc example script is giving errors and also more people seem to be using pyOSC on RPi so I'm gonna try pyOSC, installing via `sudo pip install pyOSC`

Looks like we need some third-party PD objects, I found compiling them on the Pi to be painful so I got the objects by running PD on the Pi and doing 'Help/Find externals' then I got iemnet and OSC.  These I downloaded to PD/lib and then I had to add the new folders inside lib to PD's path preferences.  Oh boy.

Made the Pi auto connect to various networks by adding network info:

`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

```
network={
        ssid="MOMNET"
        psk="3.14ispi"
        key_mgmt=WPA-PSK
}

network={
        ssid="MediaLabLighting"
        psk="the media lab"
        key_mgmt=WPA-PSK
}
```

Installing software for screensharing:

```sudo apt-get install tightvncserver```
