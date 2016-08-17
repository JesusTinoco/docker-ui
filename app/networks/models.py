class Network(object):
    """
    Represent a Network
    """

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def id(self):
        return self.dictionary["Id"]

    def name(self):
        return self.dictionary["Name"]

    def driver(self):
        return self.dictionary["Driver"]
