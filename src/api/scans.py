from core import Networking

from .models import ScanSettings


class ScansAPI(Networking):
    def attachment_prepare(
        self, scan_id: int, attachment_id: int, history_id: int = None
    ) -> dict:
        """
        Returns a single-use scan attachment token for the scan and attachment IDs.

        Args:
            scan_id (int): _description_
            attachment_id (int): _description_
            history_id (int, optional): _description_. Defaults to None.

        Returns:
            dict: Returns the 64-character single-use attachment token.
        """
        return dict(
            self.post(
                f"/scans/{scan_id}/attachments/{attachment_id}/prepare",
                params={} if history_id is None else {"history_id": history_id},
            )
        )

    def configure(
        self, scan_id: int, settings: ScanSettings, template_uuid: str = None
    ) -> dict:
        """
        Changes the schedule or policy parameters of a scan.

        Args:
            scan_id (int): The id of the scan to change.
            settings (ScanSettings): The scan settings object the hold relevant settings to configure.
            template_uuid (str, optional): The uuid for the editor template to use.. Defaults to None.

        Returns:
            dict: Configuration change:

                    {
                        "creation_date": {integer},
                        "custom_targets": {string},
                        "default_permisssions": {integer},
                        "description": {string},
                        "emails": {string},
                        "id": {integer},
                        "last_modification_date": {integer},
                        "name": {string},
                        "notification_filter_type": {string},
                        "notification_filters": {string},
                        "owner": {string},
                        "owner_id": {integer},
                        "policy_id": {integer},
                        "rrules": {string},
                        "scanner_id": {integer},
                        "shared": {integer},
                        "starttime": {string},
                        "tag_id": {integer},
                        "timezone": {string},
                        "type": {string},
                        "user_permissions": {integer},
                        "uuid": {string}
                    }
        """
        return dict(
            self.put(
                f"/scans/{scan_id}",
                params={
                    "uuid": {template_uuid},
                    "settings": {
                        "name": {settings.name},
                        "description": {settings.description},
                        "emails": {settings.emails},
                        "enabled": {settings.enabled},
                        "launch": {settings.launch},
                        "folder_id": {settings.folder_id},
                        "policy_id": {settings.policy_id},
                        "scanner_id": {settings.scanner_id},
                        "text_targets": {settings.text_targets},
                        "starttime": {settings.starttime},
                        "rrules": {settings.rrules},
                        "timezone": {settings.timezone},
                        "target_groups": {settings.target_groups},
                        "agent_groups": {settings.agent_groups},
                        "file_targets": {settings.file_targets},
                        "acls": {settings.acls},
                    },
                },
            )
        )

    def copy(self, scan_id: int, folder_id: int = None, name: str = None) -> dict:
        """
        Copies the given scan.

        Args:
            scan_id (int): The id of the scan to copy.
            folder_id (int, optional): The id of the destination folder. Defaults to None.
            name (str, optional): The name of the copied scan. Defaults to None.

        Returns:
            dict: The details of a scan.

                {
                    "id": {integer},
                    "uuid": {string},
                    "name": {string},
                    "type": {string},
                    "owner": {string},
                    "folder_id": {integer},
                    "read": {boolean},
                    "status": {string},
                    "shared": {boolean},
                    "user_permissions": {integer},
                    "creation_date": {integer},
                    "last_modification_date": {integer},
                    "control": {boolean},
                    "enabled": {boolean},
                    "starttime": {string},
                    "timezone": {string},
                    "rrules": {string}
                }
        """
        return dict(
            self.post(
                f"/scans/{scan_id}/copy",
                params={"folder_id": {folder_id}, "name": {name}},
            )
        )

    def create(self, template_uuid: str, settings: ScanSettings) -> dict:
        """
        Create a scan.

        Args:
            scan_id (int): The id of the scan to change.
            settings (ScanSettings): The scan settings object the hold relevant settings to configure.
            template_uuid (str, optional): The uuid for the editor template to use.. Defaults to None.

        Returns:
            dict: The details of a scan:

                    {
                        "scan": {
                            "creation_date": {integer},
                            "custom_targets": {string},
                            "default_permisssions": {integer},
                            "description": {string},
                            "emails": {string},
                            "id": {integer},
                            "last_modification_date": {integer},
                            "name": {string},
                            "notification_filter_type": {string},
                            "notification_filters": {string},
                            "owner": {string},
                            "owner_id": {integer},
                            "policy_id": {integer},
                            "enabled": {boolean},
                            "rrules": {string},
                            "scanner_id": {integer},
                            "shared": {integer},
                            "starttime": {string},
                            "tag_id": {integer},
                            "timezone": {string},
                            "type": {string},
                            "user_permissions": {integer},
                            "uuid": {string}
                        }
                    }
        """
        return dict(
            self.post(
                "/scans",
                params={
                    "uuid": {template_uuid},
                    "settings": {
                        "name": settings.name,
                        "description": settings.description,
                        "emails": settings.emails,
                        "enabled": settings.enabled,
                        "launch": settings.launch,
                        "folder_id": settings.folder_id,
                        "policy_id": settings.policy_id,
                        "scanner_id": settings.scanner_id,
                        "text_targets": settings.text_targets,
                        "starttime": settings.starttime,
                        "rrules": settings.rrules,
                        "timezone": settings.timezone,
                        "agent_group_id": settings.agent_groups,
                        "file_targets": settings.file_targets,
                        "acls": settings.acls,
                    },
                },
            )
        )

    def delete(self, scan_id: int) -> None:
        """
        Delete a scan. NOTE: Scans in running, paused or stopping states can not be deleted.

        Args:
            scan_id (int): The id of the scan to delete.
        """
        self.delete(f"/scans/{scan_id}")

    def delete_bulk(self, ids: list[int]) -> dict:
        """
        Delete scans in bulk. NOTE: Scans in running, paused or stopping states can not be deleted.

        Args:
            ids (list[int]): Array of scan IDs to delete.

        Returns:
            dict: JSON object:

                    {
                        "deleted": []
                    }
        """
        return dict(self.delete("/scans", params={"ids": ids}))

    def delete_history(self, scan_id: int, history_id: int) -> None:
        """
        Delete historical results from a scan.

        Args:
            scan_id (int): The id of the scan.
            history_id (int): The id of the results to delete.
        """
        self.delete(f"/scans/{scan_id}/history/{history_id}")

    def details(self, scan_id: int, history_id: int = None, limit: int = None) -> dict:
        """
        Returns details for the given scan.

        Args:
            scan_id (int): The id of the scan to retrieve.
            history_id (int, optional): The history_id of the historical data that should be returned. Defaults to None.
            limit (int, optional): The maximum number of hosts that should be returned. Defaults to None.

        Returns:
            dict: _description_
        """
        return dict(
            self.get(f"/scans/{scan_id}"),
            params={"history_id": history_id, "limit": limit},
        )

    def export_formats(self, scan_id: int, schedule_id: int) -> dict:
        """
        Returns available export formats and report options.

        Args:
            scan_id (int): The ID of the scan to export.
            schedule_id (int): The ID for the schedule that the scan is associated with.

        Returns:
            dict: Report Options as JSON Object:

                    {
                        "report_options": {
                            "formattingOptions": [
                                {
                                    "name": "Page Breaks",
                                    "key": "page_breaks"
                                }
                            ],
                            "csvColumns": [
                                {
                                    "isDefault": true,
                                    "key": "id",
                                    "name": "Plugin ID"
                                },
                                {
                                    "name": "CVE",
                                    "key": "cve",
                                    "isDefault": true
                                },
                                {
                                    "name": "Plugin ID",
                                    "key": "id",
                                    "isDefault": true
                                },
                                {
                                    "name": "CVE",
                                    "key": "cve",
                                    "isDefault": true
                                },
                                {
                                    "name": "CVSS v2.0 Base Score",
                                    "key": "cvss",
                                    "isDefault": true
                                },
                                {
                                    "name": "Risk",
                                    "key": "risk",
                                    "isDefault": true
                                },
                                {
                                    "name": "Host",
                                    "key": "hostname",
                                    "isDefault": true
                                },
                                {
                                    "name": "Protocol",
                                    "key": "protocol",
                                    "isDefault": true
                                },
                                {
                                    "name": "Port",
                                    "key": "port",
                                    "isDefault": true
                                },
                                {
                                    "name": "Name",
                                    "key": "plugin_name",
                                    "isDefault": true
                                },
                                {
                                    "name": "Synopsis",
                                    "key": "synopsis",
                                    "isDefault": true
                                },
                                {
                                    "name": "Description",
                                    "key": "description",
                                    "isDefault": true
                                },
                                {
                                    "name": "Solution",
                                    "key": "solution",
                                    "isDefault": true
                                },
                                {
                                    "name": "See Also",
                                    "key": "see_also",
                                    "isDefault": true
                                },
                                {
                                    "name": "Plugin Output",
                                    "key": "plugin_output",
                                    "isDefault": true
                                },
                                {
                                    "name": "STIG Severity",
                                    "key": "stig_severity",
                                    "isDefault": false
                                },
                                {
                                    "name": "CVSS v3.0 Base Score",
                                    "key": "cvss3_base_score",
                                    "isDefault": false
                                },
                                {
                                    "name": "CVSS v2.0 Temporal Score",
                                    "key": "cvss_temporal_score",
                                    "isDefault": false
                                },
                                {
                                    "name": "CVSS v3.0 Temporal Score",
                                    "key": "cvss3_temporal_score",
                                    "isDefault": false
                                },
                                {
                                    "name": "Risk Factor",
                                    "key": "risk_factor",
                                    "isDefault": false
                                },
                                {
                                    "name": "References",
                                    "detailColumns": [
                                        {
                                            "name": "BID",
                                            "key": "bid"
                                        },
                                        {
                                            "name": "XREF",
                                            "key": "xref"
                                        },
                                        {
                                            "name": "MSKB",
                                            "key": "mskb"
                                        }
                                    ],
                                    "key": "references",
                                    "isDefault": false
                                },
                                {
                                    "name": "Plugin Information",
                                    "detailColumns": [
                                        {
                                            "name": "Plugin Publication Date",
                                            "key": "plugin_publication_date"
                                        },
                                        {
                                            "name": "Plugin Modification Date",
                                            "key": "plugin_modification_date"
                                        }
                                    ],
                                    "key": "plugin_information",
                                    "isDefault": false
                                },
                                {
                                    "name": "Exploitable With",
                                    "detailColumns": [
                                        {
                                            "name": "Metasploit",
                                            "key": "exploit_framework_metasploit"
                                        },
                                        {
                                            "name": "Core Impact",
                                            "key": "exploit_framework_core"
                                        },
                                        {
                                            "name": "CANVAS",
                                            "key": "exploit_framework_canvas"
                                        }
                                    ],
                                    "key": "exploitable_with",
                                    "isDefault": false
                                }
                            ]
                        },
                        "formats": {
                            "custom": [],
                            "export": [
                                {
                                    "name": "Nessus",
                                    "value": "nessus"
                                },
                                {
                                    "name": "Nessus DB",
                                    "value": "db"
                                }
                            ],
                            "format": [
                                {
                                    "name": "PDF",
                                    "value": "pdf"
                                },
                                {
                                    "name": "HTML",
                                    "value": "html"
                                },
                                {
                                    "name": "CSV",
                                    "value": "csv"
                                }
                            ]
                        }
                    }
        """
        return dict(
            self.get(
                f"/scans/{scan_id}/export/formats", params={"schedule_id": schedule_id}
            )
        )

    def export_download(self, scan_id: int, file_id: int) -> str:
        """
        Download an exported scan.

        Args:
            scan_id (int): The id of the scan to export.
            file_id (int): The id of the file to download (Included in response from /scans/{scan_id}/export).

        Returns:
            str: Returns the content of the file as an attachment.
        """
        return str(self.get(f"/scans/{scan_id}/export/{file_id}/download"))

    def export_request(self):
        raise NotImplementedError()

    def export_status(self, scan_id: int, file_id: int) -> dict:
        """
        Check the file status of an exported scan. When an export has been requested, it is necessary to
        poll this endpoint until a "ready" status is returned, at which point the file is complete and can
        be downloaded using the export download endpoint.

        Args:
            scan_id (int): The id of the scan to export.
            file_id (int): The id of the file to poll (Included in response from /scans/{scan_id}/export).

        Returns:
            dict: Returns the status of the file. A status of "ready" indicates the file can be downloaded.

                    {
                        "status": {string}
                    }
        """
        return dict(self.get(f"/scans/{scan_id}/export/{file_id}/status"))

    def host_details(self, scan_id: int, host_id: int, history_id: int = None) -> dict:
        """
        Returns details for the given host.

        Args:
            scan_id (int): The id of the scan to retrieve.
            host_id (int): The id of the host to retrieve.
            history_id (int, optional): The history_id of the historical data that should be returned. Defaults to None.

        Returns:
            dict: Returns the host details.

                    {
                        "info": {
                            "host_start": {string},
                            "mac-address": {string},
                            "host-fqdn": {string},
                            "host_end": {string},
                            "operating-system": {string},
                            "host-ip": {string}
                        },
                        "compliance": [
                            host_compliance Resource
                        ],
                        "vulnerabilities": [
                            host_vulnerability Resource
                        ]
                    }
        """
        return dict(
            self.get(
                f"/scans/{scan_id}/hosts/{host_id}", params={"history_id": history_id}
            )
        )

    def import_scan(
        self, scan_file: str, folder_id: int = None, password: str = None
    ) -> dict:
        """
        Import an existing scan uploaded using file: upload.

        Args:
            scan_file (str): The name of the file to import as provided by the response from file: upload.
            folder_id (int, optional): The id of the destination folder. If not specified, the default folder will be used. Defaults to None.
            password (str, optional): The password for the file to import (required for nessus.db). Defaults to None.

        Returns:
            dict: Returns the scan object.
        """
        return dict(
            self.post(
                "/scans/import",
                params={
                    "file": scan_file,
                    "folder_id": folder_id,
                    "password": password,
                },
            )
        )

    def kill(self, scan_id: int) -> None:
        """
        For use on scans from the local scanner only, "kill" terminates a scan faster than "stop".
        All in-progress plugins are terminated. A scan can be killed with the scan in any state.

        Args:
            scan_id (int): The id of the scan to kill.
        """
        self.post(f"/scans/{scan_id}/kill")

    def launch(self, scan_id: int, alt_targets: list[str] = None) -> dict:
        """
        Launches a scan.

        Args:
            scan_id (int): The id of the scan to launch.
            alt_targets (list[str]): If specified, these targets will be scanned instead of the default.
                                     Value can be an array where each index is a target, or an array with a
                                     single index of comma separated targets. Defaults to None.

        Returns:
            dict: Scan UUID if the scan was successfully launched.

                    {
                        "scan_uuid": {string}
                    }
        """
        return dict(
            self.post(f"/scans/{scan_id}/launch", params={"alt_targets": alt_targets})
        )

    def list_scans(
        self, folder_id: int = None, last_modification_date: int = None
    ) -> dict:
        """
        Returns the scan list.

        Args:
            folder_id (int, optional): The id of the folder whose scans should be listed. Defaults to None.
            last_modification_date (int, optional): Limit the results to those that have only changed since this time. Defaults to None.

        Returns:
            dict: Returns the scan list.

                    {
                        "folders": [...],
                        "scans": [...],
                        "timestamp": {integer}
                    }
        """
        return dict(
            self.get(
                "/scans",
                params={
                    "folder_id": folder_id,
                    "last_modification_date": last_modification_date,
                },
            )
        )

    def pause(self, scan_id: int) -> None:
        """
        Pauses a scan.

        Args:
            scan_id (int): The id of the scan to pause.
        """
        self.post(f"/scans/{scan_id}/pause")

    def plugin_output(
        self, scan_id: int, host_id: int, plugin_id: int, history_id: int = None
    ) -> dict:
        """
        Returns the output for a given plugin.

        Args:
            scan_id (int): The id of the scan to retrieve.
            host_id (int): The id of the host to retrieve.
            plugin_id (int): The id of the plugin to retrieve.
            history_id (int, optional): The history_id of the historical data that should be returned. Defaults to None.

        Returns:
            dict: Returns the plugin output.

                    {
                        "info": {
                            "plugindescription": {
                                "severity": {integer},
                                "pluginname": {string},
                                "pluginattributes": {
                                    "risk_information": {
                                        "risk_factor": {string}
                                    },
                                    "plugin_name": {string},
                                    "plugin_information": {
                                        "plugin_id": {integer},
                                        "plugin_type": {string},
                                        "plugin_family": {string},
                                        "plugin_modification_date": {string}
                                    },
                                    "solution": {string},
                                    "fname": {string},
                                    "synopsis": {string},
                                    "description": {string}
                                },
                                "pluginfamily": {string},
                                "pluginid": {integer}
                            }
                        },
                        "output": [
                            plugin_output Resource
                        ]
                    }
        """
        return dict(
            self.get(
                f"/scans/{scan_id}/hosts/{host_id}/plugins/{plugin_id}",
                params={"history_id": history_id},
            )
        )

    def read_status(self, scan_id: int, read: bool) -> None:
        """
        Changes the status of a scan.

        Args:
            scan_id (int): The id of the scan to change.
            read (bool): If true, the scan has been read.
        """
        self.put(f"/scans/{scan_id}/status", params={"read": read})

    def resume(self, scan_id: int) -> None:
        """
        Resumes a scan.

        Args:
            scan_id (int): The id of the scan to resume.
        """
        self.post(f"/scans/{scan_id}/resume")

    def schedule(self, scan_id: int, enabled: bool) -> dict:
        """
        Enables or disables a scan schedule.

        Args:
            scan_id (int): The id of the scan.
            enabled (bool): Enables or disables the scan schedule.

        Returns:
            dict: JSON object:

                    {
                        "enabled": true,
                        "control": true,
                        "rrules": {string},
                        "starttime": {string},
                        "timezone": {string}
                    }
        """
        return dict(self.put(f"/scans/{scan_id}/schedule", params={"enabled": enabled}))

    def stop(self, scan_id: int) -> None:
        """
        Stops a scan.

        Args:
            scan_id (int): The id of the scan to stop.
        """
        self.post(f"/scans/{scan_id}/stop")

    def timezones(self) -> dict:
        """
        Returns the timezone list for creating a scan.

        Returns:
            dict: Returns the timezone list.

                    {
                        "timezones": [
                            timezone Resource
                        ]
                    }
        """
        return dict(self.get("/scans/timezones"))
