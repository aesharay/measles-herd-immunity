# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:35:54 2020

@author: aesha
"""
###########################################################
    #Computer Project #5
    #   open_file function
    #   get_us_value function
    #   get_min_value_and_state function
    #   get_max_value_and_state function
    #   display_herd_immunity function
    #   write_herd_immunity function
    #   printing all data through main function
###########################################################


fp = open("MMR.txt")

def open_file():
    '''Opening file pointer'''

    try:
        fp = input("Input a file name: ")
        in_file = open(fp, "r")
        return in_file    
    except FileNotFoundError:
        print("Error: file not found. Please try again.")
        open_file()
        
        
def get_us_value(fp):
    '''Printing the percentage of United States'''
    fp.seek(0)
    fp.readline()
    fp.readline()
    usperc = 0
    for line in fp:
        if line[:25].strip() == 'United States':
            usperc = float(line[25:].strip())
    return usperc
    
def get_min_value_and_state(fp):
    '''Finding the minimum percentage'''
    fp.seek(0)
    fp.readline()
    fp.readline()
    min_val = 101
    minstate = ''
    for line in fp:
        state = line[:25].strip()
        percent = line[25:].strip()
        
        try:
            percent = float(percent)
            if float(percent) < min_val:
                min_mmr = percent
                minstate = state
                min_val = percent
        except:
            pass
    return (minstate, min_mmr)
        

def get_max_value_and_state(fp):
    '''Finding the maximum percentage'''
    fp.seek(0)
    fp.readline()
    fp.readline()
    max_val = 0
    maxstate = ''
    for line in fp:
        state = line[:25].strip()
        percent = line[25:].strip()
        try:
            percent = float(percent)
            if float(percent) > max_val:
                max_mmr = percent
                maxstate = state
                max_val = percent
        except:
            pass
    return (maxstate, max_mmr)
        
def display_herd_immunity(fp):
    '''Displaying states with lower than 90%'''
    fp.seek(0)
    fp.readline()
    fp.readline()
    print("\nStates with insufficient Measles herd immunity.")
    print("{:<25s}{:>5s}".format("State","Percent"))
    for line in fp:
        try:
            state = line[:25].strip()
            percent = float(line[25:].strip())
            if percent < 90:
                print("{:<25s}{:>5.1f}%".format(state, percent))
        except ValueError:
            pass

def write_herd_immunity(fp):
    '''Writing the states wuth less than 90% into file'''
    fp.seek(0)
    fp.readline()
    fp.readline()
    herd = open("herd.txt", "w")
    fp.seek(0)
    print("\nStates with insufficient Measles herd immunity.", file = herd)
    print("{:<25s}{:>5s}".format("State","Percent"), file = herd)
    for line in fp:
        state = line[:25].strip()
        percent = line[25:].strip()
        try:
            percent = float(percent)
            if percent < 90:
                print("{:<25s}{:>5.1f}%".format(state, percent), file = herd)
        except ValueError:
            pass
    herd.close()


def main():   
    '''Calling all functions'''
    fp = open_file()
    title = fp.readline()
    print("\n"+ title)
    print("Overall US MMR coverage: {}%".format(get_us_value(fp)))
    minval,minstate = get_min_value_and_state(fp)
    print("State with minimal MMR coverage: {} {}%".format(minval,minstate))
    maxval, maxstate = get_max_value_and_state(fp)
    print("State with maximum MMR coverage: {} {}%".format(maxval,maxstate))
    display_herd_immunity(fp)
    write_herd_immunity(fp)
    
if __name__ == "__main__":
    main()    