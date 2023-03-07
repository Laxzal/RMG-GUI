database(
	thermoLibraries = ["GRI-Mech3.0", "thermo_DFT_CCSDTF12_BAC"],
	reactionLibraries = ["2-BTP/full", "2009_Sharma_C5H5_CH3_highP"],
	seedMechanisms = ["2001_Tokmakov_H_Toluene_to_CH3_Benzene"],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
),

species(
    label='rewrw',
    reactive=False,
    structure=SMILES('erwerwe'),
)

email('ewrwer')

