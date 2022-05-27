from Player import Player
from Dealer import Dealer
from DrawPile import DrawPile

def main():
    print("Welcome to BLACKJACK!\n\n")

    player_name = get_player_name()

    player = Player(player_name)
    dealer = Dealer()

    print(f"\nHello {player.get_name()}!\n")

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
        print(f"\nHow many decks would you like to play with, {player.get_name()}?\n")
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

    draw_pile = DrawPile(amount_of_decks)
    print("")

    while keep_playing:
        bet = get_bet_amount(player)
        play_round(draw_pile, player, dealer, bet)

        if player.get_total_balance() <= 0:
            print("Game over! You've lost all your money!")
            keep_playing = False
        else:
            print("\nKeep playing? (y/n)\n")
            keep_playing = get_yes_or_no_input()
        
        print("")

def play_round(draw_pile, player, dealer, bet):
    player.reset_total_hand_value()
    dealer.reset_total_hand_value()

    player_stand = False
    quit_game = False
    winner = ""

    starting_hand(player, dealer, draw_pile)
    winner = check_if_starting_hands_win(player, dealer)

    if winner != "Draw":
        quit_game = True

    while quit_game != True:
        if player_stand == False:
            print(f"Deal you a new card, {player.get_name()}? (y/n)\n")

            deal_new_card = get_yes_or_no_input()
            print("")

            if deal_new_card:
                add_card_to_hand(player, draw_pile)

                winner = check_if_blackjack_or_bust(player, dealer)

                if winner != "Draw":
                    break
            else:
                player_stand = True

        if dealer.get_total_hand_value() < 17:
            add_card_to_hand(dealer, draw_pile)

            winner = check_if_blackjack_or_bust(dealer, player)
            
            if winner != "Draw":
                break

        if player_stand and dealer.get_total_hand_value() >= 17:
            quit_game = True

    show_final_hands(player, dealer, winner, bet)

def get_bet_amount(player):
    bet = 0
    is_number = False

    while is_number == False or bet <= 0 or bet > player.get_total_balance():
        print(f"You have £{player.get_total_balance():.2f} to bet.")
        print("How much would you like to bet?\n")

        bet_string = input().strip()
        print("")

        try:
            bet = float(bet_string)
            if bet <= 0:
                print("You can't bet 0 or less! Where's the fun in that?\n")
            elif bet > player.get_total_balance():
                print("You don't have that much money!\n")
            else:
               is_number = True
        except ValueError:
            print(f"{bet_string} is not a valid number! Please type in a number and try again.\n")

    return bet

def starting_hand(player, dealer, draw_pile):
    print("***STARTING HANDS***")

    add_card_to_hand(player, draw_pile)
    add_card_to_hand(dealer, draw_pile)
    add_card_to_hand(player, draw_pile)
    add_card_to_hand(dealer, draw_pile)

def add_card_to_hand(player, draw_pile):
    card = draw_pile.draw_card()
    print(f"{player.get_name()} draws {card.get_name()}")
    player.add_value_to_hand(card.get_value())
    print(f"{player.get_name()}'s hand: {player.get_total_hand_value()}\n")

def check_if_starting_hands_win(player, dealer):
    natural_blackjack_winner_player = check_if_blackjack_or_bust(player, dealer)
    natural_blackjack_winner_dealer = check_if_blackjack_or_bust(dealer, player)

    if natural_blackjack_winner_player == dealer.get_name() and natural_blackjack_winner_dealer == player.get_name():
        return "DoubleBust"
    elif natural_blackjack_winner_player == player.get_name() and natural_blackjack_winner_dealer == dealer.get_name():
        return "StandOff"
    elif natural_blackjack_winner_player == player.get_name():
        return "Natural"
    elif natural_blackjack_winner_dealer == dealer.get_name():
        return dealer.get_name()
    else:
        return "Draw"

def check_if_blackjack_or_bust(player_to_check, opponent):
    if player_to_check.get_total_hand_value() == 21:
        print("Blackjack!")
        return player_to_check.get_name()
    elif player_to_check.get_total_hand_value() > 21:
        print("Bust!")
        return opponent.get_name()
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
    print(f"\n{player.get_name()}: {player.get_total_hand_value()}")
    print(f"{dealer.get_name()}: {dealer.get_total_hand_value()}\n")

    if player.get_total_hand_value() > dealer.get_total_hand_value() and player.get_total_hand_value() <= 21:
        winner = player.get_name()
    elif dealer.get_total_hand_value() > player.get_total_hand_value() and dealer.get_total_hand_value() <= 21:
        winner = dealer.get_name()

    if winner == player.get_name():
        print(f"\nCongratulations, {player.get_name()}! You win! £{bet:.2f} added to your balance.")
        player.add_to_total_balance(bet)
        player.add_win_to_score()
    elif winner == dealer.get_name():
        print(f"\nToo bad, {player.get_name()}! {dealer.get_name()} wins! You lost £{bet:.2f}.")
        dealer.add_win_to_score()
        player.subtract_from_total_balance(bet)
    elif winner == "Natural":
        bet *= 1.5
        print(f"Natural Blackjack! You win £{bet:.2f}!")
        player.add_to_total_balance(bet)
        player.add_win_to_score()
    elif winner == "StandOff":
        print("Stand Off! You both win! Your bet is refunded.")
        player.add_win_to_score()
        dealer.add_win_to_score()
    elif winner == "DoubleBust":
        print(f"Double Bust! You both lose! You lost £{bet:.2f}.")
        player.subtract_from_total_balance(bet)
    else:
        print("\nWell how about that? It's a draw! Your bet is refunded.")

    print("")

def show_final_scores(player, dealer):
    print("***FINAL SCORES***")
    print(f"\n{player.get_name()}: {player.get_score()} win" + ("s" if player.get_score() != 1 else "") + ".")
    print(f"\n{dealer.get_name()}: {dealer.get_score()} win" + ("s" if dealer.get_score() != 1 else "") + ".")
    print(f"\n{player.get_name()}'s Final Balance: £{player.get_total_balance():.2f}")

main()