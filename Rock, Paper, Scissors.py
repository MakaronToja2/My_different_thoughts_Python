import random

def play():
    user = input("Choose your hand: r for rock, p for paper, s for scissors ")
    computer = random.choice(['r','p','s'])
    print (f"Computer choose {computer}")

    if user == computer:
        return ("We have a draw")
    if is_win(user,computer):
        return 'user won'
    return 'Computer won'
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
print (play())

