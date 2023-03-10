database(
	thermoLibraries = [],
	reactionLibraries = [],
	seedMechanisms = [],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
)

species(
    label='TreeHouse',
    reactive=True,
    structure=AdjacencyList(                """
                1 R  ux {2,S}
                2 O  ux {1,S} {3,S}
                3 Cl ux {2,S}
                """),
)

species(
    label='simpleReactor',
    reactive=False,
    structure=SMILES('ch4'),
)



simpleReactor(
	temperature = ('100','K'),
	pressure = ('1','bar'),
	initialMoleFractions = {
		'TreeHouse': 10,
		'simpleReactor': 12,
	},
	nSims = 13,
	terminationConversion = {
		'TreeHouse': 12,
		'simpleReactor': 1,
	},
	terminationTime = (10000,'s'),
	sensitivity = ['TreeHouse'],
	sensitivityThreshold = 12,
	)
	email('trer')

