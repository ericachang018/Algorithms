#function that will run the hanoi solver and gather the number of rings needed. 

import model
import view

def run_hanoi():
	print "Hi this is my Tower's of Hanoi Solver"
	number_of_rings = int(raw_input("Pick the number of rings in this game. 1-10: "))
	hanoi = model.Hanoi(number_of_rings)
	hanoi.solve()
	view.display_moves(hanoi.moves)

