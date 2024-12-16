import fire

from compare_cli_frameworks import utils


class UsersCLI:
    def list(self, group: str, num: int = 4):
        """
        List users in the system

        Args:
            group (str): The group of the users
            num (int, optional): Number of users to list. Defaults to 4.
        """
        print(utils.list_users_in_group(group=group, num=num))

    def msg(
        self,
        group: str,
        user: str,
        msg: str = "This is the default message",
        sms: bool = False,
    ):
        """
        Send a message to a user

        Args:
            group (str): The group of the users
            user (str): The user to send the message to
            msg (str, optional): The message to send. Defaults to "This is the default message".
            sms (bool, optional): Send the message via SMS. Defaults to False.
        """
        print(utils.send_msg(user=user, group=group, msg=msg, sms=sms))


class MainCLI:
    def __init__(self):
        self.users = UsersCLI()

    def info(self):
        """Show system information."""
        print(utils.sys_info())


def main():
    fire.Fire(MainCLI())


if __name__ == "__main__":
    main()
