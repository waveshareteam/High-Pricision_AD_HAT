# /*****************************************************************************
# * | File        :   ADS1263.py
# * | Author      :   Waveshare team
# * | Function    :   ADS1263 driver
# * | Info        :
# *----------------
# * | This version:   V1.0
# * | Date        :   2020-12-15
# * | Info        :   
# ******************************************************************************/
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import config
import RPi.GPIO as GPIO

# gain
ADS1263_GAIN = {
    'ADS1263_GAIN_1' : 0,   # GAIN   1
    'ADS1263_GAIN_2' : 1,   # GAIN   2
    'ADS1263_GAIN_4' : 2,   # GAIN   4
    'ADS1263_GAIN_8' : 3,   # GAIN   8
    'ADS1263_GAIN_16' : 4,  # GAIN  16
    'ADS1263_GAIN_32' : 5,  # GAIN  32
    'ADS1263_GAIN_64' : 6,  # GAIN  64
}
# ADC2 gain
ADS1263_ADC2_GAIN = {
    'ADS1263_ADC2_GAIN_1'   : 0,    # GAIN  1
    'ADS1263_ADC2_GAIN_2'   : 1,    # GAIN  2
    'ADS1263_ADC2_GAIN_4'   : 2,    # GAIN  4
    'ADS1263_ADC2_GAIN_8'   : 3,    # GAIN  8
    'ADS1263_ADC2_GAIN_16'  : 4,    # GAIN  16
    'ADS1263_ADC2_GAIN_32'  : 5,    # GAIN  32
    'ADS1263_ADC2_GAIN_64'  : 6,    # GAIN  64
    'ADS1263_ADC2_GAIN_128' : 7,    # GAIN  128
}
# data rate
ADS1263_DRATE = {
    'ADS1263_38400SPS'  : 0xF, 
    'ADS1263_19200SPS'  : 0xE,
    'ADS1263_14400SPS'  : 0xD,
    'ADS1263_7200SPS'   : 0xC,
    'ADS1263_4800SPS'   : 0xB,
    'ADS1263_2400SPS'   : 0xA,
    'ADS1263_1200SPS'   : 0x9,
    'ADS1263_400SPS'    : 0x8,
    'ADS1263_100SPS'    : 0x7,
    'ADS1263_60SPS'     : 0x6,
    'ADS1263_50SPS'     : 0x5,
    'ADS1263_20SPS'     : 0x4,
    'ADS1263_16d6SPS'   : 0x3,
    'ADS1263_10SPS'     : 0x2,
    'ADS1263_5SPS'      : 0x1,
    'ADS1263_2d5SPS'    : 0x0,
}
# ADC2 data rate
ADS1263_ADC2_DRATE = {
    'ADS1263_ADC2_10SPS'    : 0,
    'ADS1263_ADC2_100SPS'   : 1,
    'ADS1263_ADC2_400SPS'   : 2,
    'ADS1263_ADC2_800SPS'   : 3,
}
# Delay time
ADS1263_DELAY = {
    'ADS1263_DELAY_0s'      : 0,
    'ADS1263_DELAY_8d7us'   : 1,
    'ADS1263_DELAY_17us'    : 2,
    'ADS1263_DELAY_35us'    : 3,
    'ADS1263_DELAY_169us'   : 4,
    'ADS1263_DELAY_139us'   : 5,
    'ADS1263_DELAY_278us'   : 6,
    'ADS1263_DELAY_555us'   : 7,
    'ADS1263_DELAY_1d1ms'   : 8,
    'ADS1263_DELAY_2d2ms'   : 9,
    'ADS1263_DELAY_4d4ms'   : 10,
    'ADS1263_DELAY_8d8ms'   : 11,
}
# DAC out volt
ADS1263_DAC_VOLT = {
    'ADS1263_DAC_VLOT_4_5'      : 0b01001,      #4.5V
    'ADS1263_DAC_VLOT_3_5'      : 0b01000,
    'ADS1263_DAC_VLOT_3'        : 0b00111,
    'ADS1263_DAC_VLOT_2_75'     : 0b00110,
    'ADS1263_DAC_VLOT_2_625'    : 0b00101,
    'ADS1263_DAC_VLOT_2_5625'   : 0b00100,
    'ADS1263_DAC_VLOT_2_53125'  : 0b00011,
    'ADS1263_DAC_VLOT_2_515625' : 0b00010,
    'ADS1263_DAC_VLOT_2_5078125': 0b00001,
    'ADS1263_DAC_VLOT_2_5'      : 0b00000,
    'ADS1263_DAC_VLOT_2_4921875': 0b10001,
    'ADS1263_DAC_VLOT_2_484375' : 0b10010,
    'ADS1263_DAC_VLOT_2_46875'  : 0b10011,
    'ADS1263_DAC_VLOT_2_4375'   : 0b10100,
    'ADS1263_DAC_VLOT_2_375'    : 0b10101,
    'ADS1263_DAC_VLOT_2_25'     : 0b10110,
    'ADS1263_DAC_VLOT_2'        : 0b10111,
    'ADS1263_DAC_VLOT_1_5'      : 0b11000,
    'ADS1263_DAC_VLOT_0_5'      : 0b11001,
}
# registration definition
ADS1263_REG = {
    # Register address, followed by reset the default values
    'REG_ID'        : 0,    # xxh
    'REG_POWER'     : 1,    # 11h
    'REG_INTERFACE' : 2,    # 05h
    'REG_MODE0'     : 3,    # 00h
    'REG_MODE1'     : 4,    # 80h
    'REG_MODE2'     : 5,    # 04h
    'REG_INPMUX'    : 6,    # 01h
    'REG_OFCAL0'    : 7,    # 00h
    'REG_OFCAL1'    : 8,    # 00h
    'REG_OFCAL2'    : 9,    # 00h
    'REG_FSCAL0'    : 10,   # 00h
    'REG_FSCAL1'    : 11,   # 00h
    'REG_FSCAL2'    : 12,   # 40h
    'REG_IDACMUX'   : 13,   # BBh
    'REG_IDACMAG'   : 14,   # 00h
    'REG_REFMUX'    : 15,   # 00h
    'REG_TDACP'     : 16,   # 00h
    'REG_TDACN'     : 17,   # 00h
    'REG_GPIOCON'   : 18,   # 00h
    'REG_GPIODIR'   : 19,   # 00h
    'REG_GPIODAT'   : 20,   # 00h
    'REG_ADC2CFG'   : 21,   # 00h
    'REG_ADC2MUX'   : 22,   # 01h
    'REG_ADC2OFC0'  : 23,   # 00h
    'REG_ADC2OFC1'  : 24,   # 00h
    'REG_ADC2FSC0'  : 25,   # 00h
    'REG_ADC2FSC1'  : 26,   # 40h
}
# comand
ADS1263_CMD = {
    'CMD_RESET'     : 0x06, # Reset the ADC, 0000 011x (06h or 07h)
    'CMD_START1'    : 0x08, # Start ADC1 conversions, 0000 100x (08h or 09h)
    'CMD_STOP1'     : 0x0A, # Stop ADC1 conversions, 0000 101x (0Ah or 0Bh)
    'CMD_START2'    : 0x0C, # Start ADC2 conversions, 0000 110x (0Ch or 0Dh)
    'CMD_STOP2'     : 0x0E, # Stop ADC2 conversions, 0000 111x (0Eh or 0Fh)
    'CMD_RDATA1'    : 0x12, # Read ADC1 data, 0001 001x (12h or 13h)
    'CMD_RDATA2'    : 0x14, # Read ADC2 data, 0001 010x (14h or 15h)
    'CMD_SYOCAL1'   : 0x16, # ADC1 system offset calibration, 0001 0110 (16h)
    'CMD_SYGCAL1'   : 0x17, # ADC1 system gain calibration, 0001 0111 (17h)
    'CMD_SFOCAL1'   : 0x19, # ADC1 self offset calibration, 0001 1001 (19h)
    'CMD_SYOCAL2'   : 0x1B, # ADC2 system offset calibration, 0001 1011 (1Bh)
    'CMD_SYGCAL2'   : 0x1C, # ADC2 system gain calibration, 0001 1100 (1Ch)
    'CMD_SFOCAL2'   : 0x1E, # ADC2 self offset calibration, 0001 1110 (1Eh)
    'CMD_RREG'      : 0x20, # Read registers 001r rrrr (20h+000r rrrr)
    'CMD_RREG2'     : 0x00, # number of registers to read minus 1, 000n nnnn
    'CMD_WREG'      : 0x40, # Write registers 010r rrrr (40h+000r rrrr)
    'CMD_WREG2'     : 0x00, # number of registers to write minus 1, 000n nnnn
}

