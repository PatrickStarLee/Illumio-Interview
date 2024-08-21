Instructions:
Run 'python main.py' to execute main.py.
When the program asks "Enter name of flow logs filename: ", input filename containing all flowlogs (in this demo, type in "flowlogs.txt").
When the program asks ""Enter lookup table filename: ", input filename containing a lookup table file (in this demo, type in "lookup-tbl.txt").
After inputing both files, an "output.txt" will appear with the printed results.

Assumtions:
- assume program only supports version 2
- assume program supports default log formats (I am using .txt files in this demo)
- assume the users know that the name of the files for the flow logs and lookup table and they exist
- assume there exists a file containing the information of what decimal number is associated with what protocol where each new row has information for only one protocol (this repository already includes the csv file)

Test:
- tested the progam with the given example provided in the email
- made sure to add new keys for Tags or Port/Protocol keys if they don't exist currently in a hashmap that stores the results

Analysis:
- program parses through the lookup table file and requires O(N) memory for the total number of key-value pairs for O(1) lookup time
- program parses through the protocol-numbers-1.csv file and requires O(M) memory for the total number of key-value pairs for O(1) lookup time (the key is a tuple containing the dstport and protocol)
- the main program requires O(L) time where L is the total number of rows in the log file to map each row to a tag
