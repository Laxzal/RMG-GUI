import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import customtkinter as ctk


class restartFromSeedMechanism(ctk.CTkFrame):
    
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        # Create 5 frames
        self.frame0 = ttk.Frame(self.master)
        self.frame0.grid(row=0, column=0, sticky='nsew')
        self.frame1 = ttk.Frame(self.master)
        self.frame1.grid(row=1, column=0, sticky='nsew')
        self.frame2 = ttk.Frame(self.master)
        self.frame2.grid(row=2, column=0, sticky='nsew')
        self.frame3 = ttk.Frame(self.master)
        self.frame3.grid(row=3, column=0, sticky='nsew')
        self.frame4 = ttk.Frame(self.master)
        self.frame4.grid(row=4, column=0, sticky='nsew')
        self.frame5 = ttk.Frame(self.master)
        self.frame5.grid(row=5, column=0, sticky='nsew')
        self.frame6 = ttk.Frame(self.master)
        self.frame6.grid(row=6, column=0, sticky='nsew')
        
        # Create a tick box to enable/disable the mechanism
        self.restart_seed_var = tk.BooleanVar()
        self.restart_seed_var.set(False)
        self.restart_seed_checkbutton = ttk.Checkbutton(self.frame0, text='Restart from seed', variable=self.restart_seed_var)
        self.restart_seed_checkbutton.grid(row=0, column=0, sticky='w')
        
        # Create a label called path, an entry box and a button that opens the folder browser and puts the folder string in the entry box
        self.path_label = ttk.Label(self.frame1, text='Path Seed')
        self.path_label.grid(row=0, column=0, sticky='w')
        self.path_entry = ttk.Entry(self.frame1, width=50)
        self.path_entry.grid(row=0, column=1, sticky='ew')
        self.path_browse_button = ttk.Button(self.frame1, text='Seed Path', command=lambda :self.get_folder_path(event=self.path_entry))
        self.path_browse_button.grid(row=0, column=2, sticky='ew')
        
        # Create a label that tells the user that if Path Seed path is not specified, the paths below must be specified and will be use
        self.information_label = ttk.Label(self.frame2, text='If Path Seed is not specified, the paths below must be specified and will be used',  font='Helvetica 12 bold')
        self.information_label.grid(row=0, column=0, sticky='w')
        self.informtion_separator = ttk.Separator(self.frame2, orient='horizontal' )
        self.informtion_separator.grid(row=1, column=0, sticky='ew', pady=5, padx=5, columnspan=3, ipadx=100)
        
        # Create a label called get coreSeed and an entry box and a button that opens the folder browser and puts the folder string in the entry box
        self.coreseed_label = ttk.Label(self.frame3, text='Core Seed')
        self.coreseed_label.grid(row=0, column=0, sticky='w')
        self.coreseed_entry = ttk.Entry(self.frame3, width=50)
        self.coreseed_entry.grid(row=0, column=1, sticky='ew')
        self.coreseed_browser_button = ttk.Button(self.frame3, text='Core Seed', command= lambda :self.get_folder_path(event=self.coreseed_entry), )
        self.coreseed_browser_button.grid(row=0, column=2, sticky='ew')
        
        # Create a label called edge speed and an entry box and a button that opens the folder browser and puts the folder string in the entry box
        self.edge_speed_label = ttk.Label(self.frame4, text='Edge Seed')
        self.edge_speed_label.grid(row=0, column=0, sticky='w')
        self.edge_speed_entry = ttk.Entry(self.frame4, width=50)
        self.edge_speed_entry.grid(row=0, column=1, sticky='ew')
        self.edge_speed_browser_button = ttk.Button(self.frame4, text='Edge Seed', command= lambda :self.get_folder_path(event=self.edge_speed_entry), )
        self.edge_speed_browser_button.grid(row=0, column=2, sticky='ew')
        
        
        # Create a label called filters and an entry box and a button that opens the file browser and puts the file string in the entry box
        self.filters_label = ttk.Label(self.frame5, text='Filters')
        self.filters_label.grid(row=0, column=0, sticky='w')
        self.filters_entry = ttk.Entry(self.frame5, width=50)
        self.filters_entry.grid(row=0, column=1, sticky='ew')
        self.filters_button = ttk.Button(self.frame5, text='Filters', command= lambda :self.get_filter_path(event=self.filters_entry) )
        self.filters_button.grid(row=0, column=2, sticky='ew')
        
        # Create a label called species map and an entry box and a button that opens the file browser and puts the file string in the entry box
        self.species_map_label = ttk.Label(self.frame6, text='Species Map')
        self.species_map_label.grid(row=0, column=0, sticky='w')
        self.species_map_entry = ttk.Entry(self.frame6, width=50)
        self.species_map_entry.grid(row=0, column=1, sticky='ew')
        self.species_map_button = ttk.Button(self.frame6, text='Species Map', command= lambda :self.get_species_map_path(event=self.species_map_entry) )
        self.species_map_button.grid(row=0, column=2, sticky='ew')
        
    def get_folder_path(self,event=None):
        self.foldername = filedialog.askdirectory(title="Select Folder for Seed Files")
        event.insert(0, self.foldername)
        #self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
        #self.file_store_entry.insert(0, self.filename)
    def get_filter_path(self,event=None):
        self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("h5 files","*.h5"),("all files","*.*")))
        event.insert(0, self.filename)

    def get_species_map_path(self, event=None):
        self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("yml files","*.yml"),("all files","*.*")))
        event.insert(0, self.filename)