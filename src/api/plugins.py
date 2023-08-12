from core import Networking


class PluginsAPI(Networking):
    def families(self):
        raise NotImplementedError()

    def family_details(self):
        raise NotImplementedError()

    def plugin_details(self):
        raise NotImplementedError()
