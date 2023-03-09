import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import customtkinter as ctk

class modelTolerances(tk.Frame):

    def __init__(self, master):
        super().__init__()
        self.master = master

        #Create 15 frames
        self.frame0 = ttk.Frame(self.master)
        self.frame0.grid(row=0, column=0, sticky='nsew')
        self.frame1 = ttk.Frame(self.master)
        self.frame1.grid(row=1, column=0, sticky='nsew')
        self.frame2 = ttk.Frame(self.master)
        self.frame2.grid(row=2, column=0, sticky='nsew')
        self.frame3 = ttk.Frame(self.master)
        self.frame3.grid(row=1, column=1, sticky='nsew')
        self.frame4 = ttk.Frame(self.master)
        self.frame4.grid(row=2, column=1, sticky='nsew')
        self.frame5 = ttk.Frame(self.master)
        self.frame5.grid(row=3, column=0, sticky='nsew')
        self.frame6 = ttk.Frame(self.master)
        self.frame6.grid(row=4, column=0, sticky='nsew')
        self.frame7 = ttk.Frame(self.master)
        self.frame7.grid(row=3, column=1, sticky='nsew')
        self.frame8 = ttk.Frame(self.master)
        self.frame8.grid(row=4, column=1, sticky='nsew')
        self.frame9 = ttk.Frame(self.master)
        self.frame9.grid(row=5, column=0, sticky='nsew')
        self.frame10 = ttk.Frame(self.master)
        self.frame10.grid(row=5, column=1, sticky='nsew')
        self.frame11 = ttk.Frame(self.master)
        self.frame11.grid(row=6, column=0, sticky='nsew')
        self.frame12 = ttk.Frame(self.master)
        self.frame12.grid(row=6, column=1, sticky='nsew')
        self.frame13 = ttk.Frame(self.master)
        self.frame13.grid(row=7, column=0, sticky='nsew')
        self.frame_load = ttk.Frame(self.master)
        self.frame_load.grid(row=0, column=1, sticky='nsew')
        self.frame14 = ttk.Frame(self.master)
        self.frame14.grid(row=8, column=0, sticky='nsew')



        # Create a tick box in gui to use Model Tolerances
        self.use_model_tolerances = tk.BooleanVar()
        self.use_model_tolerances.set(0)
        self.use_model_tolerances_check = tk.Checkbutton(self.frame0, text="Use Model Tolerances", variable=self.use_model_tolerances)
        self.use_model_tolerances_check.grid(row=0, column=0, padx=5, pady=5)

        # Create a label for toleranceMovetoCore and entry for toleranceMovetoCore
        self.toleranceMovetoCore_label = tk.Label(self.frame1, text='toleranceMovetoCore:')
        self.toleranceMovetoCore_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.toleranceMovetoCore_entry = tk.Entry(self.frame1, width=10)
        self.toleranceMovetoCore_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create a lavel for toleranceKeepInEdge and entry for toleranceKeepInEdge
        self.toleranceKeepInEdge_label = tk.Label(self.frame2, text='toleranceKeepInEdge:')
        self.toleranceKeepInEdge_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.toleranceKeepInEdge_entry = tk.Entry(self.frame2, width=10)
        self.toleranceKeepInEdge_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create label for toleranceInterruptSimulation and entry for toleranceInterruptSimulation
        self.toleranceInterruptSimulation_label = tk.Label(self.frame3, text='toleranceInterruptSimulation:')
        self.toleranceInterruptSimulation_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.toleranceInterruptSimulation_entry = tk.Entry(self.frame3, width=10)
        self.toleranceInterruptSimulation_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create maximumEdgeSpecies label and entry
        self.maximumEdgeSpecies_label = tk.Label(self.frame4, text='maximumEdgeSpecies:')
        self.maximumEdgeSpecies_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.maximumEdgeSpecies_entry = tk.Entry(self.frame4, width=10)
        self.maximumEdgeSpecies_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create minCoreSizeForPrune label and entry
        self.minCoreSizeForPrune_label = tk.Label(self.frame5, text='minCoreSizeForPrune:')
        self.minCoreSizeForPrune_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.minCoreSizeForPrune_entry = tk.Entry(self.frame5, width=10)
        self.minCoreSizeForPrune_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create maxNumObjsPerIter label and entry
        self.maxNumObjsPerIter_label = tk.Label(self.frame6, text='maxNumObjsPerIter:')
        self.maxNumObjsPerIter_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.maxNumObjsPerIter_entry = tk.Entry(self.frame6, width=10)
        self.maxNumObjsPerIter_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create terminateAtMaxObjects label and true or false list
        self.terminateAtMaxObjects_label = tk.Label(self.frame7, text='terminateAtMaxObjects:')
        self.terminateAtMaxObjects_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.terminateAtMaxObjects_list = ['','True', 'False']
        self.terminateAtMaxObjects = tk.StringVar()
        self.terminateAtMaxObjects.set(self.terminateAtMaxObjects_list[0])
        self.terminateAtMaxObjects_menu = tk.OptionMenu(self.frame7, self.terminateAtMaxObjects, *self.terminateAtMaxObjects_list)
        self.terminateAtMaxObjects_menu.grid(row=0, column=1, padx=5, pady=5, sticky='e')
        

        # Create toleranceMoveEdgeReactionToCore label and entry
        self.toleranceMoveEdgeReactionToCore_label = tk.Label(self.frame8, text='toleranceMoveEdgeReactionToCore:')
        self.toleranceMoveEdgeReactionToCore_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.toleranceMoveEdgeReactionToCore_entry = tk.Entry(self.frame8, width=10)
        self.toleranceMoveEdgeReactionToCore_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create toleranceMoveEdgeReactionToCoreInterrupt label and entry
        self.toleranceMoveEdgeReactionToCoreInterrupt_label = tk.Label(self.frame9, text='toleranceMoveEdgeReactionToCoreInterrupt:')
        self.toleranceMoveEdgeReactionToCoreInterrupt_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.toleranceMoveEdgeReactionToCoreInterrupt_entry = tk.Entry(self.frame9, width=10)
        self.toleranceMoveEdgeReactionToCoreInterrupt_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create toleranceMoveSurfaceSpeciesToCore label and entry
        self.toleranceMoveSurfaceSpeciesToCore_label = tk.Label(self.frame10, text='toleranceMoveSurfaceSpeciesToCore:')
        self.toleranceMoveSurfaceSpeciesToCore_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.toleranceMoveSurfaceSpeciesToCore_entry = tk.Entry(self.frame10, width=10)
        self.toleranceMoveSurfaceSpeciesToCore_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create toleranceMoveSurfaceReactionToCore label and entry
        self.toleranceMoveSurfaceReactionToCore_label = tk.Label(self.frame11, text='toleranceMoveSurfaceReactionToCore:')
        self.toleranceMoveSurfaceReactionToCore_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.toleranceMoveSurfaceReactionToCore_entry = tk.Entry(self.frame11, width=10)
        self.toleranceMoveSurfaceReactionToCore_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create minSpeciesExistIterationsForPrune label and entry
        self.minSpeciesExistIterationsForPrune_label = tk.Label(self.frame12, text='minSpeciesExistIterationsForPrune:')
        self.minSpeciesExistIterationsForPrune_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.minSpeciesExistIterationsForPrune_entry = tk.Entry(self.frame12, width=10)
        self.minSpeciesExistIterationsForPrune_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create toleranceThermoKeepSpeciesInEdge label and entry
        self.toleranceThermoKeepSpeciesInEdge_label = tk.Label(self.frame13, text='toleranceThermoKeepSpeciesInEdge:')
        self.toleranceThermoKeepSpeciesInEdge_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.toleranceThermoKeepSpeciesInEdge_entry = tk.Entry(self.frame13, width=10)
        self.toleranceThermoKeepSpeciesInEdge_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create toleranceMoveEdgeReactionToSurface label and entry
        self.toleranceMoveEdgeReactionToSurface_label = tk.Label(self.frame14, text='toleranceMoveEdgeReactionToSurface:')
        self.toleranceMoveEdgeReactionToSurface_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.toleranceMoveEdgeReactionToSurface_entry = tk.Entry(self.frame14, width=10)
        self.toleranceMoveEdgeReactionToSurface_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Create a dropdown menu for preloaded settings
        self.preloadedSettings_label = tk.Label(self.frame_load, text='Preloaded Settings:')
        self.preloadedSettings_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.preloadedSettings = tk.StringVar(self.frame_load)
        self.prelodedSettings_list = [ 'None', 
                                        'Speed Up - Filter Reactions',
                                        'Speed Up - Pruning', 
                                        'Thermodynamic Pruning', 
                                        'Taking Multiple Species at a Time',
                                        'Dynamics Criterion',
                                        'Surface Algorithm']
        self.preloadedSettings.set(self.prelodedSettings_list[0])
        self.preloadedSettings_menu = tk.OptionMenu(self.frame_load, self.preloadedSettings,*self.prelodedSettings_list,
                                                    command=self.load_preloaded_settings

                                                    )
        self.preloadedSettings_menu.grid(row=0, column=1, padx=5, pady=5, sticky='e')



    def delete_all_values_in_entry(self):
        """A function that deletes all values in the entry boxes"""
        self.toleranceKeepInEdge_entry.delete(0, 'end')
        self.toleranceInterruptSimulation_entry.delete(0, 'end')
        self.maximumEdgeSpecies_entry.delete(0, 'end')
        self.minCoreSizeForPrune_entry.delete(0, 'end')
        self.maxNumObjsPerIter_entry.delete(0, 'end')
        self.terminateAtMaxObjects.set(self.terminateAtMaxObjects_list[0])
        self.toleranceMoveEdgeReactionToCore_entry.delete(0, 'end')
        self.toleranceMoveEdgeReactionToCoreInterrupt_entry.delete(0, 'end')
        self.toleranceMoveSurfaceSpeciesToCore_entry.delete(0, 'end')
        self.toleranceMoveSurfaceReactionToCore_entry.delete(0, 'end')
        self.toleranceMovetoCore_entry.delete(0, 'end')
        self.minSpeciesExistIterationsForPrune_entry.delete(0, 'end')
        

    def load_preloaded_settings(self, events=None):
        """A function that loads preloaded settings into the entry boxes and also runs the function delete_all_values_in_entry()"""
        self.delete_all_values_in_entry()
        selected_item = self.preloadedSettings.get()

        if selected_item == 'Speed Up - Filter Reactions':
            self.toleranceMovetoCore_entry.insert(0, '0.1')
            self.toleranceInterruptSimulation_entry.insert(0, '0.1')
        elif selected_item == 'Speed Up - Pruning':
            self.toleranceMovetoCore_entry.insert(0, '0.5')
            self.toleranceInterruptSimulation_entry.insert(0, '100000000')
            self.toleranceKeepInEdge_entry.insert(0, '0.05')
            self.maximumEdgeSpecies_entry.insert(0, '200000')
            self.minCoreSizeForPrune_entry.insert(0, '50')
            self.minSpeciesExistIterationsForPrune_entry.insert(0, '2')
        elif selected_item == 'Thermodynamic Pruning':
            self.toleranceMovetoCore_entry.insert(0, '0.5')
            self.toleranceInterruptSimulation_entry.insert(0, '0.5')
            self.toleranceThermoKeepSpeciesInEdge_entry.insert(0, '0.5')
            self.maximumEdgeSpecies_entry.insert(0, '200000')
            self.minCoreSizeForPrune_entry.insert(0, '50')
        elif selected_item == 'Taking Multiple Species at a Time':
            self.toleranceKeepInEdge_entry.insert(0, '0.0')
            self.toleranceMovetoCore_entry.insert(0, '0.1')
            self.toleranceInterruptSimulation_entry.insert(0, '0.3')
            self.maxNumObjsPerIter_entry.insert(0, '2')
            self.terminateAtMaxObjects.set(self.terminateAtMaxObjects_list[1])
        elif selected_item == 'Dynamics Criterion':
            self.toleranceMovetoCore_entry.insert(0, '0.1')
            self.toleranceInterruptSimulation_entry.insert(0, '0.1')
            self.toleranceMoveEdgeReactionToCore_entry.insert(0, '10')
            self.toleranceMoveEdgeReactionToCoreInterrupt_entry.insert(0, '5.0')
        elif selected_item == 'Surface Algorithm':
            self.toleranceMovetoCore_entry.insert(0, '0.1')
            self.toleranceInterruptSimulation_entry.insert(0, '0.1')
            self.toleranceMoveSurfaceSpeciesToCore_entry.insert(0, '0.01')
            self.toleranceMoveSurfaceReactionToCore_entry.insert(0, '5')
            self.toleranceMoveEdgeReactionToCore_entry.insert(0, '30')
            self.toleranceMoveEdgeReactionToCoreInterrupt_entry.insert(0, '5.0')
            self.toleranceMoveEdgeReactionToSurface_entry.insert(0, '10')