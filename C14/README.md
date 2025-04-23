# player_detector enabled door protection

naming a program "startup.lua" means that it will be run automatically when the computer is turned on (i.e. the computer will run the program when the chunk is loaded).

## for your information
Blocks required:
```
Player detector
Computer
Redstone relay

Potentially requires:
- 4 Modems
- Network cable
```

Startup.lua reads player names from whitelist.txt.

Whitelist file is not made automatically if it doesn't exist, this must be created manually

## to make whitelist file
seperate player names by new lines, for example:

```
Liam
Jerry
Janice
```

## how to setup
1. connect redstone relay and player detector to computer
2. manually create a whitelist.txt file in the same directory as startup
