# PLAYER CLASS
class Player:
    def __init__(self, name):
        self.name = name
        self.set_wins = 0

# BADMINTONMATCH CLASS
class BadmintonMatch:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.set_scores = []

    def play(self, player1_name, player2_name, set_number): 
        player1_points = 0 
        player2_points = 0 
        print(f"\n{player1_name} vs {player2_name} | Set {set_number}")  
        while not ((player1_points >= 3 or player2_points >= 3) and abs(player1_points - player2_points) >= 2): 
            scored_player = input("Who won the point:- ")
            if scored_player == player1_name: 
                player1_points += 1 
            elif scored_player == player2_name: 
                player2_points += 1 
            else:
                print("Invalid name")
                continue
            if player1_points == 5 or player2_points == 5:
                print(f"----- SCOREBOARD (Set {set_number}) -----")
                print(f"{player1_name} : {player1_points}")
                print(f"{player2_name} : {player2_points}")
                break
            print(f"----- SCOREBOARD (Set {set_number}) -----")
            print(f"{player1_name} : {player1_points}")
            print(f"{player2_name} : {player2_points}")
        score_tuple = (set_number, player1_points, player2_points)
        self.set_scores.append(score_tuple)
        
        if player1_points > player2_points:
            print(f"{player1_name} wins Set {set_number}")
            self.player1.set_wins += 1
            return player1_name 
        else:
            print(f"{player2_name} wins Set {set_number}")
            self.player2.set_wins += 1
            return player2_name

    def play_match(self):
        set_number = 1
        while set_number <= 3:
            winner_name = self.play(self.player1.name, self.player2.name, set_number)
            if self.player1.set_wins >= 2 or self.player2.set_wins >= 2:
                break
            proceed = input("Do you want to continue to the next set? (y/n): ")
            if proceed.lower() != 'y':
                break
            set_number += 1

    def get_winner(self):
        if self.player1.set_wins > self.player2.set_wins:
            return self.player1.name
        elif self.player2.set_wins>self.player1.set_wins:
            return self.player2.name
        else:
            return "Match tied!"

# SCOREBOARD CLASS
class Scoreboard:
    @staticmethod
    def display_scoreboard(player1_name, player2_name, set_scores, winner): 
        #Header
        print(f"{'Player'}",end="")
        for i in range(1,4):
            print(f"\tSet {i}",end="")
        print()
        #Player 1
        print(f"{player1_name}",end="")
        for s,p1,p2 in set_scores:
            print(f"\t{p1}",end="")
        print()
        #Player 2
        print(f"{player2_name}",end="")
        for s,p1,p2 in set_scores:
            print(f"\t{p2}",end="")
        print()
        print(f"\nMatch Winner: {winner}")
# MAIN PROGRAM
while True:
    print("\n\t\t Available Games ")
    print("\t 1. Volleyball")
    print("\t 2. Tennis")
    print("\t 3. Badminton")
    print("\t 4. Exit")

    choice = int(input("Enter your choice:- "))

    if choice == 1 or choice == 2:
        print("Welcome to the game! Scoreboard will be updated soon")
    elif choice == 4:
        print("Thank you!")
        break
    elif choice == 3:
        print("Welcome to Badminton!")

        player1_name = input("Enter Player 1 name:- ")
        player2_name = input("Enter Player 2 name:- ")

        player1 = Player(player1_name)
        player2 = Player(player2_name)

        match = BadmintonMatch(player1, player2)
        match.play_match()

        winner = match.get_winner()
        Scoreboard.display_scoreboard(player1_name, player2_name, match.set_scores, winner)
    else:
        print("Invalid choice")
