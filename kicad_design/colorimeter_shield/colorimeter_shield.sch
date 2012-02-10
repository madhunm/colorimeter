EESchema Schematic File Version 2  date Fri 10 Feb 2012 11:31:22 AM PST
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:arduino_shieldsNCL
LIBS:tcs3200
LIBS:colorimeter_shield-cache
EELAYER 25  0
EELAYER END
$Descr A4 11700 8267
encoding utf-8
Sheet 1 1
Title ""
Date "10 feb 2012"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
NoConn ~ 5450 4550
NoConn ~ 3550 4350
NoConn ~ 3550 4250
NoConn ~ 3550 4050
NoConn ~ 5450 3450
NoConn ~ 5450 3350
Wire Wire Line
	5450 4050 5950 4050
Wire Wire Line
	8950 3800 9450 3800
Wire Wire Line
	8950 3600 9450 3600
Wire Wire Line
	8150 3900 7650 3900
Wire Wire Line
	8150 3700 7650 3700
Wire Wire Line
	8150 3500 7650 3500
Wire Wire Line
	5450 4250 5950 4250
Wire Wire Line
	5450 3550 5950 3550
Wire Wire Line
	5450 3750 5950 3750
Wire Wire Line
	3550 3850 3050 3850
Wire Wire Line
	3550 3750 3050 3750
Wire Wire Line
	5450 3850 5950 3850
Wire Wire Line
	5450 3650 5950 3650
Wire Wire Line
	5450 4350 5950 4350
Wire Wire Line
	8150 3600 7650 3600
Wire Wire Line
	8150 3800 7650 3800
Wire Wire Line
	8950 3500 9450 3500
Wire Wire Line
	8950 3700 9450 3700
Wire Wire Line
	8950 3900 9450 3900
Wire Wire Line
	5450 4150 5950 4150
Wire Wire Line
	1600 3150 1600 3450
Wire Wire Line
	2450 3150 2450 3450
Text Label 2450 3450 0    60   ~ 0
5V
$Comp
L PWR_FLAG #FLG01
U 1 1 4F04D294
P 2450 3150
F 0 "#FLG01" H 2450 3420 30  0001 C CNN
F 1 "PWR_FLAG" H 2450 3380 30  0000 C CNN
	1    2450 3150
	1    0    0    -1  
$EndComp
Text Label 1600 3450 0    60   ~ 0
GND
$Comp
L GND #PWR02
U 1 1 4F04D249
P 1600 3450
F 0 "#PWR02" H 1600 3450 30  0001 C CNN
F 1 "GND" H 1600 3380 30  0001 C CNN
	1    1600 3450
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG03
U 1 1 4F04D23F
P 1600 3150
F 0 "#FLG03" H 1600 3420 30  0001 C CNN
F 1 "PWR_FLAG" H 1600 3380 30  0000 C CNN
	1    1600 3150
	1    0    0    -1  
$EndComp
NoConn ~ 5450 4450
Text Label 5950 4050 2    60   ~ 0
S3
Text Label 5950 4150 2    60   ~ 0
S2
Text Notes 7950 3250 0    60   ~ 0
header to color sensor board
Text Label 9450 3500 2    60   ~ 0
RED
Text Label 9450 3600 2    60   ~ 0
GREEN
Text Label 9450 3700 2    60   ~ 0
BLUE
Text Label 9450 3800 2    60   ~ 0
FREQ
Text Label 9450 3900 2    60   ~ 0
S3
Text Label 7650 3900 0    60   ~ 0
S2
Text Label 7650 3800 0    60   ~ 0
S1
Text Label 7650 3700 0    60   ~ 0
S0
Text Label 7650 3600 0    60   ~ 0
GND
Text Label 7650 3500 0    60   ~ 0
5V
NoConn ~ 3550 3550
NoConn ~ 3550 3650
NoConn ~ 3550 3950
NoConn ~ 3550 4450
NoConn ~ 3550 4550
NoConn ~ 3550 4650
NoConn ~ 3550 4750
NoConn ~ 5450 4750
NoConn ~ 5450 4650
NoConn ~ 5450 3250
NoConn ~ 5450 3150
Text Label 3050 3850 0    60   ~ 0
GND
Text Label 3050 3750 0    60   ~ 0
5V
Text Label 5950 3550 2    60   ~ 0
RED
Text Label 5950 3650 2    60   ~ 0
GREEN
Text Label 5950 3750 2    60   ~ 0
BLUE
Text Label 5950 3850 2    60   ~ 0
FREQ
Text Label 5950 4250 2    60   ~ 0
S1
Text Label 5950 4350 2    60   ~ 0
S0
$Comp
L ARDUINO_SHIELD SHIELD1
U 1 1 4F03B33E
P 4500 3950
F 0 "SHIELD1" H 4150 4900 60  0000 C CNN
F 1 "ARDUINO_SHIELD" H 4550 3000 60  0000 C CNN
	1    4500 3950
	1    0    0    -1  
$EndComp
$Comp
L CONN_5X2 P2
U 1 1 4F03AC98
P 8550 3700
F 0 "P2" H 8550 4000 60  0000 C CNN
F 1 "CONN_5X2" V 8550 3700 50  0000 C CNN
	1    8550 3700
	1    0    0    -1  
$EndComp
$EndSCHEMATC
