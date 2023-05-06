import solver
import amplpy
import problem_parking as prob_park
import os


#Herite de la classe Solver, polymorphisme de la fonction solve
class SolverAmpl(solver.Solver):
    def __init__(self):
        super().__init__()

    def solve(self, prob=None):
        ampl_path = os.path.normpath('C:/ampl_mswin64/ampl_mswin64')
        ampl_env = amplpy.Environment(ampl_path)
        ampl = amplpy.AMPL(ampl_env)
        ampl.setOption('solver', 'gurobi')
        ampl.setOption('gurobi_options', 'timelim 600 outlev 1')

        model_dir = os.path.normpath('./src/Modele_AMPL')
        ampl.read(os.path.join(model_dir, 'TP2.mod'))
        
        ##longueur de la matrice de distance
        #longueur = prob.compter_nbr_parking()

