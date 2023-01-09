define system = Character('SYSTEM.ALERT', color="#CACACA")
define Gvidi_Fajron = Character('Gvidi Fajron', color="#E03B8B")
define donny = Character('Donny', color="#b71c1c")


#lessons
label lesson1:
    hide donny
    "Lesson learned, NEVER be indecisive with a bradford donny."
    jump ending1

#endings
label ending1:
    play music "audio/bgm mary.mp3"
    scene bg creditsneutral
    with fade
    system "Thanks for playing"
    system "kierancrossland.xyz"
    "Adiaŭ mondo, Saluton mondo."

    return



#START_OF_GAME
label start:
    stop music
    system "This games volume is potentially VERY loud, it's recommended you change it beforehand."
    system "Also be warned there maybe times during this game where \"rm -rf /\" is called, In that case. GG."

label prologue:
    "It is decided"
    "For what's done is done"
    "For that which isn't be cast adrift."
    "Well then, let us begin."
    "Welcome"
    "To Bradford..."
    show donny normal
    play sound "audio/sfx vineboom.ogg"
    donny "Are you ready to face Brrat'ford?"

menu:
    "Bring it on fuccin ell lad.":
        jump response_to_prologue_good

    "...":
        jump lesson1

label response_to_prologue_good:
    "The game is over for now"
    jump ending1
    return
