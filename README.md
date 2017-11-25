# PokemonTCGOCodeChecker
This is just a simple python script, that requires a few manual steps to check a list of pokemon tcgo codes

All it does it makes requests to the 'verify_code' api directly, however you need to login and pull a session id for security reasons, the code itself is <50 lines and does nothing with the codes besides tell you if they are valid, and what they redeem.

As a note it seems they limit requests to around 500 per 24h period, it wasn't really an issue once you get through the bulk of your codes.

# Requirements
1) A Pokemon Trainer Club account ( I don't think you can get banned for doing this, but I run it on alts to be safe) 
2) Python 2.7 or greater, you can check if you have python installed by opening a console and typing 'python --version' if not installed you can download it at https://www.python.org/downloads/

# Installing
1) Go to the project root https://github.com/DapperDog/PokemonTCGOCodeChecker (you are probably already there)
2) Select the Clone or Download button
3) Download Zip
4) Unzip in location of your choise

# Steps (Using chrome)
1) go to https://www.pokemon.com/ and login
2) go to https://www.pokemon.com/us/pokemon-trainer-club/enter-codes and click the 'i'm not a robot' button
3) submit any text in the 'enter code' field, this just finishes the verification, and flags your session id as not being a robot
4) Press f12
5) Select the Application tab
6) Select the Cookies tab on the left hand side under 'Storage'
7) Select https://www.pokemon.com
8) find the cookie called 'main_session_id'
9) copy the value of 'main_session_id' into the session_id field inside settings.ini
10) copy your list of codes into codes.txt, one code per line, I would heavily suggest using a phone app like Pokecollector to scan all your codes, then you can just copy the code list from an email into the text file.
11) Run pokemonCodeChecker.py {python -i pokemonCodeChecker.py}
12) You should now see it populate a timestamped file with the codes, for example CheckedCodes-20171009-232908.txt

# Common Errors

{"detail":"Authentication credentials were not provided."}

This means that you didnt put a valid session_key in the settings.ini

{"detail":"Google validation not complete"}

This means that you need to click the 'im not a robot' and submit any text in the verify code field to activate your session_id
