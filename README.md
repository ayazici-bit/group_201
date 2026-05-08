# group_201
Conquian Program

**Purposes of Files**
* .gitignore: Common file that is used to ignore any unuseful automatically created files (such as Python cache files).
* LICENSE: Shows the legal ramifications of using this software and our code. Our code can be reused but it must stay under General Public Licensing requirements.
* README.md: Contains information on our program. This includes the purpose of all files in the repository, instructions on how to run and play our game, a bibliography, and noting which group members used which techniques.
* conquian.py: The program itself. This file is our final project submission.
* trial_conquian.py: The version of the program we had when we presented. We knew this version worked and wanted to use it for our demo before making any finishing touches that could possibly break the game.

**Running the Program**\
This program takes no command line arguments. Run it as one would any python program.

**How to use the Program**\
As far as using the program, instructions on what the user should input pop up throughout the program. For clarity, when the program asks for a meld it is looking for the user to match 3 or 4 of the same card, or a sequence of at least 3 cards in the same suit.

**Bibliography**\
Bicycle Cards. “Conquian.” Bicycle, Bicycle Cards, 2026, bicyclecards.com/how-to-play/conquian.
We used this website to learn how to play Conquian. The program is based on the rules stated on this page.

‌W3 Schools. “Python Functions.” W3 Schools, Refsnes Data, 2026, www.w3schools.com/python/python_functions.asp.. This page (among a handful of others on this site) was used as a refresher for how to handle functions within functions.

**Attribution**
| Method/Function | Author | Technique |
|-----------------|--------|-----------|
| deal_hand (player) | Aleyna Yazici | |
| draw_card | Aleyna Yazici | Composition of two custom classes |
| show_hand | Aleyna Yazici | |
| number_of_melds | Aleyna Yazici | |
| best_discard_hint | Aleyna Yazici | Set operations |
| deal_hand (cpu) | Thomas Carey | |
| cpu_turn | Thomas Carey | |
| cpu_try_discard | Thomas Carey | Key functions |
| cpu_try_draw | Thomas Carey | f-strings |
| validate_meld | Paul Gomes | |
| find_possible_melds | Paul Gomes | Comprehensions & Optional parameters |
| calculate_score | Nzinga Philbert | |
| __lt__ | Nzinga Philbert | Magic methods other than __init__ |
| suggest_best_player_meld | Nzinga Philbert ||
| check_win_condition | Nzinga Philbert | Sequence unpacking|
| player_turn | Thomas Carey | |
| cpu_turn_run | Paul Gomes | |
| play_game | Paul Gomes | |
