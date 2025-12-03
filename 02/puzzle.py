from puzzle_data import *
from time import time
import re

def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"

class Puzzle():
    def __init__(self,input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split(',')
    
    def process_new_input(self):           
        self.input_list = self.input_text.strip().split(',')
        
    def p1(self):
        self.p1_solution = 0
        for r in self.input_list:
            this_range = r.split('-')
            start, end = int(this_range[0]),int(this_range[1])
            for value in range(start,end+1):
                valstr = str(value)
                vallen = len(valstr)
                if vallen%2 == 0:
                    half = vallen//2
                    first_half = valstr[0:half]
                    second_half = valstr[half:]
                    if first_half == second_half:
                       self.p1_solution += value 
            
            
        return True

    def p2(self):
        self.p2_solution = 0
        for r in self.input_list:
            this_range = r.split('-')
            start, end = int(this_range[0]),int(this_range[1])
            for value in range(start,end+1):
                valset = set()
                valstr = str(value)
                vallen = len(valstr)
                halflen = vallen//2
                if vallen > 1:
                    for char in valstr:
                        valset.add(char)
                    if len(valset) == 1:
                        self.p2_solution += value 
                        print(value)
                        continue
                    
                    for i in range(1,halflen+1):
                        chunk = valstr[0:i]
                        chunk_count = valstr.count(chunk)
                        if chunk_count*i == vallen:
                            self.p2_solution += value 
                            print(value)
                            continue
                   
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
            quit()
        print(f"Elapsed time {elapsed_time(start_time)}")
        if PUZZLE_INPUT:
            print("Processing Input...\n")
            start_time = time()
            puzzle.p2()
            print(f'SOLUTION: {puzzle.p2_solution}')
            print(f"Elapsed time {elapsed_time(start_time)}")
    
if __name__ == "__main__":
    main()