import tkinter as tk
from tkinter import filedialog, Text
import os
import base64

class Fileio:

    def exportfile(self, Man):

        directory = filedialog.askdirectory(title="Export File")
        if not directory:
            return False

        directory += "/encrypted.enc"

        f = open(directory, "w")
        f.write(Man.keytext.decode('utf-8'))
        f.write("\n")

        for i in range(0, len(Man.loaded)):

            for j in range(0, 3):
                f.write(Man.encrypt(Man.loaded[i][j]).decode('utf-8'))
                f.write("\n")

        f.close()
        return True

    def importfile(self, Man):

        filename = filedialog.askopenfilename(initialdir="C:/Desktop/", title="Import File", filetypes=(("Encrypted Files", "*.enc"), ("All Files", "*.*")))
        if not filename:
            return False

        f = open(filename, 'r')
        Man.loaded = []
        key = f.readline().strip('\n')
        Man.importkey(key)
        lines = f.readlines()

        for i in range(0, len(lines)):
            lines[i] = lines[i].replace("\n", "")
            
            if i % 3 == 2:
                accountname = Man.decrypt(lines[i-2]).decode('utf-8')
                username = Man.decrypt(lines[i-1]).decode('utf-8')
                password = Man.decrypt(lines[i]).decode('utf-8')
                Man.loaded.append([accountname, username, password])

        f.close()
        return True