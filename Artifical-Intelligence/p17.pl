delete(1,[_|T],T).
delete(P,[X|Y],[X|R]):- P1 is P-1, delete(P1,Y,R).
