#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-22 10:38
# @Author  : ZD Liu




def describe_automaton(transitions):
    '''
    The output is produced with the print() function.
    '''
    for e in transitions.keys():
        print('When in state "'+e[0]+'" and processing "'+str(e[1])+'", automaton\'s state becomes "'+transitions[e]+'".')

    pass
    # REPLACE pass ABOVE WITH YOUR CODE
# transitions_2 = {('state_1', 0): 'state_2', ('state_1', 1): 'state_1', ('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
# describe_automaton(transitions_2)


def transitions_as_dict(transitions_as_list):
    '''
    transitions_as_list is a list of strings of the form 'state_1,symbol:state_2'
    where 'state_1' and 'state_2' are words and 'symbol' is one of the 10 digits.
    We assume that there is at most one 'state_2' for given 'state_1' and 'symbol'.
    '''
    transitions = {}
    for e in transitions_as_list:
        spt1 = e.split(':')
        spt2 = spt1[0].split(',')
        tra_key = (spt2[0],int(spt2[1]))
        transitions[tra_key] = spt1[1]
    # INSERT YOUR CODE HERE
    return transitions
# a = transitions_as_dict(['state_1,0:state_2', 'state_1,1:state_1','state_2,0:state_1', 'state_2,1:state_2'])
# print(a)
def accepts(transitions, word, initial_state, accept_state):
    '''
    Starting in 'initial_state', if the automaton can process with 'transitions'
    all symbols in 'word' and eventually reach 'accept_state', then the function
    returns True; otherwise it returns False.
    '''
    # word_list = list(word)
    get_state = False
    current_state = initial_state
    for w in word:
        try:
            tra_key = (current_state,int(w))
            if tra_key in transitions.keys():
                get_state = transitions[tra_key]
                current_state = get_state
            else:
                return False
        except:
            return False
    if get_state == accept_state:
        return True
    else:
        return False
    # pass
    # REPLACE pass ABOVE WITH YOUR CODE
    # ================second method===================
    # current_state = initial_state
    # for w in word:
    #     try:
    #         tra_key = (current_state,int(w))
    #         get_state = transitions[tra_key]
    #         current_state = get_state
    #     except:
    #         print('youwu')
    #         return False
    # if get_state == accept_state:
    #     print(True)
    #     return True
    # else:
    #     print (False)
    #     return False
    # pass

#
transitions_1 = {('q0', 0): 'q1', ('q1', 1): 'q0'}
# accepts(transitions_1, '00', 'q0', 'q1')
# accepts(transitions_1, '2', 'q0', 'q0')
# accepts(transitions_1, '0101010', 'q0', 'q0')
# accepts(transitions_1, '01010101', 'q0', 'q0')
# a = not accepts(transitions_1, '01', 'q0', 'q1') and accepts(transitions_1, '010', 'q0', 'q1')
# print('=====')
# print(a)
# transitions_2 = {('state_1', 0): 'state_2', ('state_1', 1): 'state_1', ('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
# accepts(transitions_2, '011', 'state_1', 'state_1')
# accepts(transitions_2, '001110000', 'state_1', 'state_1')
# accepts(transitions_2, '1011100101', 'state_1', 'state_1')
# accepts(transitions_2, '10111000101', 'state_1', 'state_1')

if __name__ == '__main__':
    accepts(transitions_1, '0101010', 'q0', 'q0')
    # import doctest
    #
    # doctest.testmod()