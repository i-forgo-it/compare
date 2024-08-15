# summary
It compares the same file everytime it is scanned and gives only the output when there are changes, you can use the -result or -all flag to only output the changes or the whole file and you need to precise the file you want to use with the -f flag.

# Example
Let's say I have a blank file called test.txt and every minute a new line is added and I only want to output the changes.
I would first scan it  ` ` `python3 compare.py -f test.txt -result` ` `
It would give me a blank output:
![image](https://github.com/user-attachments/assets/ae1e1313-802e-4c39-a6aa-e37916640b7b)
Then if i do it again after something was added to the file ` ` `python3 compare.py -f test.txt -result` ` `
![image](https://github.com/user-attachments/assets/0a0bd96f-88fa-4b2d-8eef-880049838f37)
If something new is added and i want to ouput the whole file and not just the changes i can use the -all flag.
