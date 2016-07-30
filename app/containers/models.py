import re
from datetime import datetime


class Container(object):
    """
    Represent a Container
    """

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def id(self):
        return self.dictionary["Id"]

    def short_id(self):
        return self.dictionary["Id"][:12]

    def image(self):
        return self.dictionary["Image"]

    def command(self):
        return self.dictionary["Command"]

    def status(self):
        return self.dictionary["Status"]

    def state(self):
        return self.dictionary["State"]

    def ports(self):
        return self.dictionary["Ports"]

    def name(self):
        return self.dictionary["Names"][0][1:]

    def created(self):
        return self.dictionary["Created"]

    # TODO: Have to check this method


class ContainerInspect(object):

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def id(self):
        return self.dictionary["Id"]

    def short_id(self):
        return self.dictionary["Id"][:12]

    def config(self):
        return self.dictionary["Config"]

    def name(self):
        return self.dictionary["Name"][1:]

    def hostname(self):
        return self.dictionary["Config"]["Hostname"]

    def domain_name(self):
        return self.dictionary["Config"]["Domainname"]

    def working_dir(self):
        return self.dictionary["Config"]["WorkingDir"]

    def env(self):
        return self.dictionary["Config"]["Env"]

    def user(self):
        return self.dictionary["Config"]["User"]

    def image(self):
        return self.config()["Image"]

    def ports(self):
        return self.dictionary["NetworkSettings"]["Ports"]

    def networks(self):
        return self.dictionary["NetworkSettings"]["Networks"]

    def links(self):
        networks = self.networks()
        links = networks[networks.keys()[0]]["Links"]
        result = None;
        if links:
            result = []
            for link in links:
                names = link.split(':')
                result.append(dict(container_name=names[0], link_name=names[1]))
        return result

    def mounts(self):
        return self.dictionary["Mounts"]

    def status(self):
        return self.dictionary["State"]["Status"]

    def command(self):
        return self.dictionary["Config"]["Cmd"]

    def created(self):
        return self.dictionary["Created"]

    def human_readable_duration(self):
        parsedDate = list(map(int, re.findall(r"[\d]+", str(self.dictionary["Created"]))))
        date = datetime(parsedDate[0],
                        parsedDate[1],
                        parsedDate[2],
                        parsedDate[3],
                        parsedDate[4],
                        parsedDate[5])
        now = datetime.now()
        duration = now - date
        if duration.seconds < 1:
            return "Less than a second"
        elif duration.seconds < 60:
            return "%s seconds" % str(duration.seconds)
        elif duration.seconds / 60 < 60:
            return "%s minutes" % str(duration.seconds/60)
        elif duration.seconds/60/60 == 1:
            return "About an hour"
        elif duration.seconds/60/60 < 48:
            return "%s hours" % str(duration.seconds/60/60)
        elif duration.days < 7:
            return "%s days" % str(duration.days)
        elif duration.days < 30:
            return "%s weeks" % str(duration.days/7)
        elif duration.days < 365:
            return "%s months" % str(duration.days/30)
        return "%s years" % str(duration.days/365)
