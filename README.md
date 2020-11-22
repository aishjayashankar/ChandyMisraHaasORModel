# Chandy Misra Haas Algorithm for the OR Model
**********************************************

Author: Aishwarya Jayashankar

The algorithm has been implemented using Python and its working has been tested on Python 3.7 on Windows 10 operating system.
However, it may work with higher versions of Python as well.

To setup the Python Interpreter on your machine, follow the steps in the following links:
For Windows - https://docs.python.org/3/using/windows.html
For Linux - https://docs.python.org/3/using/unix.html
For Mac OS - https://docs.python.org/3/using/mac.html

Once the Python interpreter is available the CMH_OR.py file can be executed by simply double-clicking on the file, and a command prompt opens up.

Note: If for some reason double-clicking the file does not work, please run the same by opening a command prompt window and entering the following command (in the directory of the Python file):
python3 CMH_OR.py
PS: Python should be available in path under Environment variables

-------------INPUT DESCRIPTION----------------

Two options are available for the User:
1. Use demo input (available in file demo_input.txt)
2. Custom input from User (manually entered values)

The Graph for the Demo input can be found in demo_input_example.png

On running the program initially, press 'y' and 'Enter' for Demo input, or press 'n' and 'Enter' for Custom input.

For Custom input, the values are entered in the following order and format:
-Number of processes (integer value > 1) 
For Example: 3
-Dependencies between processes in the format a b where 'a' and 'b' are integer values in the range [1,n] where n is the number of processes. After entering the required dependencies, press 'e' and 'Enter' to move to the next step
For Example: 
1 2
2 3
3 1
e
-Initiating process number (integer value in the range [1,n] where n is the number of processes)
For Example: 1

Note: After the above steps, the program will display the Queries and Replies sent and display whether a DEADLOCK was detected or not.
If a Deadlock is NOT detected, the User will be asked if she/he wants to send some non-engaging queries.

-To send non-engaging queries, press 'y' and 'Enter'

Note: The User will be able to see a list of process IDs that are still waiting for a reply

-Process ID and number of non-engaging queries to be sent in the format a b where 'a' is an integer value in the range [1,n] where n is the number of processes and 'b' is any positive integer
For Example: 1 4

Note: The program will execute and display the non-engaging Queries and their corresponding Replies sent.
After this, the User can retry the program with another set of inputs.

-Press 'y' and 'Enter' to retry with another Input, press 'n' and 'Enter' to exit.

--------------------END----------------------
