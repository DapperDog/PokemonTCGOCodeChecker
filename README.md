# PokemonTCGOCodeChecker
This is just a simple python script, that requires a few manual steps to check a list of pokemon tcgo codes

# Steps
1) go to https://www.pokemon.com/ and login
2) go to https://www.pokemon.com/us/pokemon-trainer-club/enter-codes and click the 'i'm not a robot' button
3) Press f12
4) Select the Application tab
5) Select the Cookies tab on the left hand side under 'Storage'
6) Select https://www.pokemon.com
7) find the cookie called 'main_session_id'
8) copy the value of 'main_session_id' into settings.ini besides the session_id field.
9) copy your list of codes into codes.txt, one code per line.
10) Run pokemonCodeChecker.py
11) You should now see it populate a timestamped file with the codes, for example CheckedCodes-20171009-232908.txt
