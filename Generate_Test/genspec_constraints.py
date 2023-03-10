database(
	thermoLibraries = [],
	reactionLibraries = [],
	seedMechanisms = [],
	kineticsDepositories = ['training'],
	kineticsFamilies = 'default',
	kineticsEstimator = 'rate rules'
)

species( 
    label='Boat',
    reactive=True,
    structure=SMILES('CCC'),
)



generatedSpeciesConstraints(
	allowed=['CC,DD'],
	maximumCarbonAtoms=16,
	maximumOxygenAtoms=12,
	maximumNitrogenAtoms=12,
	maximumSiliconAtoms=2,
	maximumSulfurAtoms=2,
	maximumHeavyAtoms=2,
	maximumRadicalElectrons=5,
	maximumSingletCarbenes=5,
	maximumCarbeneRadicals=5,
	maximumIsotopicAtoms=4,
	allowSingletO2=True,
	)
	

email('d')

