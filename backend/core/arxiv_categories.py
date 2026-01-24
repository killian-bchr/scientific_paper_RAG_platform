from backend.core.constants import (
    BiologyCategories,
    ComputerScienceCategories,
    DefaultCategories,
    Domains,
    EconomicsCategories,
    ElectricalEngineeringCategories,
    FinanceCategories,
    MathematicsCategories,
    Names,
    PhysicsCategories,
    StatisticsCategories,
)

"""
arXiv Categories Mapping
"""

ARXIV_CATEGORIES = {
    # Computer Science
    "cs.AI": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.ARTIFICIAL_INTELLIGENCE,
    },
    "cs.AR": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.HARDWARE_ARCHITECTURE,
    },
    "cs.CC": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.COMPUTATIONAL_COMPLEXITY,
    },
    "cs.CE": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.COMPUTATIONAL_ENGINEERING,
    },
    "cs.CG": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.COMPUTATIONAL_GEOMETRY,
    },
    "cs.CL": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.COMPUTATION_AND_LANGUAGE,
    },
    "cs.CR": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.CRYPTOGRAPHY,
    },
    "cs.CV": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.COMPUTER_VISION,
    },
    "cs.CY": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.COMPUTERS_AND_SOCIETY,
    },
    "cs.DB": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.DATABASES,
    },
    "cs.DC": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.DISTRIBUTED_COMPUTING,
    },
    "cs.DL": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.DIGITAL_LIBRARIES,
    },
    "cs.DM": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.DISCRETE_MATHEMATICS,
    },
    "cs.DS": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.DATA_STRUCTURES,
    },
    "cs.ET": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.EMERGING_TECHNOLOGIES,
    },
    "cs.FL": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.FORMAL_LANGUAGES,
    },
    "cs.GL": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.GENERAL_LITERATURE,
    },
    "cs.GR": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.GRAPHICS,
    },
    "cs.GT": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.GAME_THEORY,
    },
    "cs.HC": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.HUMAN_COMPUTER_INTERACTION,
    },
    "cs.IR": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.INFORMATION_RETRIEVAL,
    },
    "cs.IT": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.INFORMATION_THEORY,
    },
    "cs.LG": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.MACHINE_LEARNING,
    },
    "cs.LO": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.LOGIC,
    },
    "cs.MA": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.MULTIAGENTS_SYSTEMS,
    },
    "cs.MM": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.MULTIMEDIA,
    },
    "cs.MS": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.MATHEMATICAL_SOFTWARE,
    },
    "cs.NA": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.NUMERICAL_ANALYSIS,
    },
    "cs.NE": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.NEURAL_EVOLUTIONARY,
    },
    "cs.NI": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.INTERNET_ARCHITECTURE,
    },
    "cs.OS": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.OPERATING_SYSTEMS,
    },
    "cs.PF": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.PERFORMANCE,
    },
    "cs.PL": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.PROGRAMMING_LANGUAGES,
    },
    "cs.RO": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.ROBOTICS,
    },
    "cs.SC": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.SYMBOLIC_COMPUTATION,
    },
    "cs.SD": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.SOUND,
    },
    "cs.SE": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.SOFTWARE_ENGINEERING,
    },
    "cs.SI": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.SOCIAL_AND_INFORMATION_NETWORKS,
    },
    "cs.SY": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: ComputerScienceCategories.SYSTEMS_AND_CONTROL,
    },
    "cs.OH": {
        Names.DOMAIN: Domains.COMPUTER_SCIENCE,
        Names.CATEGORY: DefaultCategories.OTHER,
    },
    # Economics
    "econ.EM": {
        Names.DOMAIN: Domains.ECONOMICS,
        Names.CATEGORY: EconomicsCategories.ECONOMETRICS,
    },
    "econ.GN": {
        Names.DOMAIN: Domains.ECONOMICS,
        Names.CATEGORY: EconomicsCategories.GENERAL_ECONOMICS,
    },
    "econ.TH": {
        Names.DOMAIN: Domains.ECONOMICS,
        Names.CATEGORY: EconomicsCategories.THEORETICAL_ECONOMICS,
    },
    # Electrical Engineering
    "eess.AS": {
        Names.DOMAIN: Domains.ELECTRICAL_ENGINEERING,
        Names.CATEGORY: ElectricalEngineeringCategories.AUDIO_AND_SPEECH_PROCESSING,
    },
    "eess.IV": {
        Names.DOMAIN: Domains.ELECTRICAL_ENGINEERING,
        Names.CATEGORY: ElectricalEngineeringCategories.IMAGE_AND_VIDEO_PROCESSING,
    },
    "eess.SP": {
        Names.DOMAIN: Domains.ELECTRICAL_ENGINEERING,
        Names.CATEGORY: ElectricalEngineeringCategories.SIGNAL_PROCESSING,
    },
    "eess.SY": {
        Names.DOMAIN: Domains.ELECTRICAL_ENGINEERING,
        Names.CATEGORY: ElectricalEngineeringCategories.SYSTEMS_AND_CONTROL,
    },
    # Mathematics
    "math.AC": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.COMMUTATIVE_ALGEBRA,
    },
    "math.AG": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.ALGEBRAIC_GEOMETRY,
    },
    "math.AP": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.ANALYSIS_OF_PDE,
    },
    "math.AT": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.ALGEBRAIC_TOPOLOGY,
    },
    "math.CA": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.CLASSICAL_ANALYSIS,
    },
    "math.CO": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.COMBINATRONICS,
    },
    "math.CT": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.CATEGORY_THEORY,
    },
    "math.CV": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.COMPLEX_VARIABLES,
    },
    "math.DG": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.DIFFERENTIAL_GEOMETRY,
    },
    "math.DS": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.DYNAMICAL_SYSTEMS,
    },
    "math.FA": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.FUNCTIONAL_ANALYSIS,
    },
    "math.GM": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.GENERAL_MATHEMATICS,
    },
    "math.GN": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.GENERAL_TOPOLOGY,
    },
    "math.GR": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.GROUP_THEORY,
    },
    "math.GT": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.GEOMETRIC_TOPOLOGY,
    },
    "math.HO": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.HISTORY_AND_OVERVIEW,
    },
    "math.IT": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.INFORMATION_THEORY,
    },
    "math.KT": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.HOMOLOGY,
    },
    "math.LO": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.LOGIC,
    },
    "math.MG": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.METRIC_GEOMETRY,
    },
    "math.MP": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.MATHEMATICAL_PHYSICS,
    },
    "math.NA": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.NUMERICAL_ANALYSIS,
    },
    "math.NT": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.NUMBER_THEORY,
    },
    "math.OA": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.OPERATOR_ALGEBRAS,
    },
    "math.OC": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.OPTIMIZATION_CONTROL,
    },
    "math.PR": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.PROBABILITY,
    },
    "math.QA": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.QUANTUM_ALGEBRA,
    },
    "math.RA": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.RINGS_AND_ALGEBRAS,
    },
    "math.RT": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.REPRESENTATION_THEORY,
    },
    "math.SG": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.SYMPLECTIC_GEOMETRY,
    },
    "math.SP": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.SPECTRAL_THEORY,
    },
    "math.ST": {
        Names.DOMAIN: Domains.MATHEMATICS,
        Names.CATEGORY: MathematicsCategories.STATISTICS_THEORY,
    },
    # Physics
    "physics.acc-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.ACCELERATOR_PHYSICS,
    },
    "physics.ao-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.ATMOSPHERIC_AND_OCEANIC_PHYSICS,
    },
    "physics.app-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.APPLIED_PHYSICS,
    },
    "physics.atm-clus": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.ATOMIC_AND_MOLECULAR_CLUSTERS,
    },
    "physics.atom-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.ATOMIC_PHYSICS,
    },
    "physics.bio-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.BIOLOGICAL_PHYSICS,
    },
    "physics.chem-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.CHEMICAL_PHYSICS,
    },
    "physics.class-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.CLASSICAL_PHYSICS,
    },
    "physics.comp-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.COMPUTATIONAL_PHYSICS,
    },
    "physics.data-an": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.DATA_ANALYSIS,
    },
    "physics.ed-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.PHYSICS_EDUCATION,
    },
    "physics.flu-dyn": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.FLUID_DYNAMICS,
    },
    "physics.gen-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.GENERAL_PHYSICS,
    },
    "physics.geo-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.GEOPHYSICS,
    },
    "physics.hist-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.HISTORY_AND_PHILOSOPHY,
    },
    "physics.ins-det": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.INSTRUMENTATION_AND_DETECTORS,
    },
    "physics.med-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.MEDICAL_PHYSICS,
    },
    "physics.optics": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.OPTICS,
    },
    "physics.plasm-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.PLASMA_PHYSICS,
    },
    "physics.pop-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.POPULAR_PHYSICS,
    },
    "physics.soc-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.PHYSICS_AND_SOCIETY,
    },
    "physics.space-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.SPACE_PHYSICS,
    },
    "quant-ph": {
        Names.DOMAIN: Domains.PHYSICS,
        Names.CATEGORY: PhysicsCategories.QUANTUM_PHYSICS,
    },
    # Biology
    "q-bio.BM": {
        Names.DOMAIN: Domains.BIOLOGY,
        Names.CATEGORY: BiologyCategories.BIOMOLECULES,
    },
    "q-bio.CB": {
        Names.DOMAIN: Domains.BIOLOGY,
        Names.CATEGORY: BiologyCategories.CELL_BEHAVIOR,
    },
    "q-bio.GN": {
        Names.DOMAIN: Domains.BIOLOGY,
        Names.CATEGORY: BiologyCategories.GENOMICS,
    },
    "q-bio.MN": {
        Names.DOMAIN: Domains.BIOLOGY,
        Names.CATEGORY: BiologyCategories.MOLECULAR_NETWORKS,
    },
    "q-bio.NC": {
        Names.DOMAIN: Domains.BIOLOGY,
        Names.CATEGORY: BiologyCategories.NEURONS_AND_COGNITION,
    },
    "q-bio.OT": {
        Names.DOMAIN: Domains.BIOLOGY,
        Names.CATEGORY: DefaultCategories.OTHER,
    },
    "q-bio.PE": {
        Names.DOMAIN: Domains.BIOLOGY,
        Names.CATEGORY: BiologyCategories.POPULATION_AND_EVOLUTION,
    },
    "q-bio.QM": {
        Names.DOMAIN: Domains.BIOLOGY,
        Names.CATEGORY: BiologyCategories.QUANTITATIVE_METHODS,
    },
    "q-bio.SC": {
        Names.DOMAIN: Domains.BIOLOGY,
        Names.CATEGORY: BiologyCategories.SUBCELLULAR_PROCESSES,
    },
    "q-bio.TO": {
        Names.DOMAIN: Domains.BIOLOGY,
        Names.CATEGORY: BiologyCategories.TISSUES_AND_ORGANS,
    },
    # Finance
    "q-fin.CP": {
        Names.DOMAIN: Domains.FINANCE,
        Names.CATEGORY: FinanceCategories.COMPUTATIONAL_FINANCE,
    },
    "q-fin.EC": {
        Names.DOMAIN: Domains.FINANCE,
        Names.CATEGORY: FinanceCategories.ECONOMICS,
    },
    "q-fin.GN": {
        Names.DOMAIN: Domains.FINANCE,
        Names.CATEGORY: FinanceCategories.GENERAL_FINANCE,
    },
    "q-fin.MF": {
        Names.DOMAIN: Domains.FINANCE,
        Names.CATEGORY: FinanceCategories.MATHEMATICAL_FINANCE,
    },
    "q-fin.PM": {
        Names.DOMAIN: Domains.FINANCE,
        Names.CATEGORY: FinanceCategories.PORTFOLIO_MANAGEMENT,
    },
    "q-fin.PR": {
        Names.DOMAIN: Domains.FINANCE,
        Names.CATEGORY: FinanceCategories.PRICING_OF_SECURITIES,
    },
    "q-fin.RM": {
        Names.DOMAIN: Domains.FINANCE,
        Names.CATEGORY: FinanceCategories.RISK_MANAGEMENT,
    },
    "q-fin.ST": {
        Names.DOMAIN: Domains.FINANCE,
        Names.CATEGORY: FinanceCategories.STATISTICAL_FINANCE,
    },
    "q-fin.TR": {
        Names.DOMAIN: Domains.FINANCE,
        Names.CATEGORY: FinanceCategories.TRADING_AND_MARKET,
    },
    # Statistics
    "stat.AP": {
        Names.DOMAIN: Domains.STATISTICS,
        Names.CATEGORY: StatisticsCategories.APPLICATIONS,
    },
    "stat.CO": {
        Names.DOMAIN: Domains.STATISTICS,
        Names.CATEGORY: StatisticsCategories.COMPUTATION,
    },
    "stat.ME": {
        Names.DOMAIN: Domains.STATISTICS,
        Names.CATEGORY: StatisticsCategories.METHODOLOGY,
    },
    "stat.ML": {
        Names.DOMAIN: Domains.STATISTICS,
        Names.CATEGORY: StatisticsCategories.MACHINE_LEARNING,
    },
    "stat.OT": {
        Names.DOMAIN: Domains.STATISTICS,
        Names.CATEGORY: DefaultCategories.OTHER,
    },
    "stat.TH": {
        Names.DOMAIN: Domains.STATISTICS,
        Names.CATEGORY: StatisticsCategories.STATISTICS_THEORY,
    },
}
