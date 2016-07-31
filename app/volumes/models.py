class Volume(object):
    """
    Represent a Volume
    """

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def mount_point(self):
        return self.dictionary["Mountpoint"]

    def driver(self):
        return self.dictionary["Driver"]

    def label(self):
        return self.dictionary["Labels"]

    def name(self):
        return self.dictionary["Name"]
