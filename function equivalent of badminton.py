#FUNCTION TO PLAY A SET

def play_set(p1_name,p2_name,set_number):
    player1_pts = 0
    player2_pts = 0
    print(f"\n{p1_name} vs {p2_name} | Set {set_number}")
    while not ((player1_pts >= 3 or player2_pts >= 3) and abs(player1_pts - player2_pts) >= 2):
        scored_player = input("Who won the point:- ")
        if scored_player == p1_name:
            player1_pts += 1
        elif scored_player == p2_name:
            player2_pts += 1
        else:
            print("Invalid name")
            continue
        if player1_pts == 5 or player2_pts == 5:
            break
        print(f"----- SCOREBOARD (Set {set_number}) -----")
        print(f"{p1_name} : {player1_pts}")
        print(f"{p2_name} : {player2_pts}")
    if player1_pts > player2_pts:
        print(f"{p1_name} wins Set {set_number}")
        return player1_pts, player2_pts, p1_name
    else:
        print(f"{p2_name} wins Set {set_number}")
        return player1_pts, player2_pts, p2_name
    proceed = input("Do you want to continue to the next point? (y/n)")
    if proceed.lower() != 'y':
        return player1_pts, player2_pts, None

#FUNCTION TO DISPLAY SCOREBOARD

def display_scoreboard(p1_name, p2_name, set_scores, winner):
    #Header
    print(f"{'Player':<12}",end="")
    for i in range(1,4):
        print(f"\tSet {i}",end="")
    print()
    #Player 1
    print(f"{p1_name}",end="")
    for s,p1,p2 in set_scores:
        print(f"\t{p1}",end="")
    print()
    #Player 2
    print(f"{p2_name}",end="")
    for s,p1,p2 in set_scores:
        print(f"\t{p2}",end="")
    print()
    print(f"\nMatch Winner: {winner}")

#MAIN PROGRAM
while True:
    print("\t\t Available Games ")
    print("\t 1. Volleyball")
    print("\t 2. Tennis")
    print("\t 3. Badminton")
    print("\t 4. Exit")
    choice=int(input("Enter your choice:- "))
    if choice==1 or choice==2:
        print("Welcome to the game! The scoreboard will be updated soon")
    elif choice==4:
        exit()
    elif choice==3:
        print("Welcome to the game!")
        p1_name = input("Enter the name of player 1:- ")
        p2_name = input("Enter the name of player 2:- ")
        print(f"The match is between {p1_name} and {p2_name}")
        sets = 0
        set_p1 = 0
        set_p2 = 0
        set_scores = []
        while (set_p1 < 2 and set_p2 < 2) and sets < 3:
            sets += 1
            p1_pts, p2_pts, set_winner = play_set(p1_name, p2_name, sets)
            if set_winner == p1_name:
                set_p1 += 1
            else:
                set_p2 += 1
            set_scores.append((sets, p1_pts, p2_pts))
            if set_p1 < 2 and set_p2 < 2 and sets < 3:
                proceed = input("Do you want to continue to the next set? (y/n)")
                if proceed.lower() != 'y':
                    break
        winner=p1_name if set_p1 > set_p2 else p2_name
        display_scoreboard(p1_name, p2_name, set_scores, winner)
    else:
        print("Invalid choice")