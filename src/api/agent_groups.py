from core import Networking, NErrors


class AgentGroupsAPI(Networking):
    def add_agent(self, group_id: int, agent_id: int) -> None:
        """
        Add an agent to the given agent group.

        Args:
            group_id (int): The id of the agent group.
            agent_id (int): The id of the agent to add.

        Raises:
            NErrors.NotFoundError: Raised if the object does not exist.
            NErrors.InternalServerError: Raises if an error occurred while attempting to add the agent.
        """        
        try:
            self.PUT(f'/permissions/{group_id}/agents/{agent_id}')
        except NErrors.StatusCodeError as e:
            match e.status_code:
                case 404:
                    raise NErrors.NotFoundError('Agent')
                case 500:
                    raise NErrors.InternalServerError()

    def add_gents(self, group_id: int, agent_ids: list[int]) -> None:
        """
        Add multiple agents to the given agent group.

        Args:
            group_id (int): The id of the agent group.
            agent_ids (list[int]): Array of agent IDs to add.

        Raises:
            NErrors.NotFoundError: Raised if the object does not exist.
            NErrors.InternalServerError: Raises if an error occurred while attempting to add the agent.
        """        
        try:
            self.PUT(f'/permissions/{group_id}/agents', params={agent_ids})
        except NErrors.StatusCodeError as e:
            match e.status_code:
                case 400:
                    raise NErrors.NotFoundError('One of the Agents')
                case 500:
                    raise NErrors.InternalServerError()

    def configure(self, group_id: int, name: str) -> None:
        """
        Changes the name of the given agent group.

        Args:
            group_id (int): The id of the agent group to change.
            name (str): The name for the agent group.

        Raises:
            NErrors.NotFoundError: Raised if the object does not exist.
            NErrors.InternalServerError: Raises if an error occurred while attempting to add the agent.
        """        
        try:
            self.PUT(f'/agent-groups/{group_id}', params={'name':name})
        except NErrors.StatusCodeError as e:
            match e.status_code:
                case 404:
                    raise NErrors.NotFoundError('Group')
                case 500:
                    raise NErrors.InternalServerError()

    def create(self, name: str) -> dict:
        """
        Create an agent group.

        Args:
            name (str): The name of the agent group.

        Raises:
            NErrors.NotFoundError: Raised if the object does not exist.
            NErrors.InternalServerError: Raises if an error occurred while attempting to add the agent.

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
        try:
            return dict(self.POST(f'/agent-groups', params={'name':name}))
        except NErrors.StatusCodeError as e:
            match e.status_code:
                case 400:
                    raise NErrors.NotFoundError('Field')
                case 403:
                    raise NErrors.InsufficientPermissionsError()
                case 500:
                    raise NErrors.InternalServerError()

    def delete_group(self, group_id: int) -> None:
        """
        Delete an agent group.

        Args:
            group_id (int): The id of the agent group to delete.
        """
        raise NotImplementedError()

    def delete_groups(self, group_ids: list[int]) -> None:
        """
        Delete multiple agent groups.

        Args:
            group_ids (list[int]): Array of agent group IDs to delete.
        """
        raise NotImplementedError()

    def delete_agent(self, group_id: int, agent_id: int) -> None:
        """
        Delete an agent from the given agent group.

        Args:
            group_id (int): The id of the agent group.
            agent_id (int): The id of the agent to remove.
        """
        raise NotImplementedError()

    def delete_sgents(self, group_id: int, agent_ids: list[int]) -> None:
        """
        Delete multiple agents from the given agent group.

        Args:
            group_id (int): The id of the agent group.
            agent_ids (list[int]): Array of agent IDs to delete.
        """
        raise NotImplementedError()

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
        raise NotImplementedError()

    def list(self) -> dict:
        """
        Returns a list of agent groups.

        Returns:
            dict: A list with details of all agent groups:

                {
                    "groups": [ {...}, {...}, {...}, ...]
                }
        """
        raise NotImplementedError()
