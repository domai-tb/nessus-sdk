from dataclasses import dataclass, field, asdict


@dataclass
class ScanSettings:
    name: str
    text_targets: str
    description: str = ""
    policy_id: int = None
    folder_id: int = None
    scanner_id: int = None
    enabled: bool = True
    launch: str = ""
    starttime: str = ""
    rrules: str = ""
    timezone: str = ""
    target_groups: list[int] = field(default_factory=lambda: [])
    agent_groups: list[int] = field(default_factory=lambda: [])
    emails: str = ""
    acls: str = ""
    file_targets: str = ""


@dataclass
class Permission:
    name: str               # The unique id of the owner of the object.
    owner: int              # The type of permission (default, user, group).
    permission_type: str    # The permission value (0, 16, 32, 64) 
    permissions: int        # The unique id of the user if type is user.
    permission_id: int      # The name of the user or group.

    def to_dict(self) -> dict:
        return asdict(self)