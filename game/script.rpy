# Character
define me = Character(_("Helen"), color="#FFC485", what_prefix='"', what_suffix ='"')
define alice = Character(_("Alice"), color="#FF7A65", what_prefix='"', what_suffix ='"')
define alan = Character(_("Alan"), color="#87B5C0", what_prefix='"', what_suffix ='"')

# File Linking

# Scene BG

image sun_setting = "./images/bg/sun setting.png"
image school_classroom = "./images/bg/school classroom.png"
image my_home_day = "./images/bg/my home day.png"
image my_home_night = "./images/bg/my home night.png"
image my_home_lightoff = "./images/bg/my home light_off.png"

# Character Sprite
image alice normal = "./images/alice/alice normal.png"
image alice smile = "./images/alice/alice smile.png"
image alice delighted = "./images/alice/alice delighted.png"
image alice sleepy = "./images/alice/alice sleepy.png"
image alice angry = "./images/alice/alice angry.png"
image alice annoyed = "./images/alice/alice annoyed.png"
image alice laugh = "./images/alice/alice laugh.png"
image alice sad = "./images/alice/alice sad.png"
image alice shocked = "./images/alice/alice shocked.png"
image alice smug = "./images/alice/alice smug.png"

image alan normal = "./images/alan/alan normal.png"
image alan smile = "./images/alan/alan smile.png"
image alan angry = "./images/alan/alan angry.png"
image alan laugh = "./images/alan/alan laugh.png"
image alan sad = "./images/alan/alan sad.png"
image alan smirk = "./images/alan/alan smirk.png"
image alan surprised = "./images/alan/alan surprised.png"

# Phone Screen
# Animation AppJoin
image appJoin_1 = "./images/phone/appJoin/a1.png"
image appJoin_2 = "./images/phone/appJoin/a2.png"
image appJoin_3 = "./images/phone/appJoin/a3.png"
image appJoin_4 = "./images/phone/appJoin/a4.png"
image appJoin_5 = "./images/phone/appJoin/a5.png"
image appJoin_6 = "./images/phone/appJoin/a6.png"
image appJoin_7 = "./images/phone/appJoin/a7.png"
image appJoin_8 = "./images/phone/appJoin/a8.png"
image appJoin_9 = "./images/phone/appJoin/a9.png"
image appJoin_10 = "./images/phone/appJoin/a10.png"
image appJoin_11 = "./images/phone/appJoin/a11.png"
image appJoin_12 = "./images/phone/appJoin/a12.png"
image appJoin_13 = "./images/phone/appJoin/a13.png"
image appJoin_14 = "./images/phone/appJoin/a14.png"
image appJoin_15 = "./images/phone/appJoin/a15.png"
image appJoin_16 = "./images/phone/appJoin/a16.png"

# BGM

define audio.bgm_happy = "./audio/bgm/AnaCaptainslogue - Noir Et Blanc Vie.mp3"

# SFX

define audio.my_phone_ring = "./audio/sfx/Wood Plank Flicks.mp3"

# Game Settings

# All
$ gameinfo.me.point = 100

# Game1
$ game1.me.position.floor = 0
$ game1.me.position.room = 0
$ game1.me.position.place = 0

$ game1.it.position.floor = 0
$ game1.it.position.room = 0
$ game1.it.position.place = 0

#Story

label start:

    scene sun_setting with dissolve

    play music bgm_happy

    "Sun is setting and clouds turn to be yellow-orange now. It's 5:15pm now. Most of people have already left school now."

    "Alice and Alan is chatting now, You are going to join the chat."

    scene school_classroom with dissolve

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

    alice "Alan, it\'s 5:29pm. Your mum will be angry if you still not back home."

    show alan surprised

    alan "Oh, I almost forget. I need to leave now. See you tomorrow."

    show alan normal

    me "See you tomorrow."

    hide alan smile
    with moveoutleft

    show alice smile at center
    with move

    "Alan left the classroom quickly."

    me "Oh. Alice, can you send the download link?"

    alice "Of course, Let me send it to you."

    play sound my_phone_ring

    pause 0.5

    me "Thanks, Alice. See you tomorrow."

    alice "Bye, Helen."

    hide alice smile
    with moveoutleft

    "You leave the school and go to eat dinner fast."

    scene my_home_night with dissolve

    "When you come back home, It's 8:30pm now."

    me "Ahhhaa... Luckily, today haven't give any homework."

    play sound my_phone_ring

    me "Oh. I almost forget."

    "You open your phone to install the Hide 'n Seek App"

    show phone_appJoin at right
    with moveinbottom

    window hide
    with Dissolve(0.001, alpha=False)

    pause 14

    window show
    with Dissolve(0.001, alpha=True)

    me "It's weird. Normally, app should not act like this."

    me "Anyways, it's seem no problem. I think it's okay."

    me "Ahhhaa... I should sleep now."
    hide phone_appJoin at right
    with moveoutbottom

    scene my_home_lightoff with Dissolve(0.01, alpha=True)

    "You turn off the light and go to sleep now."

    play sound alarm_beep

    me "Ahhhhaaa..."

    stop sound

    "You look at the clock. It's 10:00am."

    play sound my_phone_ring

    "You open your phone to see the message."

    hide phone_sms1 at right
    with moveoutbottom

    return
