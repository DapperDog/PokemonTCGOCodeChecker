# DISCLAIMER
I don't know if doing this will risk your account, I haven't run into any issues but I had always used alt accounts.

So ya, use at your own risk.

I'm also assuming you at least know a little bit about python / running python scripts

And hey, if you get some good use out of this, you can show your appreciation by sending some digital / physical cards my way :P 

# PokemonTCGOCodeChecker
This is just a simple python script, that requires a few manual steps to check a list of pokemon tcgo codes

All it does it makes requests to the 'verify_code' api directly, however you need to login and pull a session id for security reasons, the code itself is <50 lines and does nothing with the codes besides tell you if they are valid, and what they redeem.

As a note it seems they limit requests to around 500 per 24h period, it wasn't really an issue once you get through the bulk of your codes.

Youtube Video showing how to run it (unlisted video for now):
https://youtu.be/1xWUNClPAAI

# Requirements
1) A Pokemon Trainer Club account ( I don't think you can get banned for doing this, but I run it on alts to be safe) 
2) Python 2.7 or greater, you can check if you have python installed by opening a console and typing 'python --version' if not installed you can download it at https://www.python.org/downloads/

Depending on your OS/instead you might need to use easy_install instead of pip.

# Installing
1) Go to the project root https://github.com/DapperDog/PokemonTCGOCodeChecker (you are probably already there)
2) Select the Clone or Download button
3) Download Zip
4) Unzip in location of your choise
5) from commandline run 'python setup.py install' this just adds the configparser and requests python modules

# Steps FOR VALIDATOR (Using chrome)
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

# Steps FOR REDEEMER (Using chrome)
1) go to https://www.pokemon.com/ and login
2) go to https://www.pokemon.com/us/pokemon-trainer-club/enter-codes and click the 'i'm not a robot' button
3) submit any text in the 'enter code' field, this just finishes the verification, and flags your session id as not being a robot
4) Press f12
5) Select the Application tab
6) Select the Cookies tab on the left hand side under 'Storage'
7) Select https://www.pokemon.com
8) find the cookie called 'main_session_id'
9) copy the value of 'main_session_id' into the session_id field inside settings.ini
10) While still in the developer tools, select 'Elements' to view the page source
11) CTRL+F and search for 'csrfmiddlewaretoken', it should look like 
"<input type="hidden" name="csrfmiddlewaretoken" value="QlPfYvo5Ys5zgMX91azidazUG8oZDBff">"
12) copy the value of csrfmiddlewaretoken into the csrf_token field inside settings.ini
13) copy your list of codes you want to redeem into redeemCodes.txt, one code per line, I would heavily suggest using a phone app like Pokecollector to scan all your codes, then you can just copy the code list from an email into the text file.
11) Run pokemonCodeRedeemer.py {python -i pokemonCodeRedeemer.py}
12) You should now see an output in the console of your redeemed codes, this currently doesn't output to a file.

# Common Errors

{"detail":"Authentication credentials were not provided."}

This means that you didnt put a valid session_key in the settings.ini

{"detail":"Google validation not complete"}

This means that you need to click the 'im not a robot' and submit any text in the verify code field to activate your session_id

# Making your codes pretty

Make a copy of the google sheet here: https://docs.google.com/spreadsheets/d/1q3N_XSQPzzZkFYajR335qmYko9wJjO1zPHTYs3cYQmE/edit?usp=sharing

1) Copy the contents of the text file the script generated
2) paste into topleftmost empty field on the Codes tab
3) select the paste icon in the top right
4) select split text into columns (by default its commas)
5) there you go, the overview page will now list counts of each code type, as well as list any duplicate codes.

Just make sure you make a copy and don't share the sheet with anyone :P you wouldnt want your codes to be public :) 
