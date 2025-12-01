from puzzle_data import *
from time import time
from collections import deque
import re

def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"

class Puzzle():
    def __init__(self,input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split('\n')
    
    def process_new_input(self):           
        self.input_list = self.input_text.strip().split('\n')
        
    def p1(self):        
        self.p1_solution = 0
        self.position = 50
        self.zero_passes = 0
        print(f"Starting at {self.position} - Current count = {self.p1_solution}")
        for instruction in self.input_list:
            distance = int(instruction[1:])
            if instruction[0] == "L":
                distance *= -1
            
            while distance > 99:
                distance -= 100
                self.zero_passes +=1
                
            self.last_position = self.position
            self.position += distance
            
            if self.position == 0 or self.position == 100:                
                self.p1_solution += 1
                self.position = 0
            elif self.position < 0:
                self.position = 100 + self.position
                if self.last_position != 0:
                    self.zero_passes +=1
            elif self.position > 99:
                self.position -= 100     
                if self.last_position != 0:
                    self.zero_passes +=1
                                   
        return True

    def p2(self):
        self.p2_solution = self.p1_solution + self.zero_passes

        return True

def main():
    if P1_SAMPLE_SOLUTION:            
        print("PART 1\nTesting Sample...\n")
        start_time = time()
        sample = Puzzle(input_text=P1_SAMPLE_INPUT)
        sample.p1()
        if P1_SAMPLE_SOLUTION == sample.p1_solution:
            print("Sample correct.")
        else:
            print(f"Sample failed; Expected {P1_SAMPLE_SOLUTION}, got {sample.p1_solution}")
            quit()
        print(f"Elapsed time {elapsed_time(start_time)}")
        if PUZZLE_INPUT:
            puzzle = Puzzle(input_text=PUZZLE_INPUT)
            puzzle.p1()
            print("Processing Input...\n")
            start_time = time()
            print(f'SOLUTION: {puzzle.p1_solution}')
            print(f"Elapsed time {elapsed_time(start_time)}")
        
    if P2_SAMPLE_SOLUTION:
        print("PART 2\nTesting Sample...\n")
        start_time = time()
        if P2_SAMPLE_INPUT != False:
            sample.input_text = P2_SAMPLE_INPUT
            sample.process_new_input()
        sample.p2()
        if P2_SAMPLE_SOLUTION == sample.p2_solution:
            print("Sample correct.")
        else:
            print(f"Sample failed; Expected {P2_SAMPLE_SOLUTION}, got {sample.p2_solution}")
        print(f"Elapsed time {elapsed_time(start_time)}")
        if PUZZLE_INPUT:
            print("Processing Input...\n")
            start_time = time()
            puzzle.p2()
            print(f'SOLUTION: {puzzle.p2_solution}')
            print(f"Elapsed time {elapsed_time(start_time)}")
    
if __name__ == "__main__":
    main()