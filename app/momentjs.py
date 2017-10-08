from jinja2 import Markup


class Momentjs(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def render(self, fmt):
        return Markup("<script>\n document.write(moment('{}').{})\n</script>"
                      .format(self.timestamp.strftime("%Y-%m-%dT%H:%M:%S Z"), fmt))

    def render_format(self, fmt):
        return self.render("format({})".format(fmt))

    def render_calendar(self):
        return self.render('calendar()')

    def render_fromnow(self):
        return self.render('fromNow()')
