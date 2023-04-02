# CS515_project1_Adventure
 Yetong Chen ychen12@stevens.edu

 A text-based video game: players use text commands to explore a textual world.

## Github repo
https://github.com/yetongchen/CS515_project1_Adventure

## time
I spent about 7 hours on the project.

## test 
I tested my code through running the testing commands saved in the test.py file.

## bugs or issues
When setting the win condition, I used the index to refer to a specific room. However, if the map is changed, this win condition might still trigger, causing an error.

## resolved issue
To prevent triggering the winning or losing condition on other maps, I referred to the special room by its specific name throughout the text.

## 3 extensions
### A `help` verb
A `help` verb tells players what the valid verbs are. We write `...` after verbs that expect a target of some kind:
```
> A white room

You are in a simple room with white walls.

Items: shield

Exits: north east

What would you like to do? help
You can run the following commands:
  go...
  look
  get...
  drop...
  inventory
  help
  quit
What would you like to do?
```

### A `drop` verb
The `drop` verb is the opposite of get: take something from your inventory and put it down in the room. Just as get only lets you get items that are in the room, drop should only let you drop items that you already have.
```
> A white room

You are in a simple room with white walls.

Items: shield

Exits: north east

What would you like to do? get shield
You pick up the shield.
What would you like to do? inventory
Inventory:
  shield
What would you like to do? look
> A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? go north
You go north.

> A blue room

This room is simple, too, but with blue walls.

Exits: east south

What would you like to do? drop sword
You're not carrying the sword.
What would you like to do? drop shield
You drop the shield.
What would you like to do? look
> A blue room

This room is simple, too, but with blue walls.

Items: shield

Exits: east south

What would you like to do? inventory
You're not carring anything.
What would you like to do?
```
### Winning and losing conditions
There is a sword and a shield in the rooms as well as a 'boss room' in the map. If you enter the boss room without both the sword and shield, you lose, and the game continues. You can try again to get the weapons. If you enter it with both, you win, and the game ends. 
```
> A white room

You are in a simple room with white walls.

Items: shield

Exits: north east

What would you like to do? go east
You go east.

> A red room

This room is fancy. It's red!

Items: rose

Exits: north west east

What would you like to do? go east
You go east.

> A boss room

The room is boss, and there seems to be something very big sleeping deep down.

Exits: west

You encountered a dragon but were defeated due to a lack of weapons. You lose. Try again!
What would you like to do? go west
You go west.

> A red room

This room is fancy. It's red!

Items: rose

Exits: north west east

What would you like to do? go west
You go west.

> A white room

You are in a simple room with white walls.

Items: shield

Exits: north east

What would you like to do? get shield
You pick up the shield.
What would you like to do? go north
You go north.

> A blue room

This room is simple, too, but with blue walls.

Exits: east south

What would you like to do? go east
You go east.

> A green room

You are in a simple room, with bright green walls.

Items: sword

Exits: west south

What would you like to do? get sword
You pick up the sword.
What would you like to do? go south
You go south.

> A red room

This room is fancy. It's red!

Items: rose

Exits: north west east

What would you like to do? go east
You go east.

> A boss room

The room is boss, and there seems to be something very big sleeping deep down.

Exits: west

You encountered a dragon and defeated it with your sword and shield! You won! Congratulations!🎇
```
