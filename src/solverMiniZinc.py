import solver

#Herite de la classe Solver, polymorphisme de la fonction solve
class SolverMiniZinc(solver.Solver):
    def __init__(self):
        super().__init__()

    def solve():
        try:
            print('minizinc')
        except Exception as e:
            print('Problème de fichier')
            print(e)

        try:
            print('minizinc')
        except Exception as e:
            print('Problème definition variable modèle')
            print(e)
