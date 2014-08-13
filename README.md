TTTGame
=======

##Tic-Tac-Toe console game
## 
This is my implementation of the well-know game. You can specify the
size of the grid and choose to play "reverse" Tic-Tac-Toe in which you
lose if you get three-in-a-row.

To implement the game I used TTTBoard class skeleton (only class methods
and their description was provided, I had to write all the logic) from
[Principle of
Computing](https://www.coursera.org/course/principlescomputing) Coursera
course.

The interesting bit was to implement the Machine Player, which was the
homework for the above mentioned course.


### Machine Player Strategy
### 
The machine player will use a Monte Carlo simulation to choose the next
move from a given Tic-Tac-Toe position.

An outline of the simulation:
1.Start with the current board.
2.Repeat for the desired number of trials:
  1.Play an entire game by just randomly choosing a move for each player.
  2.Score the resulting board.
  3.Add the scores to a running total across all trials.
3.To select a move, randomly choose one of the empty squares on the board that has the maximum score.

####2b in more detail.
####
Scores are kept for each square on the board. The way you assign a score
to a square depends on who won the game. If the game was a tie, then all
squares should receive a score of 0, since that game will not help you
determine a winning strategy. If you won the game, each square that
matches your player should get a positive score (corresponding MCMATCH
in the template) and each square that matches the other player should
get a negative score (corresponding to -MCOTHER in the template).
Conversely, if you lost the game, each square that matches your player
should get a negative score (-MCMATCH) and and each square that matches
the other player should get a positive score (MCOTHER). All empty
squares should get a score of 0.


### Monte Carlo Simulation
### 
In Monte Carlo methods, you perform a bunch of random trials in order to
figure out the expectation that some event, or multiple events, will
actually occur.

*Why would you do that?* Well, usually you do this in situations
where it is difficult or impossible to directly compute the answer, or
perhaps directly computing the answer would take far too long.

*Why is this called the Monte Carlo methods?* Well, it's, because of the
similarity to going to a casino and basically playing and recording the
result of a bunch of, of gambling games, and in that situation you're
basically randomly sampling,the probabilities of winning and losing
those games. And perhaps such casinos appear in Monte Carlo.

*In the real world what kind of of situations do we use this in?*
Generally Monte Carlo methods are used for you know, sort of physical or
mathematical problems and the the major classes of problems are
optimisation problems, figuring out probability, distributions and
numerical integration.
