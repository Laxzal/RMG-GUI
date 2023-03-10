database(
	thermoLibraries = [],
	reactionLibraries = [],
	seedMechanisms = [],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
)

species( 
    label='Bibz',
    reactive=False,
    structure=SMILES('FFF'),
)

species(
    label='Cff',
    reactive=True,
    structure=AdjacencyList(""" DXX """),
)



options(
	name='Seed',
	generateSeedEachIteration=True,
	saveSeedToDatabase=False,
	units='si',
	generateOutputHTML=True,
	saveSimulationProfiles=True,
	saveEdgeSpecies=True,
	trimolecularProductReversible=True,
	saveSeedModulus=-1,
	)
	

email('r')

