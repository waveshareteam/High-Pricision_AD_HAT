#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import ADS1263
import RPi.GPIO as GPIO

REF = 5.08          # Modify according to actual voltage
                    # external AVDD and AVSS(Default), or internal 2.5V
TEST_ADC = 1        # ADC Test part
TEST_RTD = 0        # RTD Test part

try:
    ADC = ADS1263.ADS1263()
    if (ADC.ADS1263_init() == -1):
        exit()

    # ADC.ADS1263_DAC_Test(1, 1)      # Open IN6
    # ADC.ADS1263_DAC_Test(0, 1)      # Open IN7
    
    while(1):
        if(TEST_ADC):       # ADC Test
            ADC_Value = ADC.ADS1263_GetAll()    # get ADC1 value
            for i in range(0, 10):
                if(ADC_Value[i]>>31 ==1):
                    print("ADC1 IN%d = -%lf" %(i, (REF*2 - ADC_Value[i] * REF / 0x80000000)))  
                else:
                    print("ADC1 IN%d = %lf" %(i, (ADC_Value[i] * REF / 0x7fffffff)))   # 32bit
                    
            # ADC_Value = ADC.ADS1263_GetAll_ADC2()   # get ADC2 value
            # for i in range(0, 10):
                # if(ADC_Value[i]>>23 ==1):
                    # print("ADC2 IN%d = -%lf"%(i, (REF*2 - ADC_Value[i] * REF / 0x800000)))
                # else:
                    # print("ADC2 IN%d = %lf"%(i, (ADC_Value[i] * REF / 0x7fffff)))     # 16bit
                    
            print("\33[12A")
            
        elif(TEST_RTD):     # RTD Test
            ADC_Value = ADC.ADS1263_RTD_Test()
            RES = ADC_Value / 2147483647.0 * 2.0 *2000.0       #2000.0 -- 2000R, 2.0 -- 2*i
            print("RES is %lf"%RES)
            TEMP = (RES/100.0 - 1.0) / 0.00385      #0.00385 -- pt100
            print("TEMP is %lf"%TEMP)
            print("\33[3A")

except IOError as e:
    print(e)
   
except KeyboardInterrupt:
    print("ctrl + c:")
    print("Program end")
    ADC.ADS1263_Exit()
    exit()
   
