Overview
=============

Our objective here is to create a maze generation framework, a perfect maze: the simplest type of maze for a computer to generate and solve. A perfect maze is defined as a maze which has one and only one path from any point in the maze to any other point. This means that the maze has no inaccessible sections, no circular paths, no open areas.

![alt tag](http://mazeworks.com/mazegen/mazetut/tut1.gif)    -   ![alt tag](http://mazeworks.com/mazegen/mazetut/tut2.gif)

Images from: http://mazeworks.com

Framework
=============
We define a framework for most-common operations when creating mazes, allowing you to improve or add functionality to support other types of mazes. Actual implementations are separated from the contracts (Abstract Bases), thus allowing you to create your own implementations of Mazes, Tiles and Generators and use them interchangeably as component drop-in replacements.

Implementations provided
=============
Implementations of Maze, Tile, and Solver are provided. They are prefixed by Chill*
Take a look at the example file, where you can see them in action and see a real maze get generated!


Tests
=============
Tests are not coupled to implementations, so you can re-use them! they only test defined behavior as declared in abstract classes, so you dont have to worry about those. Just roll-in your implementations and hook them in the tests bootstrap file!
