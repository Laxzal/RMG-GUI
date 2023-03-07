database(
	thermoLibraries = [],
	reactionLibraries = [],
	seedMechanisms = [],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
)

species(
    label='eqwe',
    reactive=False,
    structure=['AdjacencyList']('weqw'),
)

email('weq')

