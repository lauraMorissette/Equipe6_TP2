include "globals.mzn";
include "alldifferent.mzn";
include "neige.dzn";

%%% ensembles
set of int: D;
set of int: A;
set of int: DEPOT;


%%% paramètres
array[D, A] of float: distance_parking;
array[D, DEPOT] of float: distance_depot_km;
array[D] of int: surface_parking;


%int: nbr_camion = max (d in D)
                      %(min (de in DEPOT) where distance_depot_km[D, DEPOT] >0);
int: division;
int: pourcent;                    
int: nbr_camion;
int: qte_neige;
int: long;
int: cout;
int: nb_neige_cm;

%%%Variables
array[D, A] of var bool: X;

array[D, DEPOT] of var 0..nbr_camion : NOMBRE_CAMION;

array[D, DEPOT] of var 0..qte_neige : QTE_NEIGE_M3;



% Contrainte c1
constraint forall(d in D) (
    sum(a in A) (X[d,a]) <= 1
);

% Contrainte c3
constraint forall(a in A) (
    sum(d in D) (X[d,a]) <= 1
);

% Contrainte c2
%constraint sum(d in D, a in A where d!=a) (X[d,a]) >= long;
constraint sum(d in D, a in A) (X[d,a]) >= long;

% Contrainte c4
%constraint forall(d in D,a in A where d<a /\ a in D /\ d in A) (
constraint forall(d in D,a in A) (
    X[d,a] + X[d,a] <= 1
    );


% Contrainte c5
constraint forall(d in D, de in DEPOT) (
    QTE_NEIGE_M3[d,de] >= (surface_parking[d] * (nb_neige_cm/pourcent))
);


% Contrainte c6
constraint forall(d in D, de in DEPOT) (
    NOMBRE_CAMION[d,de] >= ceil((surface_parking[d] * (nb_neige_cm/pourcent)) / 20)
);








% Fonction objectif
var int: Fct_obj;



constraint forall(d in D, de in DEPOT) (
    Fct_obj = sum(d in D, a in A) (X[d,a] * distance_parking[d,a] * cout) +
        sum(d in D, de in DEPOT) (NOMBRE_CAMION[d,de] * distance_depot_km[d,de] * cout)
); 

solve minimize Fct_obj;
