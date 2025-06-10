import time
from os import system
from termcolor import colored, cprint


system('cls')

def kue():
    kue = [
        "    *   *  .  .  .       *   ",
        "  *       _|__|__|_  *       ",
        "     *  _|'''''''''|_   *    ",
        " *    _|||||||||||||||_   *  ",
        "     |~~~~H-A-P-P-Y~~~~|     ",
        "  *  |-B-I-R-T-H-D-A-Y-| *   ",
        "     |~0~0~0~0~0~0~0~0~|  *  ",
        "     ~~~~~~~~~~~~~~~~~~~     "
    ]

    
    for baris in kue:
        cprint(baris, "white", "on_red")
        time.sleep(0.3)

def ucapan() :
    cprint("    Selamat Ulang Tahun !    ", "red", "on_white")
    time.sleep(1)
    cprint("Semoga kamu bahagia selalu :)","red", "on_white")


kue()
time.sleep(0.5)
ucapan()
