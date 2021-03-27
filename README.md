# docbotChatbot and recommendation systems

https://github.com/Terminalpha/docbot


We chose to use discord to develop our chatbot. Indeed, we developed our chatbot using discord developers and python.
You need to change the code for you discord token in the main (or create a info.py with the code token inside)
 
 
 After creating the bot, we linked it to a server to be able to test it with general and easy function like ping/pong (we write !ping and the bot answers pong). 
 
Our chatbot serves to list the different opening in chess that the caller wants and then the user can view the opening he wants. For that, we use a file ,we needed to modify to make it easier to use, that has all the start that are well known of the game in it and call it in the script and then depending on the input the bot write on the chat of the server the different opening we asked.
 
 
The user can also ask the bot to show opening starting with e4 d5 for examples.
 
 


List of commands:
!select <chessboard_square>  <word>
Shows the list of names of the openings containing the <word> with the <chessboard_square> (for exemple:  !select e4 defence)
!view <name_opening>
Shows the opening with the name <name_opening>
!add <chessboard_square> or <word>
Adds to the global variable a chessboard square (for example: look picture above)

!restart
Clear the global variable
!look
Shows the best openings that have the chessboard square or the word that are in the global variable (for example : look picture above)
!look_full <chessboard_square>
Shows all the openings and their moves starting by <chessboard_square> (for examples: !look_full e4 d5)
!ask <question>
Work on view + name of a opening and show the moves 
Work on select + move + name to show all the opening with this starting move and having the name given inside the opening name(multi possibility because in chess there is variations of opening)
