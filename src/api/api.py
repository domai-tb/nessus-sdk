from core import Networking

from .agent_groups import AgentGroupsAPI
from .file import FileAPI
from .folders import FoldersAPI
from .mail import MailAPI
from .permissions import PermissionsAPI
from .plugins import PluginsAPI
from .proxy import ProxyAPI
from .scanners import ScannersAPI
from .scans import ScansAPI
from .server import ServerAPI
from .session import SessionAPI
from .settings import SettingsAPI
from .software_update import SoftwareUpdateAPI
from .terrascan import TerrascanAPI
from .tokens import TokensAPI
from .users import UsersAPI


class NessusAPI:
    """
    The Nessus object is the primary interaction point for users to interface with Nessus Server.
    All of the API endpoint classes that have been written will be grafted onto this class.
    """

    def __init__(
        self,
        server_url: str | None = None,
    ) -> None:
        if server_url is not None:
            Networking().base_url = server_url

    @property
    def agent_groups(self):
        """Nessus Agent Groups API Endpoint"""
        return AgentGroupsAPI()

    @property
    def files(self):
        """Nessus File API Endpoint"""
        return FileAPI()

    @property
    def folders(self):
        """Nessus Folders API Endpoint"""
        return FoldersAPI()

    @property
    def mail(self):
        """Nessus Mail API Endpoint"""
        return MailAPI()

    @property
    def permissions(self):
        """Nessus Permissions API Endpoint"""
        return PermissionsAPI()

    @property
    def plugins(self):
        """Nessus Plugins API Endpoint"""
        return PluginsAPI()

    @property
    def proxy(self):
        """Nessus Proxy API Endpoint"""
        return ProxyAPI()

    @property
    def scanners(self):
        """Nessus Scanners API Endpoint"""
        return ScannersAPI()

    @property
    def scans(self):
        """Nessus Scans API Endpoint"""
        return ScansAPI()

    @property
    def server(self):
        """Nessus Server API Endpoint"""
        return ServerAPI()

    @property
    def session(self):
        """Nessus Session API Endpoint"""
        return SessionAPI()

    @property
    def settings(self):
        """Nessus Settings API Endpoint"""
        return SettingsAPI()

    @property
    def software_update(self):
        """Nessus Software Update API Endpoint"""
        return SoftwareUpdateAPI()

    @property
    def terrascan(self):
        """Nessus Terrascan API Endpoint"""
        return TerrascanAPI()

    @property
    def tokens(self):
        """Nessus Tokens API Endpoint"""
        return TokensAPI()

    @property
    def users(self):
        """Nessus Users API Endpoint"""
        return UsersAPI()
