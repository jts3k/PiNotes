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

```echo "Starting Pd..."   
pd -nogui -rt /home/pi/PD/launch.pd &```

You can save a backup version of this by doing `sudo nano launchscript` then writing out a back-up copy of the launchscript.

Make the script into an executable via:

```sudo chmod 755 launchscript```

Test the executable from the command line: `sudo launchscript/launchscript`

Make the script run on startup by adding it to the bottom of the `etc/profile`:

(do `sudo nano /etc/profile` then add `sudo launchscript/launchscript` to bottom of file)

Test that the script runs on startup by rebooting the pi: `sudo reboot`

SIDEBAR: This was all done on a RPi3, but I then moved the SD card to a Pi zero to test and it boots into the PD patch just fine, plays sound through the bonnet, etc.

NOW TO GET PYTHON AND PWM HAPPENING
