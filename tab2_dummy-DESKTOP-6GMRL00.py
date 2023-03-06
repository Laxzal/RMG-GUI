import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Tab2(tk.Frame):
    def __init__(self, parent, tab1):
        super().__init__(parent)
        
        self.email_label = tk.Label(self, text="Enter your email:")
        self.email_label.pack()
        
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()
        
        self.generate_button = tk.Button(self, text="Generate output file", command=self.generate_file)
        self.generate_button.pack()
        self.tab1 = tab1
        
    def email_noinput_error(self):
        if not self.email_entry.get():
            messagebox.showerror("Error", "Please enter your email address")
            return False
        return self.email_entry.get()
    
    def generate_file(self):
        
        name = self.tab1.spec_noinput_error()
        email = self.email_noinput_error()

        
        
        if email and name:
            # create list of species SMILES from user input
            species_label = []
            species_smiles = []
            species_reactive = []
            for i in range(0, len(self.species_blocks), 2):
                species_label.append(self.species_blocks[i].get())
                species_smiles.append(self.species_blocks[i+1].get())
            for i in range(0, len(self.species_checks)):
                species_reactive.append(self.species_checks[i].get())
            
            # create file contents SPECIES
            file_content_species = f"species(\n    label='{species_label[0]}',\n    reactive={species_reactive[0]},\n    structure=SMILES('{species_smiles[0]}'),\n)\n\n"
            if len(species_smiles) > 1:
                for i in range(1, len(species_smiles)):
                    file_content_species += f"species(\n    label='{species_label[i]}',\n    reactive={species_reactive[i]},\n    structure=SMILES('{species_smiles[i]}'),\n)\n\n"
            
                    file_path = filedialog.asksaveasfilename(defaultextension='.py', filetypes=[('Python Files', '*.py')])
            if not file_path:
                return
            # write file
            with open(file_path, 'w') as f:
                f.write(file_contents)
