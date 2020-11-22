# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 11:45:26 2020

@author: Aishwarya Jayashankar
"""

import fileinput

graph = [];
deadlock_detected = False;

class node:
    def __init__(self, proc_num):
        global number_of_processes;
        
        self.proc_num = proc_num;
        self.dependency_set = [];
        self.num = [0]*(number_of_processes+1);
        self.wait = [-1]*(number_of_processes+1);
        self.engaging_queries = [-1]*(number_of_processes+1);

def initialize_graph():
    global number_of_processes;

    graph.append(node(-1));
    for i in range (1, number_of_processes+1):
        graph.append(node(i));    
    
def read_input():
    global graph;
    global number_of_processes;
    global initiator_process;

    flag = input("Use demo input? (y/n) ");

    #Demo input
    if flag[0] == 'y':
        file = fileinput.input(files = "demo_input.txt");
        counter = 1;
        flag = True;
        
        for line in file:
          if counter==1:
              number_of_processes = int(line);
              initialize_graph();
              counter+=1;
          elif flag:
              if line[0] == 'e':
                  flag = False;
                  continue;
              a = int(line.split()[0]);
              b = int(line.split()[1]);
              graph[a].dependency_set.append(b);
          else:
              initiator_process = int(line);

        return;
             
    #Custom input
    #read number of processes
    number_of_processes = int(input("Enter number of processes: "));
    initialize_graph();

    #read dependency sets
    print("Enter dependencies in the format a b where a is dependent on b: ");
    while(True):
        line = input();
        if (line[0] == 'e'):
            break;
        a = int(line.split()[0]);
        b = int(line.split()[1]);
        if (a > number_of_processes or b > number_of_processes or a<1 or b<1):
            print("Invalid input");
            continue;
        graph[a].dependency_set.append(b);

    #read initiating process
    initiator_process = int(input("Enter initiating process number: "));
        

def is_engaging_query(initiator, sender, receiver):
    global graph;
    return graph[receiver].engaging_queries[initiator] == -1;

def reply(initiator, sender, receiver):
    global graph;
    global deadlock_detected;
    print("REPLY: ", initiator, sender, receiver);
    
    if (graph[receiver].wait[initiator]):
        graph[receiver].num[initiator] -= 1;
    if (graph[receiver].num[initiator] == 0):
        if (initiator == receiver):
            deadlock_detected = True;
            print("\nDeadlock detected; no need for non-engaging queries");
        else:
            reply(initiator, receiver, graph[receiver].engaging_queries[initiator]);

def query(initiator, sender, receiver):
    global graph;
    print("QUERY: ", initiator, sender, receiver);

    if (initiator==receiver):
        reply(initiator, receiver, sender);
        return;

    if (is_engaging_query(initiator, sender, receiver)):
        graph[receiver].engaging_queries[initiator] = sender;
        graph[receiver].num[initiator] += len(graph[receiver].dependency_set);
        graph[receiver].wait[initiator] = True;
        for process in graph[receiver].dependency_set:
            query(initiator, receiver, process);

    elif (graph[receiver].wait[initiator]):
        reply(initiator, receiver, sender);
        

def CMH_OR():
    global graph;
    global initiator_process;
    
    graph[initiator_process].num[initiator_process] = len(graph[initiator_process].dependency_set);
    graph[initiator_process].wait[initiator_process] = True;
    for process in graph[initiator_process].dependency_set:
        query(initiator_process, initiator_process, process);

def non_engaging_query(process_id, number_of_queries):
    global initiator_process;
    
    for i in range(0, number_of_queries):
        graph[process_id].num[initiator_process] += len(graph[process_id].dependency_set);
        graph[process_id].wait[initiator_process] = True;
        for process in graph[process_id].dependency_set:
            query(initiator_process, process_id, process);

while(True):
    read_input();
    print("\nOutput:");
    CMH_OR();
    if not deadlock_detected:
        flag = input("\nNo deadlock detected, do you want to send non-engaging queries? (y/n) ");
        if flag[0] == 'y':
            while(True):
                print("\nFollowing are process ID's which haven't received a reply yet:");
                waiting_processes = [];
                for temp_node in graph:
                    if temp_node.num[initiator_process] != 0:
                        waiting_processes.append(temp_node.proc_num);
                print(waiting_processes);
                
                line = input("\nEnter process id and number of non-engaging queries to be sent in the format a b: ");
                if len(line.split())!=2:
                    print("Incorrect input format");
                    continue;
                a = int(line.split()[0]);
                b = int(line.split()[1]);
                if (a not in waiting_processes):
                    print("\nThe entered process ID is not waiting for a reply, please choose another process");
                    continue;
                non_engaging_query(a, b);
                print("\nNo deadlock detected");
                break;
       
    if not ((input("\nTry with another input? (y/n) "))[0] == 'y'):
        break;
    
    graph.clear();
    deadlock_detected = False;








