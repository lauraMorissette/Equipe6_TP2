"""Usage: python __file__ [OPTIONS]
Programme terrifiant
Un exemple minimal d'application en ligne de commande.
Par exemple, pour spécifier 15 cm de neige tombée : 
>>> python.exe -n 15

Pour rouler l'application en mode interactif, lancez la sans paramètres:
python __file__

Paramètres obligatoires:
  -n, --neige=<N>           Quantité de neige tombée en cm

Paramètres optionnels:
  -h, --help                Affiche cette documentation
  -f, --ffff                Signifier que vous êtes terrifié
  -c, --coutKM=<c>          Coût d'un camion en $/km. La valeur par défau
                            est de 2$/km
"""

import getopt
import sys
import os
import solver as solv
import problem_parking as prob_park
import solverAMPL as solv_ampl

class Usage(Exception):
   def __init__(self, msg):
      self.msg = msg

def main(argv=None):
    
    if argv is None:
        argv = sys.argv

    # :TODO: Retirer la ligne suivante qui
    # permet de visualiser le contenu de argv
    print(argv)

    params = dict()
    try:
        try:
        
            params['CM_neige'] = None

            params['coutKM'] = 2

            with open("./Data/dist1.txt", "r") as f:
                # Lire le contenu du fichier en tant que chaîne de caractères
                content = f.read()
                # Convertir la chaîne de caractères en une liste de listes
                params['distance'] = eval(content)

            with open("./Data/surf1.txt", "r") as f:
                content = f.read()
                params['surface'] = eval(content)

            with open("./Data/dist_dep1.txt", "r") as f:
                content = f.read()
                params['distance_depot'] = eval(content)

            opts, args = getopt.getopt(argv[1:],
                                    'hn:c:',
                                    ['help',
                                        'neige=',
                                        'coutkm='])

            # :TODO: Retirer la ligne suivante qui
            # permet de visualiser le contenu d'opts
            print(opts)
        
            for o, a in opts:
                if o in ("-h", "--help"):
                    print(__doc__)
                    sys.exit(0)

                elif o in ('-f', '--ffff'):
                    print("Moi Aussi.")   
                
                #TODO : Rajouter une partie pour matrice de distances

                elif o in ('-n', '--neige'):
                    if not a.isnumeric():
                        raise Usage('La quantité de neige tombée en cm doit ' +
                                     'être numérique.')
                    CM_neige= int(a)
                    if CM_neige < 0:
                        CM_neige = 0
                    params['CM_neige'] = CM_neige

                elif o in ('-c', '--coutkm'):
                    if not a.isnumeric():
                        raise Usage('Le cout par km doit être ' +
                                    'numérique.')
                    coutKM = int(a)
                    if coutKM < 0:
                        coutKM = 0
                    params['coutKM'] = coutKM
                
                else:
                    print(__doc__)
                    raise Usage('Paramètre invalide')

            # :TODO: Vérifier les paramètres obligatoires ici
            if params['CM_neige'] is None:
                raise Usage('La qantitée de neige tombée est obligatoire')

            # :TODO: Ajouter du code pour lancer les modules de traitement ici

            solveurAMPL = solv_ampl.SolverAmpl()
            probleme = prob_park.ParkingProb(params['distance'], params['distance_depot'], params['surface'],params['CM_neige'],params['coutKM'])
            print(probleme.matrice_distance)

            print(probleme.compter_nbr_surface())
            print(probleme.compter_nbr_parking())
            print(probleme.compter_nbr_distance_depot())

            a = solveurAMPL.solve(probleme)
            print(f"Voici la matrice des destinations:\n{a['X']} \nVoici la distance totale parcourue : {a['Distance totale']} km" )

            return 0

        except getopt.error as msg:
            raise Usage(msg)
        
    except Usage as err:
        print(err.msg, file=sys.stderr)
        print("Utilisez --help pour afficher la documentation", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())

