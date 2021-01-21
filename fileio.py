import tkinter as tk
from tkinter import filedialog, Text
import os
import base64

class Fileio:

    def exportfile(self, Man):

        directory = filedialog.askdirectory(title="Export File")
        if not directory:
            return False

        encrypted = directory + "/encrypted.enc"
        key = directory + "/decoder.enc"

        f = open(encrypted, "w")
        for i in range(0, len(Man.loaded)):

            for j in range(0, 3):
                f.write(Man.encrypt(Man.loaded[i][j]).decode('utf-8'))
                f.write("\n")
        f.close()

        f = open(key, "w")
        f.write((Man.keytext.decode('utf-8'))[::-1])
        f.close()
        return True

    def importfile(self, Man):

        filename = filedialog.askopenfilename(initialdir="C:/Desktop/", title="Import Key (decoder.enc) File", filetypes=(("Encrypted Files", "*.enc"), ("All Files", "*.*")))
        if not filename:
            return False

        f = open(filename, 'r')
        key = f.readline().strip('\n')
        key = key[::-1]
        Man.importkey(key)
        f.close()

        filename = filedialog.askopenfilename(initialdir="C:/Desktop/", title="Import Password (encrypted.enc) File", filetypes=(("Encrypted Files", "*.enc"), ("All Files", "*.*")))
        if not filename:
            return False

        f = open(filename, 'r')
        Man.loaded = []
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