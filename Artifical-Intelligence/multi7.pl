multi(N,1,N).
multi(N,M,A):-
T is M-1,
multi(N,T,Y),
A is Y+N.
