class Phrase:
    def __init__(self, components):
        self.components = components

    def __str__(self):
        output = ''
        for comp in self.components:
            output += str(comp)
        return output
