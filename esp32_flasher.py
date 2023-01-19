import tkinter as tk
from tkinter import filedialog  # for selecting files in GUI
import serial  # for identifying available com ports
import subprocess  # for running command line commands

class FlashTool(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ESP32 Flash Tool")  # set the title of the GUI window
        self.geometry("300x200")  # set the size of the GUI window
        self.resizable(False, False)  # make the window non-resizable

        # create label and file selection button for bootloader file
        self.bootloader_label = tk.Label(self, text="Bootloader file:")
        self.bootloader_label.pack()
        self.bootloader_file = tk.StringVar()
        self.bootloader_button = tk.Button(self, text="Select", command=self.select_bootloader)
        self.bootloader_button.pack()

        # create label and file selection button for partition file

        self.partition_label = tk.Label(self, text="Partition file:")
        self.partition_label.pack()
        self.partition_file = tk.StringVar()
        self.partition_button = tk.Button(self, text="Select", command=self.select_partition)
        self.partition_button.pack()

        # create label and file selection button for firmware file
        self.firmware_label = tk.Label(self, text="Firmware file:")
        self.firmware_label.pack()
        self.firmware_file = tk.StringVar()
        self.firmware_button = tk.Button(self, text="Select", command=self.select_firmware)
        self.firmware_button.pack()

        # create flash button
        self.flash_button = tk.Button(self, text="Flash", command=self.flash)
        self.flash_button.pack()

    def select_bootloader(self):
        """Opens file selection dialog to select bootloader file"""
        bootloader_path = filedialog.askopenfilename()
        self.bootloader_file.set(bootloader_path)

    def select_partition(self):
        """Opens file selection dialog to select partition file"""
        partition_path = filedialog.askopenfilename()
        self.partition_file.set(partition_path)

    def select_firmware(self):
        """Opens file selection dialog to select firmware file"""
        firmware_path = filedialog.askopenfilename()
        self.firmware_file.set(firmware_path)

    def flash(self):
        """Flashes firmware to ESP32 using specified files"""
        try:
            # get the path of the com port
            port = serial.tools.list_ports()[0].device
            # construct the command to flash the firmware
            command = f"esptool.py --chip esp32 --port {port} --baud 921600 --before default_reset --after hard_reset write_flash -z --flash_mode dio --flash_freq 40m --flash_size detect 0x1000 {self.bootloader_file.get()} 0x8000 {self.partition_file.get()} 0x10000 {self.firmware_file.get()}"
            # flash the firmware
            subprocess.call(command, shell=True)
            # create a label to show the flashing is complete
            self.flash_complete = tk.Label(self, text="Flashing complete!")
            self.flash_complete.pack()
            # create a button to open the second part of the GUI
            self.next_button = tk.Button(self, text="Next", command=self.open_next_part)
            self.next_button.pack()
        except (FileNotFoundError, IndexError, serial.SerialException) as e:
            self.flash_complete = tk.Label(self, text="Flashing failed!")
            self.flash_complete.pack()
            self.flash_complete.config(fg="red")
            self.flash_error = tk.Label(self, text=str(e))
            self.flash_error.pack()
            self.flash_error.config(fg="red")
    def open_next_part(self):
        """Opens the second part of the GUI"""
        # your code here to open the second part of the GUI as shown in the attachment

if __name__ == "__main__":
    tool = FlashTool()
    tool.mainloop()