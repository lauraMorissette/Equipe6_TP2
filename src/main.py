import solver as solv
import problem_parking as prob_park
import solverAMPL as solv_ampl

## TODO faire le match up avec la classe distance
with open("./Data/dist1.txt", "r") as f:
    # Lire le contenu du fichier en tant que chaîne de caractères
    content = f.read()
    # Convertir la chaîne de caractères en une liste de listes
    distance = eval(content)

with open("./Data/surf1.txt", "r") as f:
    content = f.read()
    surface = eval(content)

with open("./Data/dist_dep1.txt", "r") as f:
    content = f.read()
    distance_depot = eval(content)

CM_neige = 15
coutKM =2

solveurAMPL = solv_ampl.SolverAmpl()
probleme = prob_park.ParkingProb(distance,distance_depot,surface,CM_neige,coutKM)
print(probleme.matrice_distance)

print(probleme.compter_nbr_surface())
print(probleme.compter_nbr_parking())
print(probleme.compter_nbr_distance_depot())
try:
    probleme.valider_probleme()
except Exception as e:
    print(e)
a= solveurAMPL.solve(probleme)
print(a)