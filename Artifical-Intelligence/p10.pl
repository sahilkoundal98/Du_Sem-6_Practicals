reverse_list(Inputlist,Outputlist):-
reverse_list(Inputlist,[],Outputlist).
reverse_list([],Outputlist,Outputlist).
reverse_list([Head|Tail],List1,List2):-
reverse_list(Tail,[Head|List1],List2).
