from core import Networking


class FoldersAPI(Networking):
    def create(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()

    def edit(self):
        raise NotImplementedError()

    def list_folders(self):
        raise NotImplementedError()
