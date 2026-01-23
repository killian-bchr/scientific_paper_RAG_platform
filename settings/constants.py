from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"


class Names:
    DOMAIN = "Domain"
    CATEGORY = "Category"


class Domains:
    COMPUTER_SCIENCE = "Computer Science"
    MATHEMATICS = "Mathematics"
    PHYSICS = "Physics"
    BIOLOGY = "Quantitative Biology"
    FINANCE = "Quantitative Finance"
    ECONOMICS = "Economics"
    ELECTRICAL_ENGINEERING = "Electrical Engineering"
    STATISTICS = "Statistics"
    OTHER = "Other"


class Category:
    pass


class DefaultCategories(Category):
    OTHER = "Other"


class ComputerScienceCategories(Category):
    ARTIFICIAL_INTELLIGENCE = "Artificial Intelligence"
    HARDWARE_ARCHITECTURE = "Hardware Architecture"
    COMPUTATIONAL_COMPLEXITY = "Computational Complexity"
    COMPUTATIONAL_ENGINEERING = "Computational Engineering, Finance and Science"
    COMPUTATIONAL_GEOMETRY = "Computational Geometry"
    COMPUTATION_AND_LANGUAGE = "Computation and Language"
    CRYPTOGRAPHY = "Cryptography and Security"
    COMPUTER_VISION = "Computer Vision and Pattern Recognition"
    COMPUTERS_AND_SOCIETY = "Computers and Society"
    DATABASES = "Databases"
    DISTRIBUTED_COMPUTING = "Distributed, Parallel, and Cluster Computing"
    DIGITAL_LIBRARIES = "Digital Libraries"
    DISCRETE_MATHEMATICS = "Discrete Mathematics"
    DATA_STRUCTURES = "Data Structures and Algorithms"
    EMERGING_TECHNOLOGIES = "Emerging Technologies"
    FORMAL_LANGUAGES = "Formal Languages and Automata Theory"
    GENERAL_LITERATURE = "General Literature"
    GRAPHICS = "Graphics"
    GAME_THEORY = "Computer Science and Game Theory"
    HUMAN_COMPUTER_INTERACTION = "Human-Computer Interaction"
    INFORMATION_RETRIEVAL = "Information Retrieval"
    INFORMATION_THEORY = "Information Theory"
    MACHINE_LEARNING = "Machine Learning"
    LOGIC = "Logic in Computer Science"
    MULTIAGENTS_SYSTEMS = "Multiagent Systems"
    MULTIMEDIA = "Multimedia"
    MATHEMATICAL_SOFTWARE = "Mathematical Software"
    NUMERICAL_ANALYSIS = "Numerical Analysis"
    NEURAL_EVOLUTIONARY = "Neural and Evolutionary Computing"
    INTERNET_ARCHITECTURE = "Networking and Internet Architecture"
    OPERATING_SYSTEMS = "Operating Systems"
    PERFORMANCE = "Performance"
    PROGRAMMING_LANGUAGES = "Programming Languages"
    ROBOTICS = "Robotics"
    SYMBOLIC_COMPUTATION = "Symbolic Computation"
    SOUND = "Sound"
    SOFTWARE_ENGINEERING = "Software Engineering"
    SOCIAL_AND_INFORMATION_NETWORKS = "Social and Information Networks"
    SYSTEMS_AND_CONTROL = "Systems and Control"


class EconomicsCategories(Category):
    ECONOMETRICS = "Econometrics"
    THEORETICAL_ECONOMICS = "Theoretical Economics"
    GENERAL_ECONOMICS = "General Economics"


class ElectricalEngineeringCategories(Category):
    AUDIO_AND_SPEECH_PROCESSING = "Audio and Speech Processing"
    IMAGE_AND_VIDEO_PROCESSING = "Image and Video Processing"
    SIGNAL_PROCESSING = "Signal Processing"
    SYSTEMS_AND_CONTROL = "Systems and Control"


