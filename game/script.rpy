label start:
    "Story"
    jump name
    return

label name:
    
    unknown "Hello?"

    C "What's your name?"

    $ mc.name = renpy.input("Input your Name:").strip()

    if mc.name == "":
        $ mc.name = "Principle"
    
    C "Welcome, [mc.name]!"

    C "your journey begins here"
    jump Your_Office
    return