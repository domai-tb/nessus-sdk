from core import Networking


class AgentGroupsAPI(Networking):
    def add_agent(self, group_id: int, agent_id: int) -> None:
        """
        Add an agent to the given agent group.

        Args:
            group_id (int): The id of the agent group.
            agent_id (int): The id of the agent to add.
        """

    def add_gents(self, group_id: int, agent_ids: list[int]) -> None:
        """
        Add multiple agents to the given agent group.

        Args:
            group_id (int): The id of the agent group.
            agent_ids (list[int]): Array of agent IDs to add.
        """

    def configure(self, group_id: int, name: str) -> None:
        """
        Changes the name of the given agent group.

        Args:
            group_id (int): The id of the agent group to change.
            name (str): The name for the agent group.
        """

    def create(self, name: str) -> dict:
        """
        Create an agent group.

        Args:
            name (str): The name of the agent group.

        Returns:
            dict: The details of an agent group:

                    {
                        "id": {integer},
                        "name": {string},
                        "owner_id": {string},
                        "owner": {string},
                        "shared": {integer},
                        "user_permissions": {integer},
                        "creation_date": {integer},
                        "last_modification_date": {integer}
                    }
        """
        return {}

    def delete_group(self, group_id: int) -> None:
        """
        Delete an agent group.

        Args:
            group_id (int): The id of the agent group to delete.
        """

    def delete_groups(self, group_ids: list[int]) -> None:
        """
        Delete multiple agent groups.

        Args:
            group_ids (list[int]): Array of agent group IDs to delete.
        """

    def delete_agent(self, group_id: int, agent_id: int) -> None:
        """
        Delete an agent from the given agent group.

        Args:
            group_id (int): The id of the agent group.
            agent_id (int): The id of the agent to remove.
        """

    def delete_sgents(self, group_id: int, agent_ids: list[int]) -> None:
        """
        Delete multiple agents from the given agent group.

        Args:
            group_id (int): The id of the agent group.
            agent_ids (list[int]): Array of agent IDs to delete.
        """

    def details(self, group_id: int) -> dict:
        """
        Return details for the given agent group.

        Args:
            group_id (int): The id of the agent group to query.

        Returns:
            dict: The details of an agent group:

                    {
                        "id": {integer},
                        "name": {string},
                        "owner_id": {string},
                        "owner": {string},
                        "shared": {integer},
                        "user_permissions": {integer},
                        "creation_date": {integer},
                        "last_modification_date": {integer}
                    }
        """
        return {}

    def list(self) -> dict:
        """
        Returns a list of agent groups.

        Returns:
            dict: A list with details of all agent groups:

                {
                    "groups": [ {...}, {...}, {...}, ...]
                }
        """
        return {}
