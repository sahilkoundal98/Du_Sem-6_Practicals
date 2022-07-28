
app([],L,L).
app([X|L1],L2,[X|L3]):- app(L1,L2,L3).
palindrome([]).
palindrome([_]).
palindrome(Plist):-app([H|T],[H],Plist),palindrome(T).
