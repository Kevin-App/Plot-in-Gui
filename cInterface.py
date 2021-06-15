from tkinter import *
import tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

TEXT_WHITE_OFF = "#f0f0f0"
BACKGROUND_MAIN_GRAY = "#2e3233"
BACKGROUND_SUB_GRAY = "#242726"
MAIN_BLUE = "#324870"

#Class to create User-Interface with embedded matplotlib
class Interface:
    #CONSTRUCTOR
    def __init__(self) -> None:

        #Create a Window
        self.window = tkinter.Tk()

        #Create Layout
        self.__create_layout()

        #Creating Plot
        self.__create_plot()

        #Run Tkinter event loop
        self.window.mainloop()

    #Method to create Gui Layout
    #
    #IMPORTANT: DONT'T CHANGE ORDER OF THE FRAMES!
    def __create_layout(self):

        #Create main top menu bar
        self.menu_bar_top = tkinter.Frame(master=self.window,height=35, bg=BACKGROUND_MAIN_GRAY)
        self.menu_bar_top.pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=False)

        #Create main bottom menu bar
        self.status_bar_bottom = tkinter.Frame(master=self.window,height=25, bg=MAIN_BLUE)
        self.status_bar_bottom.pack(fill=tkinter.BOTH,side=tkinter.BOTTOM, expand=False)

        #Create left menu bar -> inputs for plot
        self.menu_bar_left = tkinter.Frame(master=self.window, width=150, bg=BACKGROUND_MAIN_GRAY)
        self.menu_bar_left.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=False)

        #Create bottom menu --> output text
        self.plot_bottom_menu = tkinter.Frame(master=self.window,height=100, bg=BACKGROUND_SUB_GRAY)
        self.plot_bottom_menu.pack(fill=tkinter.BOTH,side=tkinter.BOTTOM, expand=False)
        
        #Create left plot menu
        self.plot_left_menu = tkinter.Frame(master=self.window, width=50, bg=BACKGROUND_SUB_GRAY)
        self.plot_left_menu.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=False)

        #Create area for plot
        self.plot_center_area = tkinter.Frame(master=self.window)
        self.plot_center_area.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

        #Create right plot menu
        self.plot_right_menu = tkinter.Frame(master=self.window, width=50, bg=BACKGROUND_SUB_GRAY)
        self.plot_right_menu.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=False)

    #Method to create Plot
    def __create_plot(self):

        #Create Plot-Figure
        self.figure = Figure(figsize=(5, 4), dpi=100)

        #Create Axis
        self.axis = self.figure.add_subplot(1,1,1)

        #Change Backgorund Color
        self.figure.patch.set_facecolor(BACKGROUND_SUB_GRAY) #outside plot
        self.axis.set_facecolor(BACKGROUND_SUB_GRAY) #inside plot

        #Change Axis Color
        self.axis.spines['bottom'].set_color(TEXT_WHITE_OFF)
        self.axis.spines['top'].set_color(TEXT_WHITE_OFF)
        self.axis.spines['left'].set_color(TEXT_WHITE_OFF)
        self.axis.spines['right'].set_color(TEXT_WHITE_OFF)
        self.axis.tick_params(axis='x', colors=TEXT_WHITE_OFF)
        self.axis.tick_params(axis='y', colors=TEXT_WHITE_OFF)
        
        #Create Canvas to set Plot inside plot_center_area
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_center_area)

        #Draw Canvas
        self.canvas.draw()

        #Pack Canvas to Frame and make in Responsive
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)