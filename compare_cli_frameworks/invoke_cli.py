from invoke import Collection, Program, task

from compare_cli_frameworks import utils


@task
def info(ctx):
    """Show system information."""
    print("System Information")


@task
def list_users(ctx, group: str, num: int = 4):
    """List users in the system."""
    print(utils.list_users_in_group(group=group, num=num))


@task
def msg_to_user(
    ctx,
    group: str,
    user: str,
    msg: str = "This is the default message",
    sms: bool = False,
):
    """Send a message to a user."""
    print(utils.send_msg(user=user, group=group, msg=msg, sms=sms))


# Create the namespace
namespace = Collection()

# Add the main commands
namespace.add_task(info)
namespace.add_task(list_users)
namespace.add_task(msg_to_user)

# Create a users collection
users = Collection("users")
users.add_task(list_users)
users.add_task(msg_to_user)
namespace.add_collection(users)

# Allow script to be run directly
if __name__ == "__main__":
    program = Program(namespace=namespace)
    program.run()
