#  Hymaïa-cli

Bienvenue sur la CLI d'Hymaïa, il faut savoir que cette initiative est parti d'un délire sur nos valeurs qui formaient 
PIP avec leurs premières lettres et un collègue qui enchaine "on va créer pip install hymaia". 

Elle vous permettra d'en savoir un peu plus sur [Hymaïa](https://www.hymaia.com/) !

## Tests
Les tests sont assez sommaires pour cette première version et notamment du fait que la CLI n'a pas de fonctionnalité poussée, du moins pour le moment :) 

Pour lancer les tests :
```bash
poetry run pytest
```

## Overview de La CLI
Tout est dans le helper :
```bash
usage: hymaïa-cli [-h] [-w] [-m] [-c] [-v [VALUES]] [-j [JOIN]]

optional arguments:
  -h, --help            show this help message and exit
  -w, --why             Understand why Hymaïa exist
  -m, --manifest        Read our manifest to know what drives us
  -c, --contact         To get in touch
  -v [VALUES], --values [VALUES]
                        Get Hymaïa values
  -j [JOIN], --join [JOIN]
                        If you want to join us

```

Enjoy! 