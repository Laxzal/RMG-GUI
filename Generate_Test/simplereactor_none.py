database(
	thermoLibraries = [],
	reactionLibraries = [],
	seedMechanisms = [],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
)

species(
    label='QWEQWEQ',
    reactive=False,
    structure=SMILES('WEQ'),
)

email('WEQ')

