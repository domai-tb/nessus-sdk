from core import Networking


class ProxyAPI(Networking):
    def change(self):
        raise NotImplementedError()

    def view(self):
        raise NotImplementedError()
