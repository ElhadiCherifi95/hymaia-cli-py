import configparser


class Command:
    config = configparser.ConfigParser()
    config.read('hymaia_cli/resources/config.properties')
    base_url = config['aws.api-gateway']['url']

    def __init__(self, name: str, url_parameter: str):
        self.name: str = name
        self.url_parameter: str = url_parameter
        self.url: str = Command.base_url + self.url_parameter

    def get_url_with_parameter(self):
        return self.base_url, self.url_parameter


class ParametrizedCommand(Command):
    def __init__(self, commands, url_parameter, name):
        super().__init__(name, url_parameter)
        self.commands: list[Command] = commands

    def get_commands(self):
        return self.commands
