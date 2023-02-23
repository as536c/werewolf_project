# Werewolf Project

# Install pygame to run the app, werewolf.py main app.

Werewolf is a deception party game that can currently be played by 5-10 people. The goal is simple, werewolves try to kill the villagers, while the villagers figure out who the werewolf/ves are/is and lynch them. Neutral characters are also introduced in this game where they don't side with neither villagers nor werewolves and can win the game in their own terms.

# Rules:

1. Players get their roles at the start of the game. Werewolves (if there are more than 1) will be able to tell who are their team mates while villagers don't.
2. The game starts on a night phase where werewolves can kill and villagers can utilize their abilities (if there are any).
3. Villagers win if the wolves are eliminated.
4. Wolves win if they outnumber(or equal) to the other players.
5. Wilcard players are alone and will win on different conditions. (See role tab)


# Roles:

Every game, the players are divided into 3 parties; Villagers, Wolves, Wildcards. Which has their own unique abilities. Letters that are enclosed with a parentheses are the output when the player is checked by the seer.
(b) = bad, villager
(g) = good, wolf
(u) = unknown, might be a wildcard, or villager/wolf with a strong ability to add complexity to the game

- Wolves
Any wolf can kill another villager during night phase. Also has assassinate ability(not yet implemented) that can be used ONCE; if correctly guessed a role, the target dies; but wolf dies if the guess is wrong.
      (b) Wolf: kills at night 
      (u) Alpha: unknown to seer; c
      (b) Wolf trickster: can reverse a role of a player each night, unknown will remain unknown: trick

- Villagers
People of the village, their goal is to sniff out the wolves
      (g) Seer: can check players if good or bad
      (g) Super seer: can see roles
      (g) Silencer: can silence a chat/voice
      (u) Medium: can speak to the dead
      (g) Bodyguard: can protect/has 2 lives
      (g) Sheriff: can kill player during daytime
      (g) Doctor: can revive a player once
      (g) Villager: no power
      (u) Jailer: can jail player and restrict user powers
      (g) Priest: can splash holy water during day or night, if wolf, wolf will die. if not, priest will die.

- Wildcards
      (u) Fool: only wins if got voted out
      (u) Hunter: wins when target gets voted out
      (u) Arsonist: can put gasoline/or ignite. wins as the last man standing
      (u) Serial killer: cannot be killed by wolves, can kill every night. can only be killed by sheriff or lynch. wins as the last man standing


--------------------------------------------------------------------------------------------------------------------------

# Dev notes:
- Improve visuals (player cards, action PNG files)
- Focus polishing 5 player first before proceeding to add 6-10 players.

To test game:
1. run *server.py*, this will append random roles in *wroles.py* file, this is to make consistent roles across all players.
    >> python3 server.py
2. run *werewolf.py* on terminal. This can run 2 instances for now, for testing purposes but should run 5 clients.
    >> python3 werewolf.py
