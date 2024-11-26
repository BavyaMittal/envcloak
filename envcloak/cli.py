import click
from envcloak.commands.encrypt import encrypt
from envcloak.commands.decrypt import decrypt
from envcloak.commands.generate_key import generate_key
from envcloak.commands.generate_key_from_password import generate_key_from_password
from envcloak.commands.rotate_keys import rotate_keys
from envcloak.commands.compare import compare
from version_check import warn_if_outdated

#Warn About Outdated Versions
warn_if_outdated()
@click.group()
@click.version_option(prog_name="EnvCloak")
def main():
    """
    EnvCloak: Securely manage encrypted environment variables.
    """


# Add all commands to the main group
main.add_command(encrypt)
main.add_command(decrypt)
main.add_command(generate_key)
main.add_command(generate_key_from_password)
main.add_command(rotate_keys)
main.add_command(compare)


if __name__ == "__main__":
    main()
