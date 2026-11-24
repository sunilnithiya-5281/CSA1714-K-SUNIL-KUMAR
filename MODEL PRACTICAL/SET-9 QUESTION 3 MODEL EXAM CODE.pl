
% Family Relationship Database

% Facts
male(raju).
male(arun).
male(bala).
male(kumar).

female(latha).
female(priya).
female(divya).
female(chitra).

% Parent relationships
father(raju, arun).
father(raju, priya).
father(kumar, bala).
father(kumar, divya).

mother(latha, arun).
mother(latha, priya).
mother(chitra, bala).
mother(chitra, divya).

% Brother relationship
brother(X, Y) :-
    male(X),
    father(F, X),
    father(F, Y),
    X \= Y.

% Sister relationship
sister(X, Y) :-
    female(X),
    father(F, X),
    father(F, Y),
    X \= Y.

% Uncle relationship
uncle(X, Y) :-
    brother(X, P),
    (father(P, Y); mother(P, Y)).

% Aunt relationship
aunt(X, Y) :-
    sister(X, P),
    (father(P, Y); mother(P, Y)).

% Cousin relationship
cousin(X, Y) :-
    father(F1, X),
    father(F2, Y),
    brother(F1, F2),
    X \= Y.

% Queries
% ?- father(raju, arun).
% ?- mother(latha, priya).
% ?- brother(arun, priya).
% ?- sister(priya, arun).
% ?- uncle(arun, bala).
% ?- aunt(priya, bala).
% ?- cousin(arun, bala).
