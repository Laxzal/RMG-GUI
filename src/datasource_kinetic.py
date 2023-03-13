import customtkinter as ctk
import tkinter as tk
from tkinter import ttk




class kineticDatabase(ctk.CTkFrame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        
        # Create a frame for the kinetic database
        self.frame_kinetic = ctk.CTkFrame(self)
        self.frame_kinetic.grid(row=0, column=0, sticky='nsew')
        
        
        # Create a heading of unselected and selected kinetic databases
        self.heading = ctk.CTkLabel(self.frame_kinetic, text='Kinetic Database')
        self.heading.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        self.left_heading = ctk.CTkLabel(self.frame_kinetic, text='Unselected')
        self.left_heading.grid(row=2, column=0, padx=5, pady=5)
        self.right_heading = ctk.CTkLabel(self.frame_kinetic, text='Selected')
        self.right_heading.grid(row=2, column=2, padx=5, pady=5)
        
        # Create an entry box to search for kinetic database
        self.search_kinetic = ctk.CTkEntry(self.frame_kinetic, width=30, placeholder_text='Search kinetic library', placeholder_text_color='grey')
        self.search_kinetic.grid(row=1, column=0, padx=5, pady=5, columnspan=1, sticky='ew')
        self.search_kinetic.bind('<KeyRelease>', self.search_kinetic_database)
        self.search_kinetic.bind('<Return>', self.search_kinetic_database)
        
        #Create pair of listboxes
        self.left_listbox = tk.Listbox(self.frame_kinetic, width=30, height=10, selectmode=tk.EXTENDED)
        self.left_listbox.grid(row=3, column=0, padx=5, pady=5, rowspan=2)
        self.right_listbox = tk.Listbox(self.frame_kinetic, width=30, height=10, selectmode=tk.EXTENDED)
        self.right_listbox.grid(row=3, column=2, padx=5, pady=5, rowspan=2)
        
        # insert items into listbox
        self.options_kinetic =  ['1989_Stewart_2CH3_to_C2H5_H', '2-BTP/full', '2-BTP/seed', 
                                '2001_Tokmakov_H_Toluene_to_CH3_Benzene', 
                                '2003_Miller_Propargyl_Recomb_High_P', 
                                '2005_Senosiain_OH_C2H2', '2006_Joshi_OH_CO', 
                                '2009_Sharma_C5H5_CH3_highP', '2015_Buras_C2H3_C4H6_highP', 
                                'Aromatics_high_pressure/C10H10_1', 
                                'Aromatics_high_pressure/C10H10_2', 
                                'Aromatics_high_pressure/C10H10_H_abstraction', 
                                'Aromatics_high_pressure/C10H11_1', 
                                'Aromatics_high_pressure/C10H11_2', 
                                'Aromatics_high_pressure/C10H11_3', 
                                'Aromatics_high_pressure/C10H11_4', 
                                'Aromatics_high_pressure/C10H7', 
                                'Aromatics_high_pressure/C10H8_H_abstraction_H_recomb',
                                'Aromatics_high_pressure/C10H9_1', 
                                'Aromatics_high_pressure/C10H9_2', 
                                'Aromatics_high_pressure/C10H9_3', 
                                'Aromatics_high_pressure/C10H9_4', 'Aromatics_high_pressure/C12H10_1', 
                                'Aromatics_high_pressure/C12H10_2', 'Aromatics_high_pressure/C12H10_H_abstraction', 
                                'Aromatics_high_pressure/C12H11', 'Aromatics_high_pressure/C12H8_H_abstraction', 
                                'Aromatics_high_pressure/C12H9', 'Aromatics_high_pressure/C14H10_H_abstraction_H_recomb', 
                                'Aromatics_high_pressure/C14H11_1', 'Aromatics_high_pressure/C14H11_2', 'Aromatics_high_pressure/C14H11_3', 
                                'Aromatics_high_pressure/C14H11_4', 'Aromatics_high_pressure/C14H9', 'Aromatics_high_pressure/C16H11', 
                                'Aromatics_high_pressure/C7H8', 'Aromatics_high_pressure/C7H8_H_abstraction', 'Aromatics_high_pressure/C7H9', 
                                'Aromatics_high_pressure/C8H5O2_H_abstraction', 'Aromatics_high_pressure/C8H5O2_oxid_CO', 
                                'Aromatics_high_pressure/C8H5O2_oxid_CO2', 'Aromatics_high_pressure/C8H6_1', 'Aromatics_high_pressure/C8H6_2', 
                                'Aromatics_high_pressure/C8H6_H_abstraction', 'Aromatics_high_pressure/C8H7_1', 'Aromatics_high_pressure/C8H7_2', 
                                'Aromatics_high_pressure/C8H7_3', 'Aromatics_high_pressure/C8H7_H_abstraction', 'Aromatics_high_pressure/C8H8', 
                                'Aromatics_high_pressure/C9H5_H_abstraction', 'Aromatics_high_pressure/C9H5_oxid_CO', 'Aromatics_high_pressure/C9H5_oxid_CO2', 
                                'Aromatics_high_pressure/C9H6_1', 'Aromatics_high_pressure/C9H6_2', 'Aromatics_high_pressure/C9H6_H_abstraction', 
                                'Aromatics_high_pressure/C9H7',    "Aromatics_high_pressure/C9H8_1",
                                "Aromatics_high_pressure/C9H8_2",
                                "Aromatics_high_pressure/C9H8_H_abstraction",
                                "Aromatics_high_pressure/C9H9_1",
                                "Aromatics_high_pressure/C9H9_2",
                                "BurkeH2O2inArHe","BurkeH2O2inN2","C10H11","C12H11_pdep","C2H2_init","C2H4+O_Klipp2017","C3","C6H5_C4H4_Mebel","CF2BrCl","CH3Cl",
                                "Chernov","CurranPentane","DMSOxy","DTU_mech_CH3Cl","Dooley/C1","Dooley/methylformate","Dooley/methylformate_2",
                                "Dooley/methylformate_all_ARHEbathgas","Dooley/methylformate_all_N2bathgas","ERC-FoundationFuelv0.9",
                                "Ethylamine","FFCM1(-)","First_to_Second_Aromatic_Ring/2005_Ismail_C6H5_C4H6_highP","First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP","First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP",
                                "First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP","First_to_Second_Aromatic_Ring/2016_Mebel_Indene_CH3_highP","First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP","First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP",
                                "First_to_Second_Aromatic_Ring/2017_Mebel_C6H5C2H2_C2H2_highP","First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C2H2_highP","First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP","First_to_Second_Aromatic_Ring/phenyl_diacetylene_effective",'Fulvene_H', 
                                'GRI-HCO', 'GRI-Mech3.0', 'GRI-Mech3.0-N', 'Glarborg/C0', 'Glarborg/C1', 'Glarborg/C2', 'Glarborg/C3', 'Glarborg/highP', 'HydrazinePDep', 'Iodine-R_recombination', 'JetSurF1.0', 'JetSurF2.0', 'Klippenstein_Glarborg2016', 'Lai_Hexylbenzene', 'Mebel_C6H5_C2H2', 'Mebel_Naphthyl', 'Methylformate', 'N-S_interactions', 
                                'NIST_Fluorine/CH2F2/full', 'NIST_Fluorine/CH2F2/seed', 'NIST_Fluorine/full', 'NIST_Fluorine/seed', 'NOx2018', 'Narayanaswamy', 'Nitrogen_Dean_and_Bozzelli', 'Nitrogen_Glarborg_Gimenez_et_al', 'Nitrogen_Glarborg_Lucassen_et_al', 'Nitrogen_Glarborg_Zhang_et_al', 'Sulfur/DMDS', 'Sulfur/DMS', 'Sulfur/DTBS', 'Sulfur/GlarborgBozzelli', 
                                'Sulfur/GlarborgH2S', 'Sulfur/GlarborgH2S/alt', 'Sulfur/GlarborgMarshall', 'Sulfur/GlarborgNS', 'Sulfur/HSSH_1bar', 'Sulfur/Hexanethial_nr', 'Sulfur/Sendt', 'Sulfur/TP_Song', 'Sulfur/Thial_Hydrolysis', 'Surface/Ammonia/Duan_Ni111', 'Surface/Ammonia/Duan_Ni211', 'Surface/Ammonia/Kraehnert_Pt111', 'Surface/Ammonia/Novell_Pd111', 'Surface/Ammonia/Novell_Pt111', 
                                'Surface/Ammonia/Novell_Rh111', 'Surface/Ammonia/Offermans_Pt111', 'Surface/Ammonia/Popa_Rh111', 'Surface/Ammonia/Rebrov_Pt111', 'Surface/Ammonia/Roldan_Ru0001', 'Surface/Ammonia/Scheuer_Pt', 'Surface/Ammonia/Schneider_Pd111', 'Surface/Ammonia/Schneider_Pd211', 'Surface/Ammonia/Schneider_Pt111', 'Surface/Ammonia/Schneider_Pt211', 'Surface/Ammonia/Schneider_Rh111',"Surface/Ammonia/Schneider_Rh211",
                                "Surface/Ammonia/Vlachos_Ru0001","Surface/CPOX_Pt/Deutschmann2006_adjusted","Surface/DOC/Arevalo_Pt111","Surface/DOC/Ishikawa_Rh111","Surface/DOC/Mhadeshwar_Pt111","Surface/DOC/Nitrogen","Surface/Example","Surface/Hydrazine/Roldan_Cu111","Surface/Hydrazine/Roldan_Ir111","Surface/Methane/Deutschmann_Ni","Surface/Methane/Deutschmann_Ni_full"
                                ,"Surface/Methane/Deutschmann_Pt","Surface/Methane/Vlachos_Pt111","Surface/Methane/Vlachos_Rh","TEOS","YF/full","YF/seed","biCPD_H_shift","c-C5H5_CH3_Sharma","combustion_core/version2","combustion_core/version3","combustion_core/version4","combustion_core/version5","fascella","kislovB","naphthalene_H","primaryH2O2","primaryNitrogenLibrary",
                                "primaryNitrogenLibrary/LowT","primarySulfurLibrary","vinylCPD_H"
                                ]
        self.original_index = { item: index for index, item in enumerate(self.options_kinetic)}
        self.selected_items = []
        self.unselected_items = list(self.options_kinetic)
        for item in self.unselected_items:
            self.left_listbox.insert("end", item)
        
        
        # Create buttons to move items between listboxes
        self.kinetic_button_add = ctk.CTkButton(self.frame_kinetic, text='>>', command=lambda: self.move_items(self.left_listbox, self.right_listbox))
        self.kinetic_button_add.grid(row=3, column=1, padx=5, pady=5)
        self.kinetic_button_remove = ctk.CTkButton(self.frame_kinetic, text='<<', command=lambda: self.move_items(self.right_listbox, self.left_listbox))
        self.kinetic_button_remove.grid(row=4, column=1, padx=5, pady=5)
        
        # Create an entry box that allows for user to input kinetic database
        self.kinetic_database = ctk.CTkEntry(self.frame_kinetic, width=30, placeholder_text='Enter custom kinetic library', placeholder_text_color='grey')
        self.kinetic_database.grid(row=1, column=2, padx=5, pady=5, columnspan=1, sticky='ew')
        self.kinetic_database_button = ctk.CTkButton(self.frame_kinetic, text='Enter', command=lambda: self.add_kinetic_database(self.kinetic_database.get()))
        self.kinetic_database_button.grid(row=1, column=3, padx=5, pady=5)
        
    
    
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
    
    # Define a function to search for kinetic database
    def search_kinetic_database(self, event):
        search_term = self.search_kinetic.get()
        self.left_listbox.delete(0, "end")
        for item in self.unselected_items:
            if search_term.lower() in item.lower():
                self.left_listbox.insert("end", item)
            
    # Define a function to add kinetic database
    def add_kinetic_database(self, kinetic_database):
        #self.unselected_items.append(kinetic_database)
        self.right_listbox.insert("end", kinetic_database)        