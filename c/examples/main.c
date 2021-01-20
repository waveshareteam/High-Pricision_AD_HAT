#include <stdlib.h>     //exit()
#include <signal.h>     //signal()
#include <time.h>
#include "ADS1263.h"
#include "stdio.h"
#include <string.h>

#define TEST_ADC	1			// ADC Test part
#define	TEST_RTD	0			// RTD Test part
#define REF			5.08		//Modify according to actual voltage
								//external AVDD and AVSS(Default), or internal 2.5V

void  Handler(int signo)
{
    //System Exit
    printf("\r\n END \r\n");
    DEV_Module_Exit();
    exit(0);
}

int main(void)
{
    UDOUBLE ADC[10];
	UBYTE i;
	double RES, TEMP;
	
    // Exception handling:ctrl + c
    signal(SIGINT, Handler);
	
    printf("ADS1263 Demo \r\n");
    DEV_Module_Init();

	ADS1263_SetMode(0);
	if(ADS1263_init() == 1) {
		printf("\r\n END \r\n");
		DEV_Module_Exit();
		exit(0);
	}
	
	/* Test DAC */
	// ADS1263_DAC(ADS1263_DAC_VLOT_3, Positive_A6, Open);		
	// ADS1263_DAC(ADS1263_DAC_VLOT_2, Negative_A7, Open);
	
    while(1) {
		if(TEST_ADC) {
			ADS1263_GetAll(ADC);	// Get ADC1 value
			for(i=0; i<10; i++) {
				if((ADC[i]>>31) == 1)
					printf("IN%d is -%lf \r\n", i, REF*2 - ADC[i]/2147483648.0 * REF);		//7fffffff + 1
				else
					printf("IN%d is %lf \r\n", i, ADC[i]/2147483647.0 * REF);		//7fffffff
			}
			DEV_Delay_ms(200);
			
			/*ADC 2*/
			// ADS1263_GetAll_ADC2(ADC);	// Get ADC2 value
			// for(i=0; i<10; i++) {
				// if((ADC[i]>>23) == 1)
					// printf("IN%d is -%lf \r\n", i, REF*2 - ADC[i]/8388608.0 * REF);		//7fffff + 1
				// else
					// printf("IN%d is %lf \r\n", i, ADC[i]/8388607.0 * REF);		//7fffff
			// }
			// DEV_Delay_ms(200);
			
			printf("\33[11A");//Move the cursor up 6 lines
		}else if(TEST_RTD) {
			ADC[0] = ADS1263_RTD(ADS1263_DELAY_8d8ms, ADS1263_GAIN_1, ADS1263_20SPS);
			RES = ADC[0]/2147483647.0 * 2.0 * 2000.0;	//2000.0 -- 2000R, 2.0 -- 2*i
			printf("Res is %lf \r\n", RES);
			TEMP = (RES/100.0 - 1.0) / 0.00385;		//0.00385 -- pt100
			printf("Temp is %lf \r\n", TEMP);
			DEV_Delay_ms(200);
			
			printf("\33[2A");//Move the cursor up 2 lines
		}
	}
	
	return 0;
}
