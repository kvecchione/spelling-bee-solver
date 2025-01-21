# Spelling Bee Solver

Solver for NYT Spelling Bee game. Obviously I like not using this when I play (cheating), but it was fun to figure out the method to solve it in code. It uses the scrabble input word list from here: https://www.freescrabbledictionary.com/twl06/ which may not be an exact match to the SB word list, but close enough.

It will download the most recent word list or use the cached file if it has already been downloaded. 

The program uses all built-in functionality, no dependencies.

## Usage Example

```
# python3 spelling-bee-solver.py Abcdefg
CABBAGED [8]
DEBAGGED [8]
ACCEDED [7]
BAGGAGE [7]
CABBAGE [7]
DEFACED [7]
EFFACED [7]
FEEDBAG [7]
ACCEDE [6]
...
```
