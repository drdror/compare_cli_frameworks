import argparse

from compare_cli_frameworks import utils


def info_command(args):
    """Show system information."""
    print(utils.sys_info())


def list_users_command(args):
    """List users in the system"""
    print(utils.list_users_in_group(group=args.group, num=args.num))


def msg_to_user_command(args):
    """Send a message to a user"""
    print(utils.send_msg(user=args.user, group=args.group, msg=args.msg, sms=args.sms))


def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser(description="Main CLI application")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    subparsers.required = True

    # Info command
    info_parser = subparsers.add_parser("info", help="Show system information")
    info_parser.set_defaults(func=info_command)

    # Users subcommand group
    users_parser = subparsers.add_parser("users", help="Users management commands")
    users_subparsers = users_parser.add_subparsers(dest="users_command")
    users_subparsers.required = True

    # Users list subcommand
    list_parser = users_subparsers.add_parser("list", help="List users in the system")
    list_parser.add_argument("group", help="Group to list users from")
    list_parser.add_argument(
        "--num", type=int, default=4, help="Number of users to list (default: 4)"
    )
    list_parser.set_defaults(func=list_users_command)

    # Users msg subcommand
    msg_parser = users_subparsers.add_parser("msg", help="Send a message to a user")
    msg_parser.add_argument("group", help="User's group")
    msg_parser.add_argument("user", help="Username to send message to")
    msg_parser.add_argument(
        "msg",
        nargs="?",
        default="This is the default message",
        help="Message to send (optional)",
    )
    msg_parser.add_argument(
        "--sms", "-s", action="store_true", help="Send the message via SMS"
    )
    msg_parser.set_defaults(func=msg_to_user_command)

    # Parse arguments and call the appropriate function
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
