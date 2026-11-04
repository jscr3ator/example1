lantern = False
playing = True

print("lost lantern")
print("its foggy af and u gotta get home. find a lantern first")

while playing:
    print("\n1. check the forest")
    print("2. cross the bridge")
    print("3. im done lol")
    choice = input("pick 1 2 or 3: ").strip()

    if choice == "1":
        if lantern:
            print("bro u already got the lantern theres nothing else here")
        else:
            lantern = True
            print("yo theres a lantern in this tree, its yours now")
    elif choice == "2":
        if lantern:
            print("u can see the bridge now. made it home lets gooo u win")
            playing = False
        else:
            print("nah its too dark get a light first")
    elif choice == "3":
        print("aight ur staying here then. game over lol")
        playing = False
    else:
        print("bro pick 1 2 or 3")
