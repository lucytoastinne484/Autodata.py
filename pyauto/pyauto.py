import pyautogui as pyauto
import runpy as run
import pathlib as lib
import pathspec as spec
import tkinter as tk
import pandas as pd
import csv as comma
from matplotlib import matplotlib_fname as mat_fn
import matplotlib as plot
from matplotlib import warnings as alerts
import PyQt5 as pyqt
import time as clock



    
    

class Autodata:
    def __init__(self):
        pass
    def load_excel():#launches excel
        with pyauto.hold('win'):
            pyauto.press(['r'])
            
        pyauto.press(['backspace'])
        pyauto.write('excel.exe')
        pyauto.press(['enter'])
    def load_app(self,app_name):
        with pyauto.hold('win'):
            pyauto.press(['r'])
            
        pyauto.press(['backspace'])
        pyauto.write(app_name)
        pyauto.press(['enter'])
        
    def load_sheet(path):
        path = path
        with pyauto.hold('win'):
            pyauto.press(['r'])
            
        pyauto.press(['backspace'])
        pyauto.write(path)
        pyauto.press(['enter'])
        
    def Input_data(name,tel,cell,email,website,sm,sector):#input data for contact
        #sm stands for Social Medias#
        name = name + ","
        pyauto.write(name)
        tel = tel + ","
        pyauto.write(tel)
        cell = cell + ","
        pyauto.write(cell)
        email = email + ","
        pyauto.write(email)
        website = website + ","
        pyauto.write(website)
        sm = sm + ","
        pyauto.write(sm)
        sector = sector + ","
        pyauto.write(sector)
        pyauto.press(['enter'],presses=1)
        
    def control_painel(self):#launches the control painel 
        painel = tk()
        upgrade = pyqt()
    def get_location(self):#get the location to 
        pos = pyauto.position()
        print(pos)
    def recalibrate(self,x,y):
        x = x
        y = y
        pyauto.moveTo(x,y)
    def click(self,turns):
        pyauto.click(clicks=turns)
        
    def keyboard(self,key,turns):
        pyauto.press([key],presses=turns)
        
    
        
        



   
Autodata.load_sheet(r"C:\Program Files\Krita (x64)\bin\krita.exe")












#Autodata.load_sheet(r"C:\Users\Computador\oteropython\pyauto\data_test\data.csv")
