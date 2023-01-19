# ESP32 Flash Tool

This is a simple tool that allows you to flash firmware to an ESP32 using a GUI.

## Requirements
- Python 3
- Tkinter
- pyserial
- esptool

## Installation

- Clone this repository to your local machine
- Install the required packages by running `pip install -r requirements.txt`

## Usage
- Run the script using the command `python flash_tool.py`
- Select the bootloader, partition, and firmware files using the provided buttons
- Press the "Flash" button to start the flashing process
- If the flashing is successful, a message will be displayed and a "Next" button will appear
- Press the "Next" button to open the second part of the GUI