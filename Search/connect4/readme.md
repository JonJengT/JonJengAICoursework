We have implemented a simple connect4 game.

The professor provided connect4.py and driver.py.

Our goal was to create an AI that is able to play connect4 using the minimax algorithm, alpha-beta pruning, and search depth.

I created a heuristic function that scans the board for 3 in a row. It gives ai points if they are able to get 3 in a row. In that heuristic function, I gave the ai points if it selected spaces in the middle of the board. 

This AI is not perfect, in fact I have been able to beat it a couple of times, but it is not a bad start. If I were to improve the AI, I would create better heuristics. 

to play against the ai you must be in the connect4 file and input:

python3 driver.py -x ai -o human

