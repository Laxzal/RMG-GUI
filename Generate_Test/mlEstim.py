database(
	thermoLibraries = [],
	reactionLibraries = [],
	seedMechanisms = [],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
)

species( 
    label='Age',
    reactive=True,
    structure=SMILES('CCCC'),
)



mlEstimator(
	thermo=True,
	name='CC',
	minHeavyAtoms=3,
	maxHeavyAtoms=42,
	minCarbonAtoms=321231,
	maxCarbonAtoms=523,
	minOxygenAtoms=523,
	maxOxygenAtoms=4234,
	minNitrogenAtoms=123,
	maxNitrogenAtoms=4212,
	onlyCyclics=True,
	onlyHeterocyclics=False,
	minCycleOverlap=23,
	)
	

email('231')

