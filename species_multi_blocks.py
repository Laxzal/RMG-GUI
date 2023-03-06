import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        #self.master.title('Species File Generator')
        self.label = tk.Label(self, text="Species Generator")
        self.label.pack(pady=5, padx=5)

        # create dropdown menu to select number of species blocks
        num_species_menu_label = tk.Label(self.master, text='Number of Species Blocks:')
        num_species_menu_label.grid(row=0, column=0)
        num_species_menu = ttk.Combobox(self.master, width=2, textvariable=self.num_species_blocks, state='readonly')
        num_species_menu.grid(row=0, column=1)
        num_species_menu['values'] = ('1', '2', '3', '4', '5')
        num_species_menu.bind('<<ComboboxSelected>>', self.on_select)
        num_species_menu.current(0)
        
        # create button to generate file
        generate_button = tk.Button(self.master, text='Generate', command=self.generate_file)
        generate_button.grid(row=10, column=6, columnspan=2, pady=10)
        
        # create list to store species blocks
        self.species_blocks = []
        self.species_labels_blocks = []
        self.species_checks = []
        self.on_select()

    def on_select(self, event=None):
        # clear existing species blocks
        for block in self.species_blocks:
            block.destroy()
        self.species_blocks = []
        self.species_checks = []
        
        for block in self.species_labels_blocks:
            block.destroy()
        self.species_labels_blocks = []
        
        # create new species blocks
        num_blocks = int(self.num_species_blocks.get())
        for i in range(num_blocks):
            species_label = tk.Label(self.master, text=f'Species {i+1}:')
            species_label.grid(row=i+2, column=0, padx=5, pady=5, sticky='e')
            species_label_entry = tk.Entry(self.master, width=50)
            species_label_entry.grid(row=i+2, column=1, padx=5, pady=5, sticky='w')
            
            species_smiles = tk.Label(self.master, text=f'SMILES {i+1}:')
            species_smiles.grid(row=i+2, column=3, padx=5, pady=5)
            species_smiles_entry = tk.Entry(self.master, width=50)
            species_smiles_entry.grid(row=i+2, column=4, padx=5, pady=5, sticky='w')

            reactive_var = tk.BooleanVar()
            reactive_var.set(0)
            reactive_check = tk.Checkbutton(self.master, text="Reactive", variable=reactive_var)
            reactive_check.grid(row=i+2, column=5, padx=5, pady=5)

            self.species_blocks.append(species_label_entry)
            self.species_blocks.append(species_smiles_entry)
            self.species_checks.append(reactive_var)
            self.species_labels_blocks.append(species_label)
            self.species_labels_blocks.append(species_smiles)
            self.species_labels_blocks.append(reactive_check)
    
    def generate_file(self):
        # create list of species SMILES from user input
        species_label = []
        species_smiles = []
        species_reactive = []
        for i in range(0, len(self.species_blocks), 2):
            species_label.append(self.species_blocks[i].get())
            species_smiles.append(self.species_blocks[i+1].get())
        for i in range(0, len(self.species_checks)):
            species_reactive.append(self.species_checks[i].get())

        # create file contents
        file_contents = f"species(\n    label='{species_label[0]}',\n    reactive={species_reactive[0]},\n    structure=SMILES('{species_smiles[0]}'),\n)\n\n"
        if len(species_smiles) > 1:
            for i in range(1, len(species_smiles)):
                file_contents += f"species(\n    label='{species_label[i]}',\n    reactive={species_reactive[i]},\n    structure=SMILES('{species_smiles[i]}'),\n)\n\n"
            
        # open file dialog to choose save location and name
        file_path = filedialog.asksaveasfilename(defaultextension='.py', filetypes=[('Python Files', '*.py')])
        if not file_path:
            return
        # write file
        with open(file_path, 'w') as f:
            f.write(file_contents)
            
        
        # show success message
        success_label = tk.Label(self.master, text='File saved successfully!', fg='green')
        success_label.grid(row=len(self.species_blocks+self.species_checks)+2, column=0, columnspan=2, pady=10)


class Tab2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Tab 2")
        self.label.pack(pady=10, padx=10)

class Tab3(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Tab 3")
        self.label.pack(pady=10, padx=10)

# root = tk.Tk()
# app = App(root)
# root.mainloop()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Tab Application")
        self.geometry("1900x900")
        
        custom_style = ttk.Style()
        custom_style.configure("CustomNotebook.TNotebook", tabposition="wn", tabmargins=[10, 10, 10, 0])
        custom_style.configure("CustomNotebook.TNotebook.Tab", padding=[5, 5], font=("Helvetica", 14), foreground="#555", background="#ccc")

        # Create a notebook widget
        self.notebook = ttk.Notebook(self, style="CustomNotebook.TNotebook")
        self.notebook.pack(fill="both", expand=True)

        # Create tabs and add them to the notebook
        # create species generator tab
        self.species_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.species_tab, text='Species Generator')
        self.app = App(self.species_tab)
        
        #self.app.pack(fill='both', expand=True)
        
        self.tab2 = Tab2(self.notebook)
        self.tab3 = Tab3(self.notebook)

        self.notebook.add(self.tab2, text="Tab 2")
        self.notebook.add(self.tab3, text="Tab 3")



if __name__ == "__main__":
    app = Application()
    app.mainloop()