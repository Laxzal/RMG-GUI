database(
	thermoLibraries = [],
	reactionLibraries = [],
	seedMechanisms = [],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
)

species(
    label='crowFeet',
    reactive=True,
    structure=AdjacencyList(""" Low """),
)

species(
    label='Science',
    reactive=False,
    structure=SMILES('DDD'),
)



model(
	toleranceMoveToCore = 0.5,
	toleranceInterruptSimulation = 100000000,
	toleranceKeepInEdge = 0.05,
	maximumEdgeSpecies = 200000,
	minCoreSizeForPrune = 50,
	maxNumObjsPerIter = None,
	terminateAtMaxObjects = False,
	toleranceMoveEdgeReactionToCore = None,
	toleranceMoveEdgeReactionToCoreInterrupt = None,
	toleranceMoveSurfaceSpeciesToCore = None,
	toleranceMoveSurfaceReactionToCore = None,
	toleranceMoveEdgeReactionToSurface = None,
	toleranceThermoKeepSpeciesInEdge = None,
	minSpeciesExistIterationsForPrune = 2,
	filterReactions = True,
	filterThreshold = None,
	)
	

email('ddd')

