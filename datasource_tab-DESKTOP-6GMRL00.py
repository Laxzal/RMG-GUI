import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

class DataSources(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        def clear(): return
        self.options = ["primaryThermoLibrary","DFT_QCI_thermo","GRI-Mech3.0","CBS_QB3_1dHR","thermo_DFT_CCSDTF12_BAC","SABIC_aromatics","C3","Fulvene_H","BurkeH2O2","Chlorinated_Hydrocarbons","heavy_oil_ccsdtf12_1dHR","Narayanaswamy","CHN","CHOFClBr_G4","vinylCPD_H","CHOFBr_G4","CHOClBr_G4","SABIC_aromatics_1dHR","SulfurGlarborgH2S","CHOFCl_G4","naphthalene_H","s3_5_7_ane","NOx2018","iodinated_Hydrocarbons","JetSurF1.0","SulfurGlarborgMarshall","SABIC_aromatics_1dHR_extended","CH","NitrogenCurran","CHO","bio_oil","2-BTP","SulfurLibrary","CHOCl_G4","C10H11","CHON_G4","Klippenstein_Glarborg2016","2-BTP_G4","primaryNS","CurranPentane","halogens","USC-Mech-ii","GRI-Mech3.0-N","Fluorine","JetSurF2.0","FFCM1(-)","Chlorination","SulfurGlarborgNS","CHOBr_G4","surfaceThermoNi111","surfaceThermoPt111","NISTThermoLibrary","Lai_Hexylbenzene","SulfurHaynes","CN","BurcatNS","SulfurGlarborgBozzelli","Chernov","Spiekermann_refining_elementary_reactions","CHOF_G4","CHON"]
        select = unselect = done = enter = clear
        self.selected = []
        self.not_selected = list(self.options)
        
        # lf = ttk.LabelFrame(parent, text="Select options:")
        # lf.grid(column=0, row=0, padx=20, pady=20)
        
        # self.selected_listbox = tk.Listbox(lf, selectmode=tk.MULTIPLE)
        # self.selected_listbox.grid(column=2, row=0, padx=10, pady=10)
        # self.selected_listbox.config(width=30, height=20)
        
        # self.not_selected_listbox = tk.Listbox(lf, selectmode=tk.MULTIPLE)
        # self.not_selected_listbox.grid(column=0, row=0, padx=10, pady=10)
        # self.not_selected_listbox.config(width=30, height=20)
        
        # midpoint = (self.selected_listbox.grid_info()['row'] + self.not_selected_listbox.grid_info()['row']) // 2
        
        # self.add_button = tk.Button(lf, text='Add >>', command=self.add_selected)
        # self.add_button.grid(column=1, row=midpoint, padx=2, sticky='EW', rowspan=2)

        # self.remove_button = tk.Button(lf, text='<< Remove', command=self.remove_selected)
        # self.remove_button.grid(column=1, row=midpoint+1, padx=2,sticky='EW', rowspan=2)
        
        
        frame0 = ttk.Frame(parent)
        frame0.grid(row=0, column=0, sticky='WE', padx=5, pady=5, columnspan=3)
        frame0.grid_columnconfigure(0, weight=1)
        lblentry = ttk.Label(frame0, text="Entry Box:")
        lblentry.grid(row=0, column=0, sticky='W')
        entrybx = ttk.Entry(frame0)
        entrybx.grid(row=1, column=0, sticky='NSEW', columnspan=2)
        entrybt = ttk.Button(frame0, text=' Enter ', command=enter)
        entrybt.grid(row=1, column=2, sticky='NW', padx=3)
        
        
        frame1 = ttk.Frame(parent)
        frame1.grid(row=1, column=0, sticky='EW', padx=5, pady=5)
        lblshow_lst = ttk.Label(frame1, text="List Box 1:")
        lblshow_lst.grid(row=0, sticky='W')
        self.not_selected_listbox = ttk.Listbox(frame1)
        self.not_selected_listbox.grid(row=1, sticky='W')
        
        
        frame2 = ttk.Frame(pa)
        frame2.grid(row=1, column=1, sticky='W')
        selbtn = ttk.Button(frame2, text='Select', command=self.add_selectedselect)
        selbtn.grid(row=0, padx=5, sticky='EW')
        uselbtn = Button(frame2, text='Unselect', command=self.remove_selected)
        uselbtn.grid(row=1, padx=5, sticky='EW')
        
        self.update_lists()

    def update_lists(self):
        self.selected_listbox.delete(0, tk.END)
        for item in self.selected:
            self.selected_listbox.insert(tk.END, item)
            
        self.not_selected_listbox.delete(0, tk.END)
        for item in self.not_selected:
            self.not_selected_listbox.insert(tk.END, item)

    def add_selected(self):
        selected_items = self.not_selected_listbox.curselection()
        selected_items = [self.not_selected[index] for index in selected_items]
        for item in selected_items:
            self.selected.append(item)
            self.not_selected.remove(item)
        self.update_lists()

    def remove_selected(self):
        selected_items = self.selected_listbox.curselection()
        selected_items = [self.selected[index] for index in selected_items]
        for item in selected_items:
            self.not_selected.append(item)
            self.selected.remove(item)
        self.update_lists()