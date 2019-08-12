import click
from parsec.commands.quotas.create_quota import cli as create_quota
from parsec.commands.quotas.delete_quota import cli as delete_quota
from parsec.commands.quotas.get_quotas import cli as get_quotas
from parsec.commands.quotas.show_quota import cli as show_quota
from parsec.commands.quotas.undelete_quota import cli as undelete_quota
from parsec.commands.quotas.update_quota import cli as update_quota


@click.group()
def cli():
    pass


cli.add_command(create_quota)
cli.add_command(delete_quota)
cli.add_command(get_quotas)
cli.add_command(show_quota)
cli.add_command(undelete_quota)
cli.add_command(update_quota)