class ADS1263:
    def __init__(self):
        self.rst_pin = config.RST_PIN
        self.cs_pin = config.CS_PIN
        self.drdy_pin = config.DRDY_PIN
        self.ScanMode = 1

    # Hardware reset
    def ADS1263_reset(self):
        config.digital_write(self.rst_pin, GPIO.HIGH)
        config.delay_ms(200)
        config.digital_write(self.rst_pin, GPIO.LOW)
        config.delay_ms(200)
        config.digital_write(self.rst_pin, GPIO.HIGH)
        config.delay_ms(200)
    
    
    def ADS1263_WriteCmd(self, reg):
        config.digital_write(self.cs_pin, GPIO.LOW)#cs  0
        config.spi_writebyte([reg])
        config.digital_write(self.cs_pin, GPIO.HIGH)#cs 1
    
    
    def ADS1263_WriteReg(self, reg, data):
        config.digital_write(self.cs_pin, GPIO.LOW)#cs  0
        config.spi_writebyte([ADS1263_CMD['CMD_WREG'] | reg, 0x00, data])
        config.digital_write(self.cs_pin, GPIO.HIGH)#cs 1
        
        
    def ADS1263_ReadData(self, reg):
        config.digital_write(self.cs_pin, GPIO.LOW)#cs  0
        config.spi_writebyte([ADS1263_CMD['CMD_RREG'] | reg, 0x00])
        data = config.spi_readbytes(1)
        config.digital_write(self.cs_pin, GPIO.HIGH)#cs 1
        return data

    
    # Check Data
    def ADS1263_CheckSum(self, val, byt):
        sum = 0
        mask = 0xff     # 8 bits mask
        while(val) :
            # print(sum, val)
            sum += val & mask   # only add the lower values
            val = val >> 8      # shift down
        sum += 0x9b
        # print(sum, byt)
        return (sum&0xff) ^ byt     # if sum equal byt, this will be 0
    
    
    # waiting for a busy end, just for ADC1
    def ADS1263_WaitDRDY(self):
        i = 0
        while(1):
            i+=1
            if(config.digital_read(self.drdy_pin) == 0):
                break
            if(i >= 400000):
                print ("Time Out ...\r\n")
                break
        
    # Check chip ID, success is return 1
    def ADS1263_ReadChipID(self):
        id = self.ADS1263_ReadData(ADS1263_REG['REG_ID'])
        return id[0] >> 5
    
    
    def ADS1263_SetMode(self, Mode):
        self.ScanMode = Mode
        
        
    #The configuration parameters of ADC, gain and data rate
    def ADS1263_ConfigADC(self, gain, drate):
        MODE2 = 0x80    # 0x80:PGA bypassed, 0x00:PGA enabled
        MODE2 |= (gain << 4) | drate
        self.ADS1263_WriteReg(ADS1263_REG['REG_MODE2'], MODE2)
        if(self.ADS1263_ReadData(ADS1263_REG['REG_MODE2'])[0] == MODE2):
            print("REG_MODE2 success")
        else:
            print("REG_MODE2 unsuccess")

        REFMUX = 0x24   # 0x00:+-2.5V as REF, 0x24:VDD,VSS as REF
        self.ADS1263_WriteReg(ADS1263_REG['REG_REFMUX'], REFMUX)
        if(self.ADS1263_ReadData(ADS1263_REG['REG_REFMUX'])[0] == REFMUX):
            print("REG_REFMUX success")
        else:
            print("REG_REFMUX unsuccess")
            
        MODE0 = ADS1263_DELAY['ADS1263_DELAY_35us']
        self.ADS1263_WriteReg(ADS1263_REG['REG_MODE0'], MODE0)
        if(self.ADS1263_ReadData(ADS1263_REG['REG_MODE0'])[0] == MODE0):
            print("REG_MODE0 success")
        else:
            print("REG_MODE0 unsuccess")

        MODE1 = 0x84    # Digital Filter; 0x84:FIR, 0x64:Sinc4, 0x44:Sinc3, 0x24:Sinc2, 0x04:Sinc1
        self.ADS1263_WriteReg(ADS1263_REG['REG_MODE1'], MODE1)
        if(self.ADS1263_ReadData(ADS1263_REG['REG_MODE1'])[0] == MODE1):
            print("REG_MODE1 success")
        else:
            print("REG_MODE1 unsuccess")

    #The configuration parameters of ADC2, gain and data rate
    def ADS1263_ConfigADC2(self, gain, drate):
        ADC2CFG = 0x20          # REF, 0x20:VAVDD and VAVSS, 0x00:+-2.5V
        ADC2CFG |= (drate << 6) | gain
        self.ADS1263_WriteReg(ADS1263_REG['REG_ADC2CFG'], ADC2CFG)
        if(self.ADS1263_ReadData(ADS1263_REG['REG_ADC2CFG'])[0] == ADC2CFG):
            print("REG_ADC2CFG success")
        else:
            print("REG_ADC2CFG unsuccess")
            
        MODE0 = ADS1263_DELAY['ADS1263_DELAY_35us']
        self.ADS1263_WriteReg(ADS1263_REG['REG_MODE0'], MODE0)
        if(self.ADS1263_ReadData(ADS1263_REG['REG_MODE0'])[0] == MODE0):
            print("REG_MODE0 success")
        else:
            print("REG_MODE0 unsuccess")
            

    # Set ADC1 Measuring channel
    def ADS1263_SetChannal(self, Channal):
        if Channal > 10:
            return 0
        INPMUX = (Channal << 4) | 0x0a
        self.ADS1263_WriteReg(ADS1263_REG['REG_INPMUX'], INPMUX)
        if(self.ADS1263_ReadData(ADS1263_REG['REG_INPMUX'])[0] == INPMUX):
            # print("REG_INPMUX success")
            pass
        else:
            print("REG_INPMUX unsuccess")


    # Set ADC2 Measuring channel
    def ADS1263_SetChannal_ADC2(self, Channal):
        if Channal > 10:
            return 0
        INPMUX = (Channal << 4) | 0x0a
        self.ADS1263_WriteReg(ADS1263_REG['REG_ADC2MUX'], INPMUX)
        if(self.ADS1263_ReadData(ADS1263_REG['REG_ADC2MUX'])[0] == INPMUX):
            # print("REG_ADC2MUX success")
            pass
        else:
            print("REG_ADC2MUX unsuccess")
            

    # Set ADC1 Measuring differential channel
    def ADS1263_SetDiffChannal(self, Channal):
        if Channal == 0:
            INPMUX = (0<<4) | 1     #DiffChannal    AIN0-AIN1
        elif Channal == 1:
            INPMUX = (2<<4) | 3     #DiffChannal    AIN2-AIN3
        elif Channal == 2:
            INPMUX = (4<<4) | 5     #DiffChannal    AIN4-AIN5
        elif Channal == 3:
            INPMUX = (6<<4) | 7     #DiffChannal    AIN6-AIN7
        elif Channal == 4:
            INPMUX = (8<<4) | 9     #DiffChannal    AIN8-AIN9
        self.ADS1263_WriteReg(ADS1263_REG['REG_INPMUX'], INPMUX)
        if(self.ADS1263_ReadData(ADS1263_REG['REG_INPMUX'])[0] == INPMUX):
            # print("REG_INPMUX success")
            pass
        else:
            print("REG_INPMUX unsuccess")
            

    # Set ADC2 Measuring differential channel
    def ADS1263_SetDiffChannal_ADC2(self, Channal):
        if Channal == 0:
            INPMUX = (0<<4) | 1     #DiffChannal    AIN0-AIN1
        elif Channal == 1:
            INPMUX = (2<<4) | 3     #DiffChannal    AIN2-AIN3
        elif Channal == 2:
            INPMUX = (4<<4) | 5     #DiffChannal    AIN4-AIN5
        elif Channal == 3:
            INPMUX = (6<<4) | 7     #DiffChannal    AIN6-AIN7
        elif Channal == 4:
            INPMUX = (8<<4) | 9     #DiffChannal    AIN8-AIN9
        self.ADS1263_WriteReg(ADS1263_REG['REG_ADC2MUX'], INPMUX)
        if(self.ADS1263_ReadData(ADS1263_REG['REG_ADC2MUX'])[0] == INPMUX):
            # print("REG_ADC2MUX success")
            pass
        else:
            print("REG_ADC2MUX unsuccess")
            

    # Device initialization (ADC1)
    def ADS1263_init_ADC1(self, Rate1 = 'ADS1263_14400SPS'):
        if (config.module_init() != 0):
            return -1
        self.ADS1263_reset()
        id = self.ADS1263_ReadChipID()
        if id == 0x01 :
            print("ID Read success  ")
        else:
            print("ID Read failed   ")
            return -1
        self.ADS1263_WriteCmd(ADS1263_CMD['CMD_STOP1'])
        self.ADS1263_ConfigADC(ADS1263_GAIN['ADS1263_GAIN_1'], ADS1263_DRATE[Rate1])
        self.ADS1263_WriteCmd(ADS1263_CMD['CMD_START1'])
        return 0
        

    # Device initialization (ADC2)
    def ADS1263_init_ADC2(self, Rate2 = 'ADS1263_ADC2_100SPS'):
        if (config.module_init() != 0):
            return -1
        self.ADS1263_reset()
        id = self.ADS1263_ReadChipID()
        if id == 0x01 :
            print("ID Read success  ")
        else:
            print("ID Read failed   ")
            return -1
        self.ADS1263_WriteCmd(ADS1263_CMD['CMD_STOP2'])
        self.ADS1263_ConfigADC2(ADS1263_ADC2_GAIN['ADS1263_ADC2_GAIN_1'], ADS1263_ADC2_DRATE[Rate2])
        return 0

        
    # Read ADC data
    def ADS1263_Read_ADC_Data(self):
        config.digital_write(self.cs_pin, GPIO.LOW)#cs  0
        while(1):
            config.spi_writebyte([ADS1263_CMD['CMD_RDATA1']])
            # config.delay_ms(10)
            if(config.spi_readbytes(1)[0] & 0x40 != 0):
                break
        buf = config.spi_readbytes(5)
        config.digital_write(self.cs_pin, GPIO.HIGH)#cs 1
        read  = (buf[0]<<24) & 0xff000000
        read |= (buf[1]<<16) & 0xff0000
        read |= (buf[2]<<8) & 0xff00
        read |= (buf[3]) & 0xff
        CRC = buf[4]
        # print(read, CRC)
        if(self.ADS1263_CheckSum(read, CRC) != 0):
            print("ADC1 data read error!")
        return read
 
 
    # Read ADC2 data
    def ADS1263_Read_ADC2_Data(self):
        read = 0
        config.digital_write(self.cs_pin, GPIO.LOW)#cs  0
        while(1):
            config.spi_writebyte([ADS1263_CMD['CMD_RDATA2']])
            # config.delay_ms(10)
            if(config.spi_readbytes(1)[0] & 0x80 != 0):
                break
        buf = config.spi_readbytes(5)
        config.digital_write(self.cs_pin, GPIO.HIGH)#cs 1
        read |= (buf[0]<<16) & 0xff0000
        read |= (buf[1]<<8) & 0xff00
        read |= (buf[2]) & 0xff
        CRC = buf[4]
        if(self.ADS1263_CheckSum(read, CRC) != 0):
            print("ADC2 data read error!")
        return read
        
        
    # Read ADC1 specified channel data
    def ADS1263_GetChannalValue(self, Channel):
        if(self.ScanMode == 0):# 0  Single-ended input 10 channel Differential input 5 channel 
            if(Channel>10):
                print("The number of channels must be less than 10")
                return 0
            self.ADS1263_SetChannal(Channel)
            self.ADS1263_WaitDRDY()
            Value = self.ADS1263_Read_ADC_Data()
        else:
            if(Channel>4):
                print("The number of channels must be less than 5")
                return 0
            self.ADS1263_SetDiffChannal(Channel)
            self.ADS1263_WaitDRDY()
            Value = self.ADS1263_Read_ADC_Data()
        return Value


    # Read ADC2 specified channel data
    def ADS1263_GetChannalValue_ADC2(self, Channel):
        if(self.ScanMode == 0):# 0  Single-ended input 10 channel Differential input 5 channel
            if(Channel>10):
                print("The number of channels must be less than 10")
                return 0
            self.ADS1263_SetChannal_ADC2(Channel)
            # config.delay_ms(2)
            self.ADS1263_WriteCmd(ADS1263_CMD['CMD_START2'])
            # config.delay_ms(2)
            Value = self.ADS1263_Read_ADC2_Data()
        else:
            if(Channel>4):
                print("The number of channels must be less than 5")
                return 0
            self.ADS1263_SetDiffChannal_ADC2(Channel)
            # config.delay_ms(2) 
            self.ADS1263_WriteCmd(ADS1263_CMD['CMD_START2'])
            # config.delay_ms(2) 
            Value = self.ADS1263_Read_AD2C_Data()
        return Value
        

    def ADS1263_GetAll(self, List):
        ADC_Value = []
        for i in List:
            ADC_Value.append(self.ADS1263_GetChannalValue(i))
        return ADC_Value
          
          
    def ADS1263_GetAll_ADC2(self):
        ADC_Value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, 10, 1):
            ADC_Value[i] = self.ADS1263_GetChannalValue_ADC2(i)
            self.ADS1263_WriteCmd(ADS1263_CMD['CMD_STOP2'])
            config.delay_ms(20) 
        return ADC_Value
        
        
    def ADS1263_RTD_Test(self):
        Delay = ADS1263_DELAY['ADS1263_DELAY_8d8ms']
        Gain = ADS1263_GAIN['ADS1263_GAIN_1']
        Drate = ADS1263_DRATE['ADS1263_20SPS']
        
        #MODE0 (CHOP OFF)
        MODE0 = Delay 
        self.ADS1263_WriteReg(ADS1263_REG['REG_MODE0'], MODE0) 
        config.delay_ms(1) 

        #(IDACMUX) IDAC2 AINCOM,IDAC1 AIN3
        IDACMUX = (0x0a<<4) | 0x03 
        self.ADS1263_WriteReg(ADS1263_REG['REG_IDACMUX'], IDACMUX) 
        config.delay_ms(1) 

        #((IDACMAG)) IDAC2 = IDAC1 = 250uA
        IDACMAG = (0x03<<4) | 0x03 
        self.ADS1263_WriteReg(ADS1263_REG['REG_IDACMAG'], IDACMAG) 
        config.delay_ms(1) 

        MODE2 = (Gain << 4) | Drate 
        self.ADS1263_WriteReg(ADS1263_REG['REG_MODE2'], MODE2) 
        config.delay_ms(1) 

        #INPMUX (AINP = AIN7, AINN = AIN6)
        INPMUX = (0x07<<4) | 0x06 
        self.ADS1263_WriteReg(ADS1263_REG['REG_INPMUX'], INPMUX) 
        config.delay_ms(1) 

        # REFMUX AIN4 AIN5
        REFMUX = (0x03<<3) | 0x03 
        self.ADS1263_WriteReg(ADS1263_REG['REG_REFMUX'], REFMUX) 
        config.delay_ms(1) 

        #Read one conversion
        self.ADS1263_WriteCmd(ADS1263_CMD['CMD_START1']) 
        config.delay_ms(10) 
        self.ADS1263_WaitDRDY() 
        Value = self.ADS1263_Read_ADC_Data() 
        self.ADS1263_WriteCmd(ADS1263_CMD['CMD_STOP1']) 
    
        return Value
        
    
    def ADS1263_DAC_Test(self, isPositive, isOpen):
        Volt = ADS1263_DAC_VOLT['ADS1263_DAC_VLOT_3']
        
        if(isPositive):
            Reg = ADS1263_REG['REG_TDACP']  # IN6
        else:
            Reg = ADS1263_REG['REG_TDACN']  # IN7

        if(isOpen):
            Value = Volt | 0x80
        else:
            Value = 0x00

        self.ADS1263_WriteReg(Reg, Value) 
        
        
    def ADS1263_Exit(self):
        config.module_exit()
        
### END OF FILE ###

