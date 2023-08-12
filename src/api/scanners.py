from core import Networking


class ScannersAPI(Networking):
    def control_scans(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()

    def delete_bulk(self):
        raise NotImplementedError()

    def details(self):
        raise NotImplementedError()

    def edit(self):
        raise NotImplementedError()

    def get_aws_targets(self):
        raise NotImplementedError()

    def get_scanner_key(self):
        raise NotImplementedError()

    def get_scans(self):
        raise NotImplementedError()

    def list_scanners(self):
        raise NotImplementedError()

    def toggle_link_state(self):
        raise NotImplementedError()
