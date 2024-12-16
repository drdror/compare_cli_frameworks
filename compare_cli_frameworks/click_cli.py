import click

from compare_cli_frameworks import utils


@click.group()
def cli():
    """Main CLI application"""
    pass


@cli.group()
def users():
    """Users management commands"""
    pass


@cli.command()
def info():
    """Show system information."""
    click.echo(utils.sys_info())


@users.command("list")
@click.argument("group")
@click.option("--num", default=4, help="Number of users to list")
def list_users(group: str, num: int):
    """List users in the system"""
    click.echo(utils.list_users_in_group(group=group, num=num))


@users.command("msg")
@click.argument("group")
@click.argument("user")
@click.argument("msg", required=False, default="This is the default message")
@click.option("--sms", "-s", is_flag=True, help="Send the message via SMS")
def msg_to_user(group: str, user: str, msg: str, sms: bool):
    """Send a message to a user"""
    click.echo(utils.send_msg(user=user, group=group, msg=msg, sms=sms))


if __name__ == "__main__":
    cli()
