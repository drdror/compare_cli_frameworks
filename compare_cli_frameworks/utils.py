def sys_info() -> str:
    return "System Information"


def list_users_in_group(group: str, num: int) -> str:
    return f"Listing {num} users from the group '{group}'"


def send_msg(user: str, group: str, msg: str, sms: bool) -> str:

    return (
        f"Sending the message\n✄\n{msg}\n✄\nas an "
        f"{'SMS' if sms else 'EMAIL'} to {user} from the group '{group}'"
    )


# Objective is to create a CLI that will work as follows:
#
# $ my_cli info
#
# and
#
# $ my_cli users list group_name [--num N]
#
# $ my_cli users msg group_name user_name [optional message] [--sms]