class MathematicsCategories(Category):
    COMMUTATIVE_ALGEBRA = "Commutative Algebra"
    ALGEBRAIC_GEOMETRY = "Algebraic Geometry"
    ANALYSIS_OF_PDE = "Analysis of PDEs"
    ALGEBRAIC_TOPOLOGY = "Algebraic Topology"
    CLASSICAL_ANALYSIS = "Classical Analysis and ODEs"
    COMBINATRONICS = "Combinatorics"
    CATEGORY_THEORY = "Category Theory"
    COMPLEX_VARIABLES = "Complex Variables"
    DIFFERENTIAL_GEOMETRY = "Differential Geometry"
    DYNAMICAL_SYSTEMS = "Dynamical Systems"
    FUNCTIONAL_ANALYSIS = "Functional Analysis"
    GENERAL_MATHEMATICS = "General Mathematics"
    GENERAL_TOPOLOGY = "General Topology"
    GROUP_THEORY = "Group Theory"
    GEOMETRIC_TOPOLOGY = "Geometric Topology"
    INFORMATION_THEORY = "Information Theory"
    HISTORY_AND_OVERVIEW = "History and Overview"
    HOMOLOGY = "K-Theory and Homology"
    LOGIC = "Logic"
    METRIC_GEOMETRY = "Metric Geometry"
    MATHEMATICAL_PHYSICS = "Mathematical Physics"
    NUMERICAL_ANALYSIS = "Numerical Analysis"
    NUMBER_THEORY = "Number Theory"
    OPERATOR_ALGEBRAS = "Operator Algebras"
    OPTIMIZATION_CONTROL = "Optimization and Control"
    PROBABILITY = "Probability"
    QUANTUM_ALGEBRA = "Quantum Algebra"
    RINGS_AND_ALGEBRAS = "Rings and Algebras"
    REPRESENTATION_THEORY = "Representation Theory"
    SYMPLECTIC_GEOMETRY = "Symplectic Geometry"
    SPECTRAL_THEORY = "Spectral Theory"
    STATISTICS_THEORY = "Statistics Theory"


class PhysicsCategories(Category):
    ACCELERATOR_PHYSICS = "Accelerator Physics"
    ATMOSPHERIC_AND_OCEANIC_PHYSICS = "Atmospheric and Oceanic Physics"
    APPLIED_PHYSICS = "Applied Physics"
    ATOMIC_AND_MOLECULAR_CLUSTERS = "Atomic and Molecular Clusters"
    ATOMIC_PHYSICS = "Atomic Physics"
    BIOLOGICAL_PHYSICS = "Biological Physics"
    CHEMICAL_PHYSICS = "Chemical Physics"
    CLASSICAL_PHYSICS = "Classical Physics"
    COMPUTATIONAL_PHYSICS = "Computational Physics"
    DATA_ANALYSIS = "Data Analysis, Statistics and Probability"
    PHYSICS_EDUCATION = "Physics Education"
    FLUID_DYNAMICS = "Fluid Dynamics"
    GENERAL_PHYSICS = "General Physics"
    GEOPHYSICS = "Geophysics"
    HISTORY_AND_PHILOSOPHY = "History and Philosophy of Physics"
    INSTRUMENTATION_AND_DETECTORS = "Instrumentation and Detectors"
    MEDICAL_PHYSICS = "Medical Physics"
    OPTICS = "Optics"
    PLASMA_PHYSICS = "Plasma Physics"
    POPULAR_PHYSICS = "Popular Physics"
    PHYSICS_AND_SOCIETY = "Physics and Society"
    SPACE_PHYSICS = "Space Physics"
    QUANTUM_PHYSICS = "Quantum Physics"


class BiologyCategories(Category):
    BIOMOLECULES = "Biomolecules"
    CELL_BEHAVIOR = "Cell Behavior"
    GENOMICS = "Genomics"
    MOLECULAR_NETWORKS = "Molecular Networks"
    NEURONS_AND_COGNITION = "Neurons and Cognition"
    POPULATION_AND_EVOLUTION = "Populations and Evolution"
    QUANTITATIVE_METHODS = "Quantitative Methods"
    SUBCELLULAR_PROCESSES = "Subcellular Processes"
    TISSUES_AND_ORGANS = "Tissues and Organs"


class FinanceCategories(Category):
    COMPUTATIONAL_FINANCE = "Computational Finance"
    ECONOMICS = "Economics"
    GENERAL_FINANCE = "General Finance"
    MATHEMATICAL_FINANCE = "Mathematical Finance"
    PORTFOLIO_MANAGEMENT = "Portfolio Management"
    PRICING_OF_SECURITIES = "Pricing of Securities"
    RISK_MANAGEMENT = "Risk Management"
    STATISTICAL_FINANCE = "Statiscal Finance"
    TRADING_AND_MARKET = "Trading and Market Microstructure"


class StatisticsCategories(Category):
    APPLICATIONS = "Applications"
    COMPUTATION = "Computation"
    METHODOLOGY = "Methodology"
    MACHINE_LEARNING = "Machine Learning"
    STATISTICS_THEORY = "Statistics Theory"
