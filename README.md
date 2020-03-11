# Deal or No Deal

Our challenge today is to write a program that will imitate a round of [Deal or No Deal](https://en.wikipedia.org/wiki/Deal_or_No_Deal_(U.S._game_show)).

## Gameplay

This challenge is based on the classic single player game where a player is presented with 26 briefcases, each containing a monetary value between $.01 and $1,000,000. The player selects an initial case to hold on to for the duration of the round. The player will then select a batch of cases to be removed from play. The amounts in each of the removed cases are revealed, and the "banker" makes an offer to purchase the player's case, which the contents is still unknown.

The player can choose to take the banker's offer, which will be more than the lowest remaining unrevealed amount and less than the highest remaining unrevealed amount, or the player can opt to eliminate another batch of cases from the board. They will continue to remove cases until the player either accepts the offer from the banker, or there is only one remaining case in play.

If the player rejects the banker's offer on the final case, the player may opt to keep their own case, or switch it out with the remaining case. The player receives the amount in the chosen case as a prize.

The cases are removed in batches in between negotiations with the banker:

6 - 5 - 4 - 3 - 2 - 1 (until there is only one left)

The monetary amounts are as follows:

$.01 - $1 - $5 - $10 - $25 - $50 - $75 - $100 - $200 - $300 - $400 - $500 - $750 - $1,000 - $5,000 - $10,000 - $25,000 - $50,000 - $75,000 - $100,000 - $200,000 - $300,000 - $400,000 - $500,000 - $750,000 - $1,000,000

The object of the game is to end the game with the highest value possible. 

## App implementation

Implementation of this is open ended. You can decided which data structures you want to use, how to handle displaying the items, how to choose cases and banker interactions, and how to figure the offer from the banker. You can choose to make a web application or a terminal application. 

When you have something working that you are impressed by, share it with the group!

## Resources

* [Deal or No Deal](https://en.wikipedia.org/wiki/Deal_or_No_Deal_(U.S._game_show))
* [Howie Walks Through The Simple Yet Complicated Game | Deal Or No Deal: Back In Business (video)](https://www.youtube.com/watch?v=KotVp7EDzcA)
* [Deal or No Deal Banker's Formula (blog)](http://commcognition.blogspot.com/2007/06/deal-or-no-deal-bankers-formula.html)
