import argparse
import requests

from hymaia_cli.command.hymaia_cli_commands import HymaiaCliCommands
from hymaia_cli.utils.utils import print_content


def get_ascii_title():
    # Format Slant
    return """
                                                                       
,--.  ,--.                           ,--.                     ,--.,--. 
|  '--'  |,--. ,--.,--,--,--. ,--,--.`--' ,--,--.,-----. ,---.|  |`--' 
|  .--.  | \  '  / |        |' ,-.  |,--.' ,-.  |'-----'| .--'|  |,--. 
|  |  |  |  \   '  |  |  |  |\ '-'  ||  |\ '-'  |       \ `--.|  ||  | 
`--'  `--'.-'  /   `--`--`--' `--`--'`--' `--`--'        `---'`--'`--' 
          `---'                                                        
                             
"""


class VerboseStore(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        if not values:
            for command in getattr(HymaiaCliCommands(), self.dest).get_commands():
                print(command.name, sep="\n")
        else:
            setattr(namespace, self.dest, values)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='hymaïa-cli',
                                     description=print(get_ascii_title()),
                                     allow_abbrev=False,
                                     epilog='Enjoy our CLI! :)')
    parser.add_argument("-w", "--why", help="understand why Hymaïa exist", action="store_true")
    parser.add_argument("-m", "--manifest", help="read our manifest to know what drives us", action="store_true")
    parser.add_argument("-c", "--contact", help="to get in touch", action="store_true")
    parser.add_argument("-v", "--values", help="Get Hymaïa values", action=VerboseStore, nargs="?")
    parser.add_argument("-j", "--join", help="If you want to join us", action=VerboseStore, nargs="?")
    parsed_args = parser.parse_args()

    for k, v in vars(parsed_args).items():
        if v:
            attribute = v
            if isinstance(v, bool):
                attribute = k
            url, parameter = getattr(HymaiaCliCommands(), attribute).get_url_with_parameter()
            response = requests.get(url=url, params={'command': parameter})
            if response.status_code != 200:
                print("Oups! Something get wrong")
            else:
                print_content(response.json())