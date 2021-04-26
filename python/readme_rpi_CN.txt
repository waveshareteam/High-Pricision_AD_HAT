/*****************************************************************************
* | File      	:   Readme_CN.txt
* | Author      :   Waveshare team
* | Function    :   Help with use
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2020-12-15
* | Info        :   在这里提供一个中文版本的使用文档，以便你的快速使用
******************************************************************************/
这个文件是帮助您使用本例程。

1.基本信息：
本例程基于树莓派4B+开发的，内核版本
	Linux raspberrypi 5.4.51-v7l+ #1333 SMP Mon Aug 10 16:51:40 BST 2020 armv7l GNU/Linux
你可以在工程的main.py中查看详细的测试例程

2.管脚连接：
管脚连接你可以在config.py中查看，这里也再重述一次：
SPI:
	AD HAT =>    RPI(BCM)
	VCC    ->    没有直接连接，使用的5V转成3.3V，其他设备使用可以直接接3.3V
	GND    ->    GND
	DIN    ->    10(MOSI)
	DOUT   ->    9(MISO)
	SCLK   ->    11(SCLK)
	CS     ->    22
	DRDY   ->    17
	REST   ->    18
	AVDD   ->    5V或2.5V
	AVSS   ->    GND或-2.5V
	
3.安装库：
    sudo apt-get update
    sudo apt-get install python-pip
    sudo apt-get install python-pil
    sudo apt-get install python-numpy
    sudo pip install RPi.GPIO

或

    sudo apt-get update
    sudo apt-get install python3-pip
    sudo apt-get install python3-pil
    sudo apt-get install python3-numpy
    sudo pip3 install RPi.GPIO

4.基本使用：
出厂硬件默认COM已经连接到GND，程序配置好了IN0和IN1两个模拟输出，此时你可以引出IN0或IN1与GND测量目标电压
输入：
	sudo python main.py
或
	sudo python3 main.py

更多资料请前往微雪电子官方Wiki查看：https://www.waveshare.net/wiki/High-Precision_AD_HAT