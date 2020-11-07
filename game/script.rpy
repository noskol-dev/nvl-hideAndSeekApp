# Character
define me = Character(_("Helen"), what_prefix='"', what_suffix ='"')
define alice = Character(_("Alice"), what_prefix='"', what_suffix ='"')
define alan = Character(_("Alan"), what_prefix='"', what_suffix ='"')

# File
image alice smile = "./images/alice/alice smile.png"

image alan smile = "./images/alan/alan smile.png"

# Game Settings

label start:

    "Sun is setting and clouds turn to be yellow-orange now. It's 4:57pm now. Everyone is leaving school now."

    "Alice and Alan is chatting now, You are going to join the chat."

    show alan smile at left

    show alice smile at right

    me "Hey, guys. What are you do?"

    alice "We are talking about this app."

    me "What app?"

    alice "The Hide and Seek App."

    me "What is this app?"

    alan "It's was a ARG (Alternate Reality Game) Mobile Game.\nIt\'s like a combination of Turn-based board game and Hide \'n Seek."

    me "I\'s sound interesting."

    alan "Yes, it\'s. All of us have downloaded this app too. {w=0.5} How about we play it together?"

    alice "It\'s a good idea, Alan. Let me ask Tom and Danny. When and Where we meet?"

    me "Tomorrow is holiday. How about tomorrow afternoon?"

    alan "It\'s a good time. I think we all can play in this time."

    "Alice Looks at the clock."

    alice "Alan, it\'s 5:03pm. Your mum will be angry if you still not back home."

    alan "Oh, I almost forget. I need to leave now. See you tomorrow."

    me "See you tomorrow."

    "Alan left the classroom quickly."

    me "Oh. Alice, can you send the download link?"

    alice "Of course, Let me send it to you."

    play sound ""

    me "Thanks, Alice. See you tomorrow."

    alice "Bye, Helen."

    return
