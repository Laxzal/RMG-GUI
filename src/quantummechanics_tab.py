import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import customtkinter as ctk

class quantumMechanics(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Create 7 frames
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

        # Create a tick box in gui to use Quantum Mechanics
        self.use_quantum_mechanics = tk.BooleanVar()
        self.use_quantum_mechanics.set(0)
        self.use_quantum_mechanics_check = tk.Checkbutton(self.frame0, text="Use Quantum Mechanics", variable=self.use_quantum_mechanics)
        self.use_quantum_mechanics_check.grid(row=0, column=0, padx=5, pady=5)

        # Create a lable and entry for software
        self.software_label = tk.Label(self.frame1, text='Software:')
        self.software_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.software_entry = tk.Entry(self.frame1, width=10)
        self.software_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Create a label and entry for method
        self.method_label = tk.Label(self.frame2, text='Method:')
        self.method_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.method_entry = tk.Entry(self.frame2, width=10)
        self.method_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Ceate a file store label and entry
        self.file_store_label = tk.Label(self.frame3, text='File Store:')
        self.file_store_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.file_store_entry = tk.Entry(self.frame3, width=10)
        self.file_store_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        #Create a button to open a file dialog that gets the path of the folder
        self.folder_store_label = tk.Label(self.frame4, text='Folder Store:')
        self.folder_store_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.folder_store_button = tk.Button(self.frame4, text='ScratchDirectory', command=self.get_folder_path)
        self.folder_store_button.grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.folder_store_entry = tk.Entry(self.frame4, width=30)
        self.folder_store_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Create a lable for OnlyCyclics and a dropdown with '' and 'True and 'False'
        self.only_cyclics_label = tk.Label(self.frame5, text='Only Cyclics:')
        self.only_cyclics_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.only_cyclics_dropdown = ttk.Combobox(self.frame5, values=['', 'True', 'False'])
        self.only_cyclics_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Create a maxRadicalNumber label and entry
        self.max_radical_number_label = tk.Label(self.frame6, text='Max Radical Number:')
        self.max_radical_number_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.max_radical_number_entry = tk.Entry(self.frame6, width=10)
        self.max_radical_number_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        




    def get_folder_path(self):
        self.foldername = filedialog.askdirectory(title="Select Folder to Save Files")
        self.folder_store_entry.insert(0, self.foldername)
        #self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
        #self.file_store_entry.insert(0, self.filename)
    
    def generate_qmech(self):
        
        if self.use_quantum_mechanics.get() == 1:
            # Get all the values
            self.software_value = self.software_entry.get()
            self.method_value = self.method_entry.get()
            self.file_store_value = self.file_store_entry.get()
            self.scratch_dictory_value = self.folder_store_entry.get()
            self.only_cyclics_value = self.only_cyclics_dropdown.get()
            self.max_radical_number_value = self.max_radical_number_entry.get()
            
            # Return a dictionary with all the values
            return {'software': self.software_value, 
                    'method': self.method_value, 
                    'fileStore': self.file_store_value, 
                    'scratchDirectory': self.scratch_dictory_value, 
                    'onlyCyclics': self.only_cyclics_value, 
                    'maxRadicalNumber': self.max_radical_number_value}
        else:
            return None