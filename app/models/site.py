
class Sidelink:
    def __init__(self, name, link, subtitle):
        self.name     = name
        self.link     = link
        self.subtitle = subtitle

class Sidebar:
    def __init__(self, name, link, http=False):
        self.name     = name
        self.link     = link
        self.http     = http