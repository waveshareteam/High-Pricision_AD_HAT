/*****************************************************************************
* | File      	:   Readme_CN.txt
* | Author      :   Waveshare team
* | Function    :   Help with use
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2020-12-15
* | Info        :   Here is an English version of the documentation for your quick use.
******************************************************************************/
This file is to help you use this routine.

1. Basic information:
This routine is based on the raspberry PI 4B+ development, the kernel version:
	Linux raspberrypi 5.4.51-v7l+ #1333 SMP Mon Aug 10 16:51:40 BST 2020 armv7l GNU/Linux
You can view the detailed test routine in the project's main.py

2. Pin connection:
Pin connections can be viewed in lib/Config/DEV_Config.c(h), which is repeated here:
SPI:
	AD HAT =>    RPI(BCM)
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

3. Basic use:
The factory hardware default COM has been connected to GND
The program has configured IN0 and IN1 two analog output
At this time you can draw IN0 or IN1 and GND to measure the target voltage
Input:
	sudo make clean
	sudo make
	sudo ./main