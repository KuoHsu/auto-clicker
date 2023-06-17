import time
import pyautogui
import keyboard


class Script():
    def __init__(self):
        self.exit_flag = False
        self.start_flag = False
        keyboard.add_hotkey("e",lambda: self.exit())
        keyboard.add_hotkey("f",lambda: self.start_status_change())

    def run(self):
        print_f = False
        while(not self.exit_flag):
            if not print_f:
                print("F: start click or stop click\nE: exit application")
                print_f = True
            while(self.start_flag):
                pyautogui.click()

    def start_status_change(self):
        self.start_flag = not self.start_flag

    def exit(self):
        self.exit_flag = True




script = Script()
script.run()