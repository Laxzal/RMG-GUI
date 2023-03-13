import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
class thermoDatabase(ctk.CTkFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master)
        
        # Create a frame for the thermo database
        self.frame0 = ctk.CTkFrame(self)
        self.frame0.grid(row=0, column=0, sticky='nsew')
        
        
        # Create a heading of unselected and selected thermo databases
        self.heading = ctk.CTkLabel(self.frame0, text='Thermo Database')
        self.heading.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        self.left_heading = ctk.CTkLabel(self.frame0, text='Unselected')
        self.left_heading.grid(row=2, column=0, padx=5, pady=5)
        self.right_heading = ctk.CTkLabel(self.frame0, text='Selected')
        self.right_heading.grid(row=2, column=2, padx=5, pady=5)
        
        # Create an entry box to search for thermo database
        self.search_thermo = ctk.CTkEntry(self.frame0, width=30, placeholder_text='Search thermo library', placeholder_text_color='grey')
        self.search_thermo.grid(row=1, column=0, padx=5, pady=5, columnspan=1, sticky='ew')
        self.search_thermo.bind('<KeyRelease>', self.search_thermo_database)
        self.search_thermo.bind('<Return>', self.search_thermo_database)
        
        #Create pair of listboxes
        self.left_listbox = tk.Listbox(self.frame0, width=30, height=10, selectmode=tk.EXTENDED)
        self.left_listbox.grid(row=3, column=0, padx=5, pady=5, rowspan=2)
        self.right_listbox = tk.Listbox(self.frame0, width=30, height=10, selectmode=tk.EXTENDED)
        self.right_listbox.grid(row=3, column=2, padx=5, pady=5, rowspan=2)
        
        # insert items into listbox
        self.options_thermo = ["primaryThermoLibrary","DFT_QCI_thermo","GRI-Mech3.0",
                               "CBS_QB3_1dHR","thermo_DFT_CCSDTF12_BAC","SABIC_aromatics",
                               "C3","Fulvene_H","BurkeH2O2","Chlorinated_Hydrocarbons",
                               "heavy_oil_ccsdtf12_1dHR","Narayanaswamy","CHN","CHOFClBr_G4",
                               "vinylCPD_H","CHOFBr_G4","CHOClBr_G4","SABIC_aromatics_1dHR",
                               "SulfurGlarborgH2S","CHOFCl_G4","naphthalene_H","s3_5_7_ane",
                               "NOx2018","iodinated_Hydrocarbons","JetSurF1.0",
                               "SulfurGlarborgMarshall","SABIC_aromatics_1dHR_extended",
                               "CH","NitrogenCurran","CHO","bio_oil","2-BTP","SulfurLibrary",
                               "CHOCl_G4","C10H11","CHON_G4","Klippenstein_Glarborg2016",
                               "2-BTP_G4","primaryNS","CurranPentane","halogens","USC-Mech-ii",
                               "GRI-Mech3.0-N","Fluorine","JetSurF2.0","FFCM1(-)","Chlorination",
                               "SulfurGlarborgNS","CHOBr_G4","surfaceThermoNi111","surfaceThermoPt111",
                               "NISTThermoLibrary","Lai_Hexylbenzene","SulfurHaynes","CN","BurcatNS",
                               "SulfurGlarborgBozzelli","Chernov","Spiekermann_refining_elementary_reactions",
                               "CHOF_G4","CHON"]
        self.original_index = { item: index for index, item in enumerate(self.options_thermo)}
        self.selected_items = []
        self.unselected_items = list(self.options_thermo)
        for item in self.unselected_items:
            self.left_listbox.insert("end", item)
        
        
        # Create buttons to move items between listboxes
        self.thermo_button_add = ctk.CTkButton(self.frame0, text='>>', command=lambda: self.move_items(self.left_listbox, self.right_listbox))
        self.thermo_button_add.grid(row=3, column=1, padx=5, pady=5)
        self.thermo_button_remove = ctk.CTkButton(self.frame0, text='<<', command=lambda: self.move_items(self.right_listbox, self.left_listbox))
        self.thermo_button_remove.grid(row=4, column=1, padx=5, pady=5)
        
        # Create an entry box that allows for user to input thermo database
        self.thermo_database = ctk.CTkEntry(self.frame0, width=30, placeholder_text='Enter custom thermo library', placeholder_text_color='grey')
        self.thermo_database.grid(row=1, column=2, padx=5, pady=5, columnspan=1, sticky='ew')
        self.thermo_database_button = ctk.CTkButton(self.frame0, text='Enter', command=lambda: self.add_thermo_database(self.thermo_database.get()))
        self.thermo_database_button.grid(row=1, column=3, padx=5, pady=5)
        
    
    
    # Define a function to move items between Listboxes
    def move_items(self,left_listbox, right_listbox):
        selected_indices = left_listbox.curselection()
        for index in reversed(selected_indices):
            try:
                o_idx = self.original_index[left_listbox.get(index)]
                right_listbox.insert(o_idx, left_listbox.get(index))
            except KeyError:
                right_listbox.insert("end", left_listbox.get(index))
            left_listbox.delete(index)
    
    # Define a function to search for thermo database
    def search_thermo_database(self, event):
        search_term = self.search_thermo.get()
        self.left_listbox.delete(0, "end")
        for item in self.unselected_items:
            if search_term.lower() in item.lower():
                self.left_listbox.insert("end", item)
            
    # Define a function to add thermo database
    def add_thermo_database(self, thermo_database):
        #self.unselected_items.append(thermo_database)
        self.right_listbox.insert("end", thermo_database)        
        

