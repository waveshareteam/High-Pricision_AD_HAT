/*****************************************************************************
* | File      	:   Readme_CN.txt
* | Author      :   Waveshare team
* | Function    :   Help with use
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2021-03-22
* | Info        :   Here is an English version of the documentation for your quick use.
******************************************************************************/
This file is to help you use this routine.

1. Basic information:
This routine is based on the jetson nano development, the kernel version:
	Linux raspberrypi 5.4.51-v7l+ #1333 SMP Mon Aug 10 16:51:40 BST 2020 armv7l GNU/Linux
You can view the detailed test routine in the project's main.py

2. Pin connection:
Pin connections can be viewed in config.py, which is repeated here:
	EPD    =>    Jetson Nano/RPI(BCM)
	VCC    ->    Without direct connection, other devices can be directly connected to 3.3V
	GND    ->    GND
	DIN    ->    10(MOSI)
	DOUT   ->    9(MISO)
	SCLK   ->    11(SCLK)
	CS     ->    22
	DRDY   ->    17
	REST   ->    18
	AVDD   ->    5V or 2.5V
	AVSS   ->    GND or -2.5V

3.Installation library
    sudo apt-get update
    sudo apt-get install python-pip
    sudo apt-get install python-pil
    sudo apt-get install python-numpy
    sudo pip2 install Jetson.GPIO
	sudo pip2 install spidev

or

    sudo apt-get update
    sudo apt-get install python3-pip
    sudo apt-get install python3-pil
    sudo apt-get install python3-numpy
    sudo pip3 install Jetson.GPIO
	sudo pip3 install spidev

4.Open SPI：
In terminal input：
	sudo /opt/nvidia/jetson-io/jetson-io.py
The GPIO Tools menu will pop up, select "Configure 40-Pin Expansion Header" and press Enter to enter the secondary menu.
Then tick SPI1 and return to the higher menu, and finally select "Save and Reboot to Reconfigure Pins" to make the device reboot configuration take effect.

5. Basic use:
The factory hardware default COM has been connected to GND
The program has configured IN0 and IN1 two analog output
At this time you can draw IN0 or IN1 and GND to measure the target voltage
Input:
	sudo python main.py
or
	sudo python3 main.py

For more information, please visit the official Wiki of Waveshare:https://www.waveshare.net/wiki/High-Precision_AD_HAT   
