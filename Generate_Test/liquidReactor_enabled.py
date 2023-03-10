database(
	thermoLibraries = [],
	reactionLibraries = [],
	seedMechanisms = [],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
)

species(
    label='Pocket',
    reactive=True,
    structure=AdjacencyList(""" CH """),
)

species(
    label='Correct',
    reactive=False,
    structure=SMILES('CCC'),
)



simpleReactor(
	temperature = ('11','K'),
	pressure = ('('11', None)','bar'),
	initialMoleFractions = {
		'Pocket': 11,
		'Correct': 11,
	},
	nSims = 3333,
	terminationConversion = {
		'Pocket': 11,
	},
	terminationTime = (3,'s'),
	sensitivity = ['Pocket''Correct'],
	sensitivityThreshold = 1,
)

liquidReactor(
	temperature = ('11','K'),
	pressure = ('11','bar'),
	initialConcentrations= {
		'Pocket': 1,
		'Correct': 1,
	},
	nSims = 1,
	terminationConversion = {
		'Pocket': 1,
		'Correct': 1,
	},
	terminationTime = (111,'s'),
	sensitivity = ['Pocket''Correct'],
	sensitivityThreshold = 11,
	)
	

email('11')

