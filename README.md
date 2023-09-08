# python-vending-machine
 Practicing python and object oriented programming by coding a vending machine that responds to user input via command line.

| Command Syntax                            | Example                  | Description                                                 |
| ------------------------------------|--------------------------|-------------------------------------------------------------| 
| balance                             | balance                  | shows the balance                                           |    
| history                             | history                  | prints list of transactions                                 |
| inventory                           | inventory                | prints available items with name and ID                     |
| add item \<str\> \<int\> \<float\>  | add item chips 2 $1.00   | add an item name qty price                                  |
| buy item \<str\> \{5\}\<int\>       | buy item chips 1 2 2 4 3 | buys an item with \# dollars, quarters, dimes, nickles, <br> pennies. It also shows change given and the remaining <br> balance with currency distribution.  For change, the machine <br> uses the largest denominator of curenncy that is available.
| help                                | help                     | display help menu with these commands                       |
| exit                                | exit                     | exit the vending machine                                    |