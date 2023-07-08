from dataclasses import dataclass, field


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
