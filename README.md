# DroidWars
**This is a public repository to play with classes
Feel free to fork and make your own objects and try things by yourself :)**

I´m creating a game that randomly generates a bunch of Droids, shows the status and make them fight so that one or more players can bet for any of them.
The final purpose is to win credits by choosing the right droids based on the analitics of the Droids status

- Theres a main class Droid that holds the basic status
- Three more inherited classes, support droids give bonuses to the status of the holder, extension droids extend action in battle if especific events happens
- Base droids are the most basic droid that can battle
- Fight Droids Inherit from Base Droids the have an extra attr called mele (weapon damage)
- Super Droids inherit from fight droids, they can use  the support droids 
- Humandroids are the last class, they inherit from Super Droids and they can usea the extension droids

The game is not complete.
Things to implement:
- Max levels in droids status
- Random droid generators
- Random competition generator
- Beting system

**Thank you for reading**
