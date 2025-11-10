class Pet(object):
    def __init__(self, name, species, description):
        self.name = name
        self.species = species
        self.description = description

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def get_description(self):
        return self.description
    
    def describe(self):
            return f"{self.name} is a {self.species}. {self.description}."
    
    def set_name(self, name):
        self.name = name
     
    def set_species(self, species):
        self.species = species
     
    def set_description(self, description):
        self.description = description