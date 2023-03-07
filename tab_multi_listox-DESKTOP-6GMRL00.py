import tkinter as tk

class DualListBoxes(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6']
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
        self.options_kinetic = ['1989_Stewart_2CH3_to_C2H5_H', '2-BTP/full', '2-BTP/seed', 
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
                                "BurkeH2O2inArHe",
                                "BurkeH2O2inN2",
                                "C10H11",
                                "C12H11_pdep",
                                "C2H2_init",
                                "C2H4+O_Klipp2017",
                                "C3",
                                "C6H5_C4H4_Mebel",
                                "CF2BrCl",
                                "CH3Cl",
                                "Chernov",
                                "CurranPentane",
                                "DMSOxy",
                                "DTU_mech_CH3Cl",
                                "Dooley/C1",
                                "Dooley/methylformate",
                                "Dooley/methylformate_2",
                                "Dooley/methylformate_all_ARHEbathgas",
                                "Dooley/methylformate_all_N2bathgas",
                                "ERC-FoundationFuelv0.9",
                                "Ethylamine",
                                "FFCM1(-)",
                                "First_to_Second_Aromatic_Ring/2005_Ismail_C6H5_C4H6_highP",
                                "First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP",
                                "First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP",
                                "First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP",
                                "First_to_Second_Aromatic_Ring/2016_Mebel_Indene_CH3_highP",
                                "First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP",
                                "First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP",
                                "First_to_Second_Aromatic_Ring/2017_Mebel_C6H5C2H2_C2H2_highP",
                                "First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C2H2_highP",
                                "First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP",
                                "First_to_Second_Aromatic_Ring/phenyl_diacetylene_effective",
                                'Fulvene_H', 'GRI-HCO', 'GRI-Mech3.0', 'GRI-Mech3.0-N', 'Glarborg/C0', 'Glarborg/C1', 'Glarborg/C2', 'Glarborg/C3', 'Glarborg/highP', 'HydrazinePDep', 'Iodine-R_recombination', 'JetSurF1.0', 'JetSurF2.0', 'Klippenstein_Glarborg2016', 'Lai_Hexylbenzene', 'Mebel_C6H5_C2H2', 'Mebel_Naphthyl', 'Methylformate', 'N-S_interactions', 'NIST_Fluorine/CH2F2/full', 'NIST_Fluorine/CH2F2/seed', 'NIST_Fluorine/full', 'NIST_Fluorine/seed', 'NOx2018', 'Narayanaswamy', 'Nitrogen_Dean_and_Bozzelli', 'Nitrogen_Glarborg_Gimenez_et_al', 'Nitrogen_Glarborg_Lucassen_et_al', 'Nitrogen_Glarborg_Zhang_et_al', 'Sulfur/DMDS', 'Sulfur/DMS', 'Sulfur/DTBS', 'Sulfur/GlarborgBozzelli', 'Sulfur/GlarborgH2S', 'Sulfur/GlarborgH2S/alt', 'Sulfur/GlarborgMarshall', 'Sulfur/GlarborgNS', 'Sulfur/HSSH_1bar', 'Sulfur/Hexanethial_nr', 'Sulfur/Sendt', 'Sulfur/TP_Song', 'Sulfur/Thial_Hydrolysis', 'Surface/Ammonia/Duan_Ni111', 'Surface/Ammonia/Duan_Ni211', 'Surface/Ammonia/Kraehnert_Pt111', 'Surface/Ammonia/Novell_Pd111', 'Surface/Ammonia/Novell_Pt111', 'Surface/Ammonia/Novell_Rh111', 'Surface/Ammonia/Offermans_Pt111', 'Surface/Ammonia/Popa_Rh111', 'Surface/Ammonia/Rebrov_Pt111', 'Surface/Ammonia/Roldan_Ru0001', 'Surface/Ammonia/Scheuer_Pt', 'Surface/Ammonia/Schneider_Pd111', 'Surface/Ammonia/Schneider_Pd211', 'Surface/Ammonia/Schneider_Pt111', 'Surface/Ammonia/Schneider_Pt211', 'Surface/Ammonia/Schneider_Rh111',
                                "Surface/Ammonia/Schneider_Rh211",
                                "Surface/Ammonia/Vlachos_Ru0001",
                                "Surface/CPOX_Pt/Deutschmann2006_adjusted",
                                "Surface/DOC/Arevalo_Pt111",
                                "Surface/DOC/Ishikawa_Rh111",
                                "Surface/DOC/Mhadeshwar_Pt111",
                                "Surface/DOC/Nitrogen",
                                "Surface/Example",
                                "Surface/Hydrazine/Roldan_Cu111",
                                "Surface/Hydrazine/Roldan_Ir111",
                                "Surface/Methane/Deutschmann_Ni",
                                "Surface/Methane/Deutschmann_Ni_full",
                                "Surface/Methane/Deutschmann_Pt",
                                "Surface/Methane/Vlachos_Pt111",
                                "Surface/Methane/Vlachos_Rh",
                                "TEOS",
                                "YF/full",
                                "YF/seed",
                                "biCPD_H_shift",
                                "c-C5H5_CH3_Sharma",
                                "combustion_core/version2",
                                "combustion_core/version3",
                                "combustion_core/version4",
                                "combustion_core/version5",
                                "fascella",
                                "kislovB",
                                "naphthalene_H",
                                "primaryH2O2",
                                "primaryNitrogenLibrary",
                                "primaryNitrogenLibrary/LowT",
                                "primarySulfurLibrary",
                                "vinylCPD_H"
                                ]

        # Create Headings
        self.left_listbox_1_heading = tk.Label(self, text='Unselected ThermoLib')
        self.right_listbox_1_heading = tk.Label(self, text='Selected ThermoLib')
        self.left_listbox_2_heading = tk.Label(self, text='Unselected KineticsLib')
        self.right_listbox_2_heading = tk.Label(self, text='Selected KineticsLib')
        self.left_listbox_3_heading = tk.Label(self, text='Unselected SeedMech')
        self.right_listbox_3_heading = tk.Label(self, text='Selected SeedMech')

        # Create the first pair of Listboxes
        self.left_listbox_1 = tk.Listbox(self, height=10,width=10 selectmode=tk.EXTENDED)
        self.right_listbox_1 = tk.Listbox(self, height=10,width=10 selectmode=tk.EXTENDED)

        for item in self.options_thermo:
            self.left_listbox_1.insert(tk.END, item)

        # Create the second pair of Listboxes
        self.left_listbox_2 = tk.Listbox(self, height=10,width=10 selectmode=tk.EXTENDED)
        self.right_listbox_2 = tk.Listbox(self, height=10,width=10 selectmode=tk.EXTENDED)

        for item in self.options_kinetic:
            self.left_listbox_2.insert(tk.END, item)

        # Create the third pair of Listboxes
        self.left_listbox_3 = tk.Listbox(self, height=10,width=10 selectmode=tk.EXTENDED)
        self.right_listbox_3 = tk.Listbox(self, height=10,width=10, selectmode=tk.EXTENDED)

        for item in self.options_kinetic:
            self.left_listbox_3.insert(tk.END, item)

        # Set the layout of the Headings
        self.left_listbox_1_heading.grid(row=0, column=0, padx=5)
        self.right_listbox_1_heading.grid(row=0, column=1, padx=5)
        self.left_listbox_2_heading.grid(row=7, column=0, padx=5)
        self.right_listbox_2_heading.grid(row=7, column=1, padx=5)
        self.left_listbox_3_heading.grid(row=10, column=0, padx=5)
        self.right_listbox_3_heading.grid(row=10, column=1, padx=5)

        
        # Set the layout of the Listboxes
        self.left_listbox_1.grid(row=2, column=0, padx=10, rowspan=2)
        self.right_listbox_1.grid(row=2, column=1, padx=10, rowspan=2)
        self.left_listbox_2.grid(row=8, column=0, padx=10, rowspan=2)
        self.right_listbox_2.grid(row=8, column=1, padx=10, rowspan=2)
        self.left_listbox_3.grid(row=11, column=0, padx=10, rowspan=2)
        self.right_listbox_3.grid(row=11, column=1, padx=10, rowspan=2)

        # Create buttons to move items between Listboxes
        self.button_1 = tk.Button(self, text='>>', command=lambda: self.move_items(self.left_listbox_1, self.right_listbox_1))
        self.button_2 = tk.Button(self, text='<<', command=lambda: self.move_items(self.right_listbox_1, self.left_listbox_1))
        self.button_3 = tk.Button(self, text='>>', command=lambda: self.move_items(self.left_listbox_2, self.right_listbox_2))
        self.button_4 = tk.Button(self, text='<<', command=lambda: self.move_items(self.right_listbox_2, self.left_listbox_2))
        self.button_5 = tk.Button(self, text='>>', command=lambda: self.move_items(self.left_listbox_3, self.right_listbox_3))
        self.button_6 = tk.Button(self, text='<<', command=lambda: self.move_items(self.right_listbox_3, self.left_listbox_3))

        # Set the layout of the buttons
        self.button_1.grid(row=2, column=2, pady=10)
        self.button_2.grid(row=3, column=2, pady=10)
        self.button_3.grid(row=8, column=2, pady=10)
        self.button_4.grid(row=9, column=2, pady=10)
        self.button_5.grid(row=11, column=2, pady=10)
        self.button_6.grid(row=12, column=2, pady=10)
    # Define a function to move items between Listboxes
    def move_items(self,left_listbox, right_listbox):
        selected_indices = left_listbox.curselection()
        for index in reversed(selected_indices):
            right_listbox.insert(tk.END, left_listbox.get(index))
            left_listbox.delete(index)