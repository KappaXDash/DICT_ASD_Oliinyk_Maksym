class Spider:
    """All methods which needs personally to spiders"""
    name: str  # spiders name
    species: str  # spider species
    color: str  # horse gender
    age: int  # spiders age
    weight: float  # horse height in hands
    category: str
    areal: str

    def __init__(self, name: str, breed: str, age: int, color: str, weight: float,  category: str, areal: str) -> None:
        """Constructor of the class to set up all basic variables"""
        self.name = name
        self.species = breed
        self.color = color
        self.age = age
        self.weight = weight
        self.category = category
        self.areal = areal
    def get_info(self) -> str:
        """String representation of the object"""
        return f"Horse({self.name}, {self.species}, {self.color}, {self.age}, {self.weight}, {self.category},{self.areal})"

    def __repr__(self) -> str:
        """String representation of the object"""
        return f"Horse({self.name}, {self.species}, {self.color}, {self.age}, {self.weight},{self.category},{self.areal})"