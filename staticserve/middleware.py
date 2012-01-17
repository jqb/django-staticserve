import re

class BaseStaticServe(object):
    ready = False
    url = None
    root = None
    regex_ptr = r'^%s(?P<path>.*)$'

    def import_dependencies(self):
        from django.conf import settings
        from django.views.static import serve
        return settings, serve

    def initialize(self):
        self.settings, self.serve = self.import_dependencies()
        self.url = getattr(self.settings, self.url)
        self.root = getattr(self.settings, self.root)
        self.ready = True

        # Do not change order of initialization
        self.regex_string = self.regex_ptr % self.url.lstrip('/')
        self.regex = re.compile(self.regex_string)

    def process_request(self, request):
        if not self.ready:
            self.initialize()

        if self.settings.DEBUG:
            path = request.path.lstrip('/')
            match = self.regex.search(path)
            if match:
                return self.serve(request, match.group(1), self.root, show_indexes=True)


class StaticServe(BaseStaticServe):
    url = 'STATIC_URL'
    root = 'STATIC_ROOT'


class MediaServe(BaseStaticServe):
    url = 'MEDIA_URL'
    root = 'MEDIA_ROOT'
