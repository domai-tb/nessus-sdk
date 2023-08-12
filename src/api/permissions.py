from core import Networking, NErrors
from .models import Permission

class PermissionsAPI(Networking):
    def change(self, object_type: str, object_id: int, permissions: list[Permission]) -> None:
        """
        Changes the permissions for an object.

        Args:
            object_type (str): The type of object.
            object_id (int): The unique id of the object.
            permissions (list[Permissions]): An array of Permissions to apply to the object.

        Raises:
            NErrors.InsufficientPermissionsError: Raised if the user does not have permission to edit the object.
            NErrors.NotFoundError: Raised if the object does not exist.
        """        
        try:
            self.PUT(f'/permissions/{object_type}/{object_id}', params={'acls':[p.to_dict() for p in permissions]})
        except NErrors.StatusCodeError as e:
            match e.status_code:
                case 403:
                    raise NErrors.InsufficientPermissionsError()
                case 404:
                    raise NErrors.NotFoundError(f'{object_type} (ID: {object_id})')

    def list_permissions(self, object_type: str, object_id: int) -> dict:
        """
        Returns the current object's permissions.

        Args:
            object_type (str): The type of object.
            object_id (int): The unique id of the object.

        Raises:
            NErrors.InsufficientPermissionsError: Raised if the user does not have permission to edit the object.
            NErrors.NotFoundError: Raised if the object does not exist.

        Returns:
            dict: Returns the object permissions.

                    {
                        "owner": {integer},
                        "type": {string},
                        "permissions": {integer},
                        "id": {integer},
                        "name": {string}
                    }
        """        
        try:
            return dict(self.GET(f'/permissions/{object_type}/{object_id}'))
        except NErrors.StatusCodeError as e:
            match e.status_code:
                case 403:
                    raise NErrors.InsufficientPermissionsError()
                case 404:
                    raise NErrors.NotFoundError(f'{object_type} (ID: {object_id})')