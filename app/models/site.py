
class Sidelink:
    def __init__(self, name, link, subtitle, http=False, css_classes='sidelink', onclick=''):
        self.name        = name
        self.link        = link
        self.subtitle    = subtitle
        self.http        = http
        self.css_classes = css_classes
        self.onclick     = onclick

class Sidebar:
    def __init__(self, name, link, http=False):
        self.name     = name
        self.link     = link
        self.http     = http