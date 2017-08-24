# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default available_screens = ["notify1", "notify2", "notify3"]
default delay_done = True

# The game starts here.

label start:

    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    $allocate_screen("Ohai")
    # These display lines of dialogue

    "Hello, world."
    $allocate_screen("This")
    e "You've created a new Ren'Py game."
    $allocate_screen("Is")
    e "Once you add a story, pictures, and music, you can release it to the world!"

    $allocate_screen("An")
    "Insert more stuff here."
    
    $allocate_screen("Example")
    "The end."

    # This ends the game.

    return
