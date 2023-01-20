define system = Character('gamesystem', color="#CACACA")
#define Gvidi_Fajron = Character('Gvidi Fajron', color="#E03B8B")
define donny = Character('Donny', color="#b71c1c")



#Program starts here
label start:
    stop music
    system "This game's volume is VERY loud, It is recommended that you adjust it before proceeding."


label Beginning:
    "It is decided"
    "What is done is done."
    "There is no way out."
    "In death you will pay dearly."
    "For you shall know hell before the end."
    "but the extent to which this world reshapes you,"
    "ravages you,"
    "and births you anew."
    "shall be of your accord. "
    "Well then, let us begin."
    "Welcome"
    "To Bradford..."
    show donny normal
    play sound "audio/sfx vineboom.ogg"
    donny "Are you ready to face Brrat'ford?"

menu:
    "Bring it on fuccin ell lad for Englurlend!.":
        jump ResponseToDonny_Good

    "...":
        jump lesson1

label response_to_prologue_good:
    "The game is over for now"
    jump ending1
    return

#lessons
label lesson1:
    hide donny
    "Lesson learned, NEVER be indecisive with a bradford donny."
    jump ending1

#endings
label ending1:
    play music "audio/bgm mary.ogg"
    scene bg creditsneutral
    with fade
    system "Thanks for playing"
    
    

    return
