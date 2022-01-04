import re

class extraction:
    def __init__(self, mpath):
        self.mpath = mpath
        self.path = ""

    def path_update(self, filename):
        self.path = "{}/{}".format(self.mpath, filename)

    def remove_html_tags(self, text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def href_tag(self, filename):
        self.path_update(filename)
        file = open(self.path, encoding="utf8")
        text = file.read()
        x = re.findall("<a[^>]+href=\"(.*?)\"[^>]*>", text)
        return x

    def html_data(self, filename):
        self.path_update(filename)
        file = open(self.path, encoding="utf8")
        text = file.read()
        x = self.remove_html_tags(text)
        x = re.sub('[^a-zA-Z ]*', '', x)
        x = re.sub('[0-9]+', '', x)
        x = re.sub('[!@#$,;:\.""-()]', '', x)
        x = re.sub("'s", "", x)
        x = ' '.join(x.split())
        x = x.lower()
        return x

    def title_and_data(self, filename):
        self.path_update(filename)
        file = open(self.path, encoding="utf8")
        text = file.read()
        title = re.findall("<title>(.*?)</title>", text)[0]
        text = re.sub("<title>(.*?)</title>", "", text)
        x = self.remove_html_tags(text)
        x = re.sub("'s", "", x)
        x = ' '.join(x.split())
        return title, x

    def report(self, filename):
        text = self.html_data(filename)
        links = self.href_tag(filename)
        return text, links

    def keyword_clean(self, text):
        x = self.remove_html_tags(text)
        x = re.sub('[^a-zA-Z ]*', '', x)
        x = re.sub('[0-9]+', '', x)
        x = re.sub('[!@#$,;:\.""-()]', '', x)
        x = re.sub("'s", "", x)
        x = ' '.join(x.split())
        x = x.lower()
        return x

