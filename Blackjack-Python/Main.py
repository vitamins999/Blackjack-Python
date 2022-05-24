import Player
import DrawPile

def main():
    print("Welcome to BLACKJACK!\n\n")

    player_name = get_player_name()

    player = Player.Player(player_name)
    dealer = Player.Player("Dealer")

    print(f"\nHello {player.GetName()}!\n")

    amount_of_decks = get_amount_of_decks(player)
    play_game(player, dealer, amount_of_decks)
    show_final_scores(player, dealer)

def get_player_name():
    print("Please enter your name:")
    player_name = input().strip()

    return player_name

def get_amount_of_decks(player):
    amount_of_decks = 0
    is_number = False

    while is_number == False:
        print(f"\nHow many decks would you like to play with, {player.GetName()}?\n")
        amount_of_decks_string = input().strip()

        try:
            amount_of_decks = int(amount_of_decks_string)

            if amount_of_decks <= 0:
                print(f"{amount_of_decks_string} is not a valid number! Please type in a whole number and try again.\n")
            else:
                is_number = True
        except :
            print(f"{amount_of_decks_string} is not a valid number! Please type in a whole number and try again.\n")

    return amount_of_decks

def play_game(player, dealer, amount_of_decks):
    keep_playing = True

    drawPile = DrawPile.DrawPile(amount_of_decks)
    print("")

    while keep_playing:
        bet = get_bet_amount(player)
        play_round(drawPile, player, dealer, bet)

        if player.GetTotalBalance() <= 0:
            print("Game over! You've lost all your money!")
            keep_playing = False
        else:
            print("\nKeep playing? (y/n)\n")
            keep_playing = get_yes_or_no_input()
        
        print("")

def play_round(drawPile, player, dealer, bet):
    player.ResetTotalHandValue()
    dealer.ResetTotalHandValue()

    player_stand = False
    quit_game = False
    winner = ""

    starting_hand(player, dealer, drawPile)
    winner = check_if_starting_hands_win(player, dealer)

    if winner != "Draw":
        quit_game = True

    while quit_game != True:
        if player_stand == False:
            print(f"Deal you a new card, {player.GetName()}? (y/n)\n")

            deal_new_card = get_yes_or_no_input()
            print("")

            if deal_new_card:
                add_card_to_hand(player, drawPile)

                winner = check_if_blackjack_or_bust(player, dealer)

                if winner != "Draw":
                    break
            else:
                player_stand = True

        if dealer.GetTotalHandValue() < 17:
            add_card_to_hand(dealer, drawPile)

            winner = check_if_blackjack_or_bust(dealer, player)
            
            if winner != "Draw":
                break

        if player_stand and dealer.GetTotalHandValue() >= 17:
            quit_game = True

    show_final_hands(player, dealer, winner, bet)

def get_bet_amount(player):
    bet = 0
    is_number = False

    while is_number == False or bet <= 0 or bet > player.GetTotalBalance():
        print(f"You have £{player.GetTotalBalance():.2f} to bet.")
        print("How much would you like to bet?\n")

        bet_string = input().strip()
        print("")

        try:
            bet = float(bet_string)
            if bet <= 0:
                print("You can't bet 0 or less! Where's the fun in that?\n")
            elif bet > player.GetTotalBalance():
                print("You don't have that much money!\n")
            else:
               is_number = True
        except ValueError:
            print(f"{bet_string} is not a valid number! Please type in a number and try again.\n")

    return bet

def starting_hand(player, dealer, drawPile):
    print("***STARTING HANDS***")

    add_card_to_hand(player, drawPile)
    add_card_to_hand(dealer, drawPile)
    add_card_to_hand(player, drawPile)
    add_card_to_hand(dealer, drawPile)

def add_card_to_hand(player, drawPile):
    card = drawPile.DrawCard()
    print(f"{player.GetName()} draws {card.GetName()}")
    player.AddValueToHand(card.GetValue())
    print(f"{player.GetName()}'s hand: {player.GetTotalHandValue()}\n")

def check_if_starting_hands_win(player, dealer):
    natural_blackjack_winner_player = check_if_blackjack_or_bust(player, dealer)
    natural_blackjack_winner_dealer = check_if_blackjack_or_bust(dealer, player)

    if natural_blackjack_winner_player == dealer.GetName() and natural_blackjack_winner_dealer == player.GetName():
        return "DoubleBust"
    elif natural_blackjack_winner_player == player.GetName() and natural_blackjack_winner_dealer == dealer.GetName():
        return "StandOff"
    elif natural_blackjack_winner_player == player.GetName():
        return "Natural"
    elif natural_blackjack_winner_dealer == dealer.GetName():
        return dealer.GetName()
    else:
        return "Draw"

def check_if_blackjack_or_bust(player_to_check, opponent):
    if player_to_check.GetTotalHandValue() == 21:
        print("Blackjack!")
        return player_to_check.GetName()
    elif player_to_check.GetTotalHandValue() > 21:
        print("Bust!")
        return opponent.GetName()
    else:
        return "Draw"

def get_yes_or_no_input():
    while True:
        yes_or_no = input().strip().lower()

        if yes_or_no == "y" or yes_or_no == "yes":
            return True
        elif yes_or_no == "n" or yes_or_no == "no":
            return False
        else:
            print("\nPlease only answer 'yes', 'y', 'no', or 'n'.\n")
            continue

def show_final_hands(player, dealer, winner, bet):
    print("\n***FINAL HANDS***")
    print(f"\n{player.GetName()}: {player.GetTotalHandValue()}")
    print(f"{dealer.GetName()}: {dealer.GetTotalHandValue()}\n")

    if player.GetTotalHandValue() > dealer.GetTotalHandValue() and player.GetTotalHandValue() <= 21:
        winner = player.GetName()
    elif dealer.GetTotalHandValue() > player.GetTotalHandValue() and dealer.GetTotalHandValue() <= 21:
        winner = dealer.GetName()

    if winner == player.GetName():
        print(f"\nCongratulations, {player.GetName()}! You win! £{bet:.2f} added to your balance.")
        player.AddToTotalBalance(bet)
        player.AddWinToScore()
    elif winner == dealer.GetName():
        print(f"\nToo bad, {player.GetName()}! {dealer.GetName()} wins! You lost £{bet:.2f}.")
        dealer.AddWinToScore()
        player.SubtractFromTotalBalance(bet)
    elif winner == "Natural":
        bet *= 1.5
        print(f"Natural Blackjack! You win £{bet:.2f}!")
        player.AddToTotalBalance(bet)
        player.AddWinToScore()
    elif winner == "StandOff":
        print("Stand Off! You both win! Your bet is refunded.")
        player.AddWinToScore()
        dealer.AddWinToScore()
    elif winner == "DoubleBust":
        print(f"Double Bust! You both lose! You lost £{bet:.2f}.")
        player.SubtractFromTotalBalance(bet)
    else:
        print("\nWell how about that? It's a draw! Your bet is refunded.")

    print("")

def show_final_scores(player, dealer):
    print("***FINAL SCORES***")
    print(f"\n{player.GetName()}: {player.GetScore()} win" + ("s" if player.GetScore() != 1 else "") + ".")
    print(f"\n{dealer.GetName()}: {dealer.GetScore()} win" + ("s" if dealer.GetScore() != 1 else "") + ".")
    print(f"\n{player.GetName()}'s Final Balance: £{player.GetTotalBalance():.2f}")

main()