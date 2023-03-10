database(
	thermoLibraries = [],
	reactionLibraries = [],
	seedMechanisms = [],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
)

species( 
    label='40Mins',
    reactive=True,
    structure=SMILES('Miii'),
)

species(
    label='rish',
    reactive=False,
    structure=AdjacencyList(""" DDD """),
)



quantumMechanics(
	software='mopac',
	method='qm3',
	fileStore='QMFiles',
	scratchDirectory='C:/Users/Calvin/Documents/repositories/RMG-GUI/Generate_Test',
	onlyCyclics=True,
	maxRadicalNumber=22,
	)
	

email('df')

