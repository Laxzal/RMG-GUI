database(
	thermoLibraries = [],
	reactionLibraries = [],
	seedMechanisms = [],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
)

species(
    label='Restroom',
    reactive=True,
    structure=AdjacencyList(""" HOHO """),
)



pressureDependence(
	method='Modified Strong Collision',
	maximumGrainSize=(5000,'kcal/mol),
	maximumAtoms=23,
	interpolation='Chebyshev(2,4)',
	)
	

email('23')

