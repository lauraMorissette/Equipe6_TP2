set D;
set A;
set DEPOT;

var X {d in D, a in A} binary;
var NOMBRE_CAMION {d in D, de in DEPOT} integer >= 0 ;
var QTE_NEIGE_M3 {d in D, de in DEPOT} integer >= 0 ;



param DISTANCE_PARKING {d in D, a in A};
param LONGUEUR;
param COUT_PAR_KM;
param DISTANCE_DEPOT_KM {d in D, de in DEPOT};
param SURFACE_PARKING {d in D};
param NB_CM_NEIGE;

minimize Fct_obj: sum {d in D, a in A}X[d,a]*DISTANCE_PARKING[d,a]*COUT_PAR_KM + sum {d in D, de in DEPOT}NOMBRE_CAMION[d,de]*DISTANCE_DEPOT_KM[d,de]*COUT_PAR_KM;
subject to c1 {d in D}: sum {a in A}X[d,a]<=1;
subject to c3 {a in A}: sum {d in D}X[d,a]<=1;
subject to c2 :sum{d in D, a in A: d<>a} X[d,a] >= LONGUEUR; 
subject to c4 {d in D, a in A: d<a && a in D && d in A}: X[d,a] + X[a,d]  <= 1;

subject to c5 {d in D, de in DEPOT}: QTE_NEIGE_M3[d,de] >= (SURFACE_PARKING[d]*(NB_CM_NEIGE/100));
subject to c6 {d in D, de in DEPOT}: NOMBRE_CAMION[d,de] >= ceil((SURFACE_PARKING[d]*(NB_CM_NEIGE/100))/20);


