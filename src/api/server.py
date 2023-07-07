from core import Networking


class ServerAPI(Networking):
    def properties(self) -> dict:
        """
        Returns the server version and other properties. Nessus build and version numbers are only available with an established session.

        Returns:
            dict: JSON object of Server properties:

                    {
                        "capabilities": {
                            "multi_scanner": {boolean},
                            "multi_user": {string},
                            "report_email_config": {boolean}
                        },
                        "enterprise": {boolean},
                        "expiration": {integer},
                        "expiration_time": {integer},
                        "idle_timeout": {integer},
                        "license": {
                            "agents": {integer},
                            "expiration_date": {string},
                            "ips": {integer},
                            "scanners": {integer}
                        },
                        "loaded_plugin_set": {string},
                        "login_banner": {boolean},
                        "nessus_type": {string},
                        "nessus_ui_version": {string},
                        "notifications": [
                            {
                                "type": {string},
                                "message": {string}
                            }
                        ],
                        "plugin_set": {string},
                        "scanner_boottime": {integer},
                        "server_version": {string},
                        "server_build": {string},
                        "server_uuid": {string},
                        "terrascan_desired": {boolean},
                        "terrascan_installed": {boolean},
                        "terrascan_version": {string},
                        "update": [
                            {
                                "href": {string},
                                "new_version": {boolean},
                                "restart": {boolean}
                            }
                        ]
                    }
        """
        return self.get("/server/properties")

    def status(self) -> dict:
        """
        Returns the server status.

        Returns:
            dict: Returns the server status (loading, ready, corrupt-db, feed-expired, eval-expired, locked, register, register-locked, download-failed, feed-error).
        """
        return self.get("/server/status")

    def restart(
        self,
        reason: str = " ",
        soft: bool = False,
        unlink: bool = False,
        when_idle: bool = False,
    ) -> None:
        """
        Restarts the Nessus service and/or web server.

        Args:
            reason (str, optional): Describes the reason that the service or web server is being restarted. Defaults to " ".
            soft (bool, optional): Indicates that only the web server should be restarted and not the service. Defaults to False.
            unlink (bool, optional): Indicates whether the scanner should be unlinked from Tenable.io or Nessus Manager before restarting. Defaults to False.
            when_idle (bool, optional): Indicates that the scanner should be restarted when there are no scans currently running. Defaults to False.
        """
        self.post(
            "/server/restart",
            params={
                "reason": reason,
                "soft": soft,
                "unlink": unlink,
                "when_idle": when_idle,
            },
        )
