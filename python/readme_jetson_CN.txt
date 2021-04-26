/*****************************************************************************
* | File      	:   Readme_CN.txt
* | Author      :   Waveshare team
* | Function    :   Help with use
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2021-03-22
* | Info        :   在这里提供一个中文版本的使用文档，以便你的快速使用
******************************************************************************/
这个文件是帮助您使用本例程。

1.基本信息：
本例程基于jetson nano开发的，内核版本
	Linux jetson-desktop 4.9.140-tegra #1 SMP PREEMPT Tue Oct 27 21:02:37 PDT 2020 aarch64 aarch64 aarch64 GNU/Linux
你可以在工程的main.py中查看详细的测试例程

2.管脚连接：
管脚连接你可以在config.py中查看，这里也再重述一次：
	EPD    =>    Jetson Nano/RPI(BCM)
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
    sudo pip2 install Jetson.GPIO
	sudo pip2 install spidev
或

    sudo apt-get update
    sudo apt-get install python3-pip
    sudo apt-get install python3-pil
    sudo apt-get install python3-numpy
    sudo pip3 install Jetson.GPIO
	sudo pip3 install spidev

4.打开SPI：
终端输入：
	sudo /opt/nvidia/jetson-io/jetson-io.py
会弹出GPIO工具菜单，选择“Configure 40-pin expansion header”按下回车进入次级菜单。
然后勾选spi1并返回上级菜单，最后选择“Save and reboot to reconfigure pins”使设备重启配置生效。

5.基本使用：
出厂硬件默认COM已经连接到GND，程序配置好了IN0和IN1两个模拟输出，此时你可以引出IN0或IN1与GND测量目标电压
输入：
	sudo python main.py
或
	sudo python3 main.py

更多资料请前往微雪电子官方Wiki查看：https://www.waveshare.net/wiki/High-Precision_AD_HAT
