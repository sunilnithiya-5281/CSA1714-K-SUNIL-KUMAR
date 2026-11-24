
% Inference Engine using Prolog

% Facts
human(ram).
human(raju).
human(arun).

male(ram).
male(raju).

female(priya).

% Rules
mortal(X) :-
    human(X).

father(ram, raju).
father(raju, arun).

parent(X, Y) :-
    father(X, Y).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Inference queries
prove(Query) :-
    call(Query),
    write('Query is PROVED').

prove(Query) :-
    \+ call(Query),
    write('Query is NOT PROVED').

% Example Queries
% ?- prove(human(ram)).
% ?- prove(mortal(raju)).
% ?- prove(grandparent(ram, arun)).
% ?- prove(human(priya)).
