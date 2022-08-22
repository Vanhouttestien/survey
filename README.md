# Nummory 

Nummory is a memmory game, in wich you have to try to remember as much numbers as possible. It is developed with the intend to help people train their memory and and improve their brain. 
<img src="" alt="Picture of webpage across different devices" width="600px">

##  Table of content
- [How to play](#how-to-play)
- [Technologies used](#technologies-used)
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## How to play
### Frameworks, Libraries & Programs Used
- [GitPod](https://gitpod.io/): Gitpod was used as development environment 
- [GitHub](https://github.com/): Github was used to deploy the site and store it  
- random: for generating a random number
- time: used for waiting after user gives nickname and typing effect 
- os: celaring the screen 
- getkey: used for the user to use a keypress to choose, or go to the next step
- gspread: used for the high score list
- google.oauth2.service_account: for high score list 
- tabulate: to create the high score
- colorama: used to add color to the text
- pyfiglet: used for the ASCII Art Text Banner
- sys: used for the typewriting effect
- Threading: used for the timer during the game that is cancelable. 

## Features


## Testing 



### Fixed bugs 
- The start menu and restart option was not limited. When notting or another key was klicked the program went to the following line.  

### Unfixed bugs
- when your time is up you still have to click to be able to give your answer. I wasn't able to get the key press canceled or mocked. So I added a line that you have to press a key to continue. 

## Deployment 
This site was deployed with the code institute mock terminal for Heroku. 

To deploy a page you first go to Heroku dashboard and click op new, create new app. 
Than set the buildpacks to python and jsnode. 
Lasly in the deploy tab connect the github repositiory and click on enable automatic deploy. 

The link can be found here: https://nummory.herokuapp.com/

## Credits
### code
- code for ASCII Art Text Banner: https://www.devdungeon.com/content/create-ascii-art-text-banners-python
- code for the typing effect in the instructions: https://www.101computing.net/python-typing-text-effect/
- code for converting list of string to integers: https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
- code for building a table: https://www.statology.org/create-table-in-python/
### support 
- Mentor Martina Terlevic for feedback
- Code institute tutor support, tutor Ger. For his time and effort to help try to resolve a bug
- Code institute template and mock terminal
