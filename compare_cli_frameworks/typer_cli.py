import typer

from compare_cli_frameworks import utils

app = typer.Typer()
users_app = typer.Typer()
app.add_typer(users_app, name="users")


# Main app commands
@app.command()
def info():
    """Show system information."""
    typer.echo(utils.sys_info())


# Users group commands
@users_app.command("list", help="List users in the system")
def list_users(
    group: str = typer.Argument(..., help="The group of theusers"),
    num: int = typer.Option(4, help="Number of users to list"),
):
    typer.echo(utils.list_users_in_group(group=group, num=num))


@users_app.command("msg", help="Send a message to a group member")
def msg_to_user(
    group: str = typer.Argument(help="The group of theusers"),
    user: str = typer.Argument(..., help="The user to send the message to"),
    msg: str = typer.Argument(
        default="This is the default message", help="The message to send"
    ),
    sms: bool = typer.Option(False, "--sms", "-s", help="Send the message via email"),
):
    """
    Send a message to a user
    """
    typer.echo(utils.send_msg(user=user, group=group, msg=msg, sms=sms))
    raise typer.Exit(0)


if __name__ == "__main__":
    app()
