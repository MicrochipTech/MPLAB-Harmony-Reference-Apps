---
grand_parent: Reference Applications
parent: Curiosity PIC32MX470 Development Board
title: Getting Started
nav_order: 1
---
<img src = "images/microchip_logo.png">
<img src = "images/microchip_mplab_harmony_logo_small.png">

# Getting Started Application on Curiosity PIC32MX470 Development Board
-----
## Description

>  The application reads the current room temperature from the temperature sensor on the MikroElectronika Weather click board. 
	The temperature read is displayed on a serial console periodically every 500 milliseconds. The periodicity of the temperature 
	values displayed on the serial console is changed to one second, two seconds, four seconds, and back to 500 milliseconds every 
	time you press the switch S1 on the Curiosity PIC32MX470 Development Board. Also, LED1 is toggled every time the temperature is 
	displayed on the serial console.

## Modules/Technology Used:

- Peripheral Modules      
	- I2C
	- Timer
	- Core Timer
	- GPIO
	- UART
	- DMA

## Hardware Used:

- [Curiosity PIC32MX470 Development Board](http://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=DM320103)   
- [MikroElectronika Weather click board](https://www.mikroe.com/weather-click)
- [MikroElectronika USB UART click board ](https://www.mikroe.com/usb-uart-click)


## Software/Tools Used:
<span style="color:blue"> *This project has been verified to work with the following versions of software tools:*</span>  

 - [MPLAB Harmony v3 "csp" repo v3.5.2](https://github.com/Microchip-MPLAB-Harmony/csp/releases/tag/v3.5.2)
 - [MPLAB Harmony v3 "dev_packs" repo v3.5.0](https://github.com/Microchip-MPLAB-Harmony/dev_packs/releases/tag/v3.5.0)  
 - [MPLAB Harmony v3 "mhc" repo v3.3.3](https://github.com/Microchip-MPLAB-Harmony/mhc/releases/tag/v3.3.3)   
 - MPLAB Harmony Configurator Plugin v3.4.0
 - [MPLAB X IDE v5.30](https://www.microchip.com/mplab/mplab-x-ide)
 - [MPLAB XC32 Compiler v2.30](https://www.microchip.com/mplab/compilers)
 - [MPLAB X IPE v5.30](https://www.microchip.com/mplab/mplab-integrated-programming-environment)  
 - Any Serial Terminal application like Tera Term terminal application.  

 <span style="color:blue"> *Because Microchip regularly update tools, occasionally issue(s) could be discovered while using the newer versions of the tools. If the project doesn’t seem to work and version incompatibility is suspected, It is recommended to double-check and use the same versions that the project was tested with.* </span>  

## Setup:  
- Connect the Curiosity PIC32MX470 Development Board to the Host PC as a USB Device 
  through a Type-A male to micro-B USB cable connected to Micro-B USB port
- Connect the MikroElectronika Weather click board on the mikroBUS interface 1
- Connect the MikroElectronika USB UART click board on the mikroBUS interface 2 
- Connect USB Type-A male to mini-B male cable to USB-UART serial port through mikroBUS interface 2  
<img src = "images/hardware_setup.png" width="500" height="325" align="middle">

## Programming binary/hex file:
If you are not interested in installing development tools. The pre-built binary/hex file can be programmed to the target  

### Steps to program the hex file using MPLAB X IPE
- Open MPLAB X IPE
- Select Device has "PIC32MX470F512H"
- Power the Curiosity PIC32MX470 Development Board from a Host PC through a Type-A male to Micro-B USB cable connected to Micro-B port
- Once Power cable is connected, "PKOB" hardware tool is identified as a programmer
- Browse to hex file (getting_started_hex_file.hex)
- Click on program button. The device gets programmed in sometime
- Follow the steps in "Running the Demo" section below

## Programming/Debugging Application Project:
- Open the project (getting_started\firmware\pic32mx470_curiosity.X) in MPLAB X IDE
- Ensure "PKOB4" is selected as hardware tool to program/debug the application
- Build the code and program the device by clicking on the "make and program" button in MPLAB X IDE tool bar
- Follow the steps in "Running the Demo" section below

## Running the Demo:
- Open the Tera Term terminal application on your PC (from the Windows® Start menu by pressing the Start button)
- Change the baud rate to 115200
- You should see the temperature values (in °F) being displayed on the terminal every 500 milliseconds, as shown below  
<img src = "images/result1.png" width="425" height="235" align="middle">  
- Also, notice LED1 blinking at a 500 millisecond rate
- You may vary the temperature by placing your finger on the temperature sensor (for a few seconds)  
<img src = "images/temp_sensor_placement.png" width="500" height="325" align="middle">  
- Press the S1 switch on the Curiosity PIC32MX470 Development Board to change the default sampling rate to one second  
<img src = "images/user_button_placement.png" width="500" height="325" align="middle">  
<img src = "images/result2.png" width="345" height="165" align="middle">  
- Every subsequent press of switch S1 on the Curiosity PIC32MX470 Development Board changes the default sampling 
  rate to two seconds, four seconds, 500 milliseconds and back to one second in cyclic order as shown below  
  <img src = "images/result3.png" width="315" height="440" align="middle">  
- While the temperature sampling rate changes on every switch S1 press, notice LED1 toggling at the same sampling rate

## Comments:
- Reference Training Module: [Getting Started With Harmony v3 Peripheral Libraries on PIC32MX 470 MCUs](https://microchipdeveloper.com/harmony3:pic32mx470-getting-started-training-module)
- This application demo builds and works out of box by following the instructions above in "Running the Demo" section. If you need to enhance/customize this application demo, you need to use the MPLAB Harmony v3 Software framework. Refer links below to setup and build your applications using MPLAB Harmony. 
	- [How to Setup MPLAB Harmony v3 Software Development Framework](https://www.microchip.com/mymicrochip/filehandler.aspx?ddocname=en1000821) 
	- [How to Build an Application by Adding a New PLIB, Driver, or Middleware to an Existing MPLAB Harmony v3 Project](http://ww1.microchip.com/downloads/en/DeviceDoc/How_to_Build_Application_Adding_PLIB_%20Driver_or_Middleware%20_to_MPLAB_Harmony_v3Project_DS90003253A.pdf)  
              
## Revision: 
- v1.0 released demo application