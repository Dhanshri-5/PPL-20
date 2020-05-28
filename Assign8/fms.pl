
airport(pune,50,30).
airport(mumbai,75,20).
airport(kolkata,75,25).
airport(jaipur,40,20).
airport(goa,50,15).


flight(pune,kolkata,united,1950,440).
flight(pune,kolkata,airIndia,1800,480).
flight(pune,kolkata,jetairways,1900,400).

flight(pune,mumbai,jetairways,500,80).
flight(pune,mumbai,united,650,90).
flight(pune,mumbai,airindia,600,100).

flight(kolkata, mumbai, jetairways, 1200, 240).
flight(kolkata,jaipur,jetairWays,1100,200).
flight(kolkata,jaipur,airIndia,1120,220).
flight(kolkata,goa,airIndia,950,180).

flight(mumbai,kolkata,airIndia,1100,250).
flight(mumbai,kolkata,united,800,300).
flight(mumbai,jaipur,airIndia,720,240).


/*To list down all airports with their tax ,  delay.*/
getairport(X) :-
	airport(X,Y,Z),
	format('~w airport taxes you $~w with delay of ~w mins.~n',[X,Y,Z]).

/* To display the flights of particular airlines*/
airlines(X):-
    flight(A,B,X,D,E),
    format('Fight : ~w - ~w    price:$~w    Duration: ~w minutes.',[A,B,D,E]).

/*To display all DIRECT the available flights with their name , cost,duration./   
getallflights(A, B) :-
    flight(A,B,C,D,E),
    format('Direct flight from ~w to\" ~w by \" ~w  will cost you $~w and take ~w minutes.',[A,B,C,D,E]).

/*To check if there exist a cheap flight between city A and B.*/
getcheapflight(A, B):-
    flight(A,B,C,D,E), 
    D < 900,
    format('Direct flight from ~w to\" ~w by \" ~w  will cost you $~w (less than $900) and take ~w minutes.',[A,B,C,D,E]).  


/*To check if it is possible to reach from A to B by INDIRECT flights.*/
getindirectflight(A,B) :-
    flight(A,X,C,D,E),
    flight(X,B,P,Q,R),
    format('Joining flights from ~w to ~w via ~w ~nFight 1 : ~w - ~w    BY:~w    price:$~w    Duration: ~w minutes.~nFight 2 : ~w - ~w    BY:~w    price:$~w    Duration: ~w minutes.',[A,B,X,A,X,C,D,E,X,B,P,Q,R]).

/*Query to check if there is a preferable flight between X,Y depending on time*/
cmptime(A,B,X,Y):-
    flight(A,B,X,D,E) , flight(A,B,Y,P,Q),
    Z is abs((E-Q)),
    format('~w :~wmins  ~w:~wmins   Time difference of ~w minutes.',[X,E ,Y,Q,Z]).
    
/*Query to check if there is a preferable flight between X,Y depending on price*/
cmpprice(A,B,X,Y):-
    flight(A,B,X,D,E) , flight(A,B,Y,P,Q),
    Z is abs((D - P)),
    format('~w : $~w  ~w: $~w   Price difference of $~w.',[X,D ,Y,P,Z]).
   


















