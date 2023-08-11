from core import Networking


class MailAPI(Networking):
    def change(
        self,
        smtp_host: str,
        smtp_port: int,
        smtp_from: str,
        smtp_www_host: str,
        smtp_auth: str,
        smtp_user: str,
        smtp_pass: str,
        smtp_enc: str,
    ) -> None:
        """
        Changes the mail server settings.

        Args:
            smtp_host (str): The mail server host.
            smtp_port (int): The mail server port.
            smtp_from (str): The sender of mail messages.
            smtp_www_host (str): The host to use in email links.
            smtp_auth (str): The mail server authentication type.
            smtp_user (str): The sender's username.
            smtp_pass (str): The sender's password.
            smtp_enc (str): The encryption protocol to use.
        """
        self.PUT(
            "/settings/network/mail",
            params={
                "smtp_host": smtp_host,
                "smtp_port": smtp_port,
                "smtp_from": smtp_from,
                "smtp_www_host": smtp_www_host,
                "smtp_auth": smtp_auth,
                "smtp_user": smtp_user,
                "smtp_pass": smtp_pass,
                "smtp_enc": smtp_enc,
            },
        )

    def view(self) -> dict:
        """
        Returns the mail server settings.

        Raises:
            NErrors.UnexpectedError: An unexpected error occured.

        Returns:
            dict: JSON object of Mail settings:
                {
                    "smtp_host": {string},
                    "smtp_port": {integer},
                    "smtp_from": {string},
                    "smtp_www_host": {string},
                    "smtp_auth": {string},
                    "smtp_user": {string},
                    "smtp_pass": {string},
                    "smtp_enc": {string}
                }
        """
        return dict(self.GET("/settings/network/mail"))
