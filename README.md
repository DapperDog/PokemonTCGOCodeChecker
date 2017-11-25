# PokemonTCGOCodeChecker
This is just a simple python script, that requires a few manual steps to check a list of pokemon tcgo codes

All it does it makes requests to the 'verify_code' api directly, however you need to login and pull a session id for security reasons, the code itself is <50 lines and does nothing with the codes besides tell you if they are valid, and what they redeem.

# Requirements
1) A Pokemon Trainer Club account ( I don't think you can get banned for doing this, but I run it on alts to be safe) 
2) Python 2.7 or greater

# Notes
It appears you can only make ~500 requests per account per 24 hours, so just keep that in mind, I have many trainer club accounts I use, but I am rarely checking that many codes after I did the first big batch.

# Steps (Using chrome)
1) go to https://www.pokemon.com/ and login
2) go to https://www.pokemon.com/us/pokemon-trainer-club/enter-codes and click the 'i'm not a robot' button
3) Press f12
4) Select the Application tab
5) Select the Cookies tab on the left hand side under 'Storage'
6) Select https://www.pokemon.com
7) find the cookie called 'main_session_id'
8) copy the value of 'main_session_id' into the session_id field inside settings.ini
9) copy your list of codes into codes.txt, one code per line, I would heavily suggest using a phone app like Pokecollector to scan all your codes, then you can just copy the code list from an email into the text file.
10) Run pokemonCodeChecker.py {python -i pokemonCodeChecker.py}
11) You should now see it populate a timestamped file with the codes, for example CheckedCodes-20171009-232908.txt
