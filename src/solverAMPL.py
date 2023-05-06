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
        longueur = prob.compter_nbr_parking()
        print(prob.matrice_distance)
        try:

            D = list(range(2,longueur+2))
            A = list(range(2,longueur+2))
            DEPOT = [1]

            df = amplpy.DataFrame('D')
            df.set_column('D', D)
            ampl.setData(df, 'D')

            df = amplpy.DataFrame('A')
            df.set_column('A', A)
            ampl.setData(df, 'A')

            df = amplpy.DataFrame('DEPOT')
            df.set_column('DEPOT', DEPOT)
            ampl.setData(df, 'DEPOT')

            df = amplpy.DataFrame(('D','A'), 'DISTANCE_PARKING')
            df.setValues({
                (depart, arrive): prob.matrice_distance[i][j]
                for i, depart in enumerate(D)
                for j, arrive in enumerate(A)
            })
            ampl.setData(df)

            df = amplpy.DataFrame(('D','DEPOT'), 'DISTANCE_DEPOT_KM')
            df.setValues({
                (depart, arrive): prob.matrice_depot[i][j]
                for i, depart in enumerate(D)
                for j, arrive in enumerate(DEPOT)
            })
            ampl.setData(df)

            df = amplpy.DataFrame(('D'), 'SURFACE_PARKING')
            df.setValues({
                (depart): prob.matrice_surface[i]
                for i, depart in enumerate(D)
            })
            ampl.setData(df)

            ampl.getParameter('LONGUEUR').set(longueur)
            ampl.getParameter('COUT_PAR_KM').set(prob.cm_neige)
            ampl.getParameter('NB_CM_NEIGE').set(prob.cout_KM)

            
            ampl.solve()
            return ampl


        except Exception as e:
            print(e)
        

