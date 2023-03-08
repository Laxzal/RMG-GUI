import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from species_tab import Species as Tab1
from tab2_dummy import Tab2 as Tab2
from datasource_tab import ThermoSources, ReactionSources

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1900x900")

        self.title("My App")
        
        custom_style = ttk.Style()
        custom_style.configure("CustomNotebook.TNotebook", tabposition="wn", tabmargins=[10, 10, 10, 0])
        custom_style.configure("CustomNotebook.TNotebook.Tab", padding=[5, 5], font=("Helvetica", 14), foreground="#555", background="#ccc")

        # Create a notebook widget
        self.notebook = ttk.Notebook(self, style="CustomNotebook.TNotebook")
        self.notebook.pack(fill="both", expand=True)

        
        self.datasources_tab = ttk.Frame(self.notebook)
        self.species_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.datasources_tab, text="DataSources")
        self.notebook.add(self.species_tab, text='Species Generator')

        
        self.thermo_sources = ThermoSources(self.datasources_tab)
        self.thermo_sources.grid(row=0, column=0)
        #self.reaction_sources = ReactionSources(self.datasources_tab)
        #self.reaction_sources.grid(row=0, column=10)
        
        
  
        self.tab1 = Tab1(self.species_tab)
        tab2 = Tab2(self.notebook, self.tab1)

        self.notebook.add(tab2, text="Tab 2")
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()