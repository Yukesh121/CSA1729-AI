sum(1, 1).
sum(N, Sum) :-
    N > 1,
    Prev is N - 1,
    sum(Prev, PrevSum),
    Sum is PrevSum + N.
