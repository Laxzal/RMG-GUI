database(
	thermoLibraries = [],
	reactionLibraries = [],
	seedMechanisms = [],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
)

species( 
    label='butane',
    reactive=True,
    structure=SMILES('CCCC'),
)

species(
    label='O2',
    reactive=False,
    structure=SMILES('[O][O]'),
)

species(
    label='N2',
    reactive=True,
    structure=AdjacencyList("""
    1 N u0 p1 c0 {2,T}
    2 N u0 p1 c0 {1,T}
    """),
)



simulator(
	atol = 0.0000009,
	rtol = 99,
	sens_atol = 0.0129,
	sens_rtol = 0.1233,
	)
	

email('2')

