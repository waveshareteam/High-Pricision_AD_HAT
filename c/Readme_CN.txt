/*****************************************************************************
* | File      	:   Readme_CN.txt
* | Author      :   Waveshare team
* | Function    :   Help with use
* | Info        :
*----------------
* |	This version:   V1.1
* | Date        :   2020-12-15
* | Info        :   在这里提供一个中文版本的使用文档，以便你的快速使用
******************************************************************************/
这个文件是帮助您使用本例程。

1.基本信息：
本例程基于树莓派4B+和jetson nano开发的，内核版本
	Linux raspberrypi 5.4.51-v7l+ #1333 SMP Mon Aug 10 16:51:40 BST 2020 armv7l GNU/Linux
		&
	Linux jetson-desktop 4.9.140-tegra #1 SMP PREEMPT Tue Oct 27 21:02:37 PDT 2020 aarch64 aarch64 aarch64 GNU/Linux
你可以在工程的 examples/main.c 中查看详细的测试例程

2.管脚连接：
管脚连接你可以在 lib/Config/DEV_Config.c(h) 中查看，这里也再重述一次：
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
安装BCM2835：
	wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.68.tar.gz
	tar zxvf bcm2835-1.68.tar.gz 
	cd bcm2835-1.68/
	sudo ./configure && sudo make && sudo make check && sudo make install

4.基本使用：
出厂硬件默认COM已经连接到GND，程序配置好了IN0和IN1两个模拟输出，此时你可以引出IN0或IN1与GND测量目标电压

RPI：
	sudo make clean
	sudo make
	sudo ./main

jetson nano:
	sudo make clean
	sudo make JETSON
	sudo ./main
	
更多资料请前往微雪电子官方Wiki查看：https://www.waveshare.net/wiki/High-Precision_AD_HAT