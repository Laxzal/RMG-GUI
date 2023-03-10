database(
	thermoLibraries = [],
	reactionLibraries = [],
	seedMechanisms = [],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
)

species( 
    label='231',
    reactive=False,
    structure=SMILES('132'),
)

species(
    label='31',
    reactive=False,
    structure=AdjacencyList(231),
)



mlEstimator(
	thermo=True,
	name='',
	minHeavyAtoms=0,
	maxHeavyAtoms=0,
	minCarbonAtoms=0,
	maxCarbonAtoms=0,
	minOxygenAtoms=0,
	maxOxygenAtoms=0,
	minNitrogenAtoms=0,
	maxNitrogenAtoms=0,
	onlyCyclics=,
	onlyHeterocyclics=,
	minCycleOverlap=0,
	H298UncertaintyCutOff=(34242,'kcal/mol'),
	S298UncertaintyCutoff=(0.0,'cal/(mol*k)'),
	CpUncertaintyCutoff=(0.0,'cal/(mol*k)'),
	)
	

uncertainty(
	localAnalysis=True,
	globalAnalysis=,
	uncorrelated=True,
	correlated=,
	localNumber=0,
	terminationTime=(0,'s'),
	pceRunTime=(0,'s'),
	logx=True,
	)
	

email('234')

