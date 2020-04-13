# Cards Elemental
## A card game for two players.
### Project

We are building a base engine for the game with a reference implementation in text-mode.
The idea is that anyone can built a client, like PyGame, web or such that communicates with the server. 

Whether the server will be running JSON REST, GRPC or whatever has yet to be decided.

### Rules

- Each player draws 5 cards from the deck.

A card has an element, a colours and a value.

The deck consists of cards numbered from 1 - 10 from each element and in each colours  - 120 cards.

An element can be `fire`, `water`, or `ice`.

The colours are `red`, `green`, `blue`, and `yellow`. 

### A round 
- In turn each player plays a card to see who wins.
- The winner keeps their own card in their winnings pile.
- The starting player is chosen at random (dice rolls/draw cards). Following rounds are started by the last round winner.

### Winning a round
A winner is determined by first the elements then the value (1-10)

- fire beats ice (melts it)
- ice beats water (freezes it)
- water beats fire (extinguishes it)

If the element is the same, the higher value wins.

-  if no winner is found the round is a draw, both cards are discarded and a new round is started

### Winning the game

- First to obtain cards of 3 _different_ elements or 3 cards of the _same_ colour in **one** element wins the game

