from DeckOfCards import * # importing the deck code from the other file

# introduction to the game
print("Welcome to the game of Black Jack!")
print("The goal of this game is to get as close to 21 as possible without going over.")
print("You can hit and get another card, or stand and keep your current hand.")


# Create the deck
deck = DeckOfCards()


# Continue playing until the user chooses not to play again
play_again = "yes"

while play_again == "yes":

    # Print the deck before and after it is shuffled
    print("\nDeck before shuffled:")
    deck.print_deck()

    deck.shuffle_deck()

    print("\nDeck after shuffled:")
    deck.print_deck()


    # Create empty lists for the player's and dealer's hands
    player_cards = []
    dealer_cards = []


    # Deal two cards to the player
    player_cards.append(deck.get_card())
    player_cards.append(deck.get_card())


    # Deal two cards to the dealer
    dealer_cards.append(deck.get_card())
    dealer_cards.append(deck.get_card())


    # Display the player's cards
    print("\nCard number 1 is:", player_cards[0].face, "of", player_cards[0].suit)
    print("Card number 2 is:", player_cards[1].face, "of", player_cards[1].suit)


    # Calculate the player's starting score
    player_score = 0
    player_aces = 0

    for card in player_cards:
        player_score = player_score + card.val

        if card.face == "Ace":
            player_aces = player_aces + 1


    # Change an Ace from 11 to 1 if the player would bust
    while player_score > 21 and player_aces > 0:
        player_score = player_score - 10
        player_aces = player_aces - 1


    print("Your total score is:", player_score)


    # Let the player continue hitting while they want another card
    hit = input("Would you like a hit? (yes/no): ")


    while hit == "yes" and player_score <= 21:

        # Give the player another card
        new_card = deck.get_card()
        player_cards.append(new_card)

        print("Card number", len(player_cards), "is:",
              new_card.face, "of", new_card.suit)


        # Recalculate the player's score
        player_score = 0
        player_aces = 0

        for card in player_cards:
            player_score = player_score + card.val

            if card.face == "Ace":
                player_aces = player_aces + 1


        # Change Aces from 11 to 1 if necessary
        while player_score > 21 and player_aces > 0:
            player_score = player_score - 10
            player_aces = player_aces - 1


        print("Your total score is:", player_score)


        # If the player has not busted, ask if they want another card
        if player_score <= 21:
            hit = input("Would you like a hit? (yes/no): ")


    # If the player busts, they automatically lose
    if player_score > 21:

        print("Your score is over 21. You busted, you lose!")

    else:

        # Reveal the dealer's cards
        print("\nDealer card number 1 is:",
              dealer_cards[0].face, "of", dealer_cards[0].suit)

        print("Dealer card number 2 is:",
              dealer_cards[1].face, "of", dealer_cards[1].suit)


        # Calculate the dealer's starting score
        dealer_score = 0
        dealer_aces = 0

        for card in dealer_cards:
            dealer_score = dealer_score + card.val

            if card.face == "Ace":
                dealer_aces = dealer_aces + 1


        # Change an Ace from 11 to 1 if necessary
        while dealer_score > 21 and dealer_aces > 0:
            dealer_score = dealer_score - 10
            dealer_aces = dealer_aces - 1


        # Dealer must hit while their score is below 17
        while dealer_score < 17:

            new_card = deck.get_card()
            dealer_cards.append(new_card)

            print("Dealer hits, card number", len(dealer_cards), "is:",
                  new_card.face, "of", new_card.suit)


            # Recalculate dealer's score
            dealer_score = 0
            dealer_aces = 0

            for card in dealer_cards:
                dealer_score = dealer_score + card.val

                if card.face == "Ace":
                    dealer_aces = dealer_aces + 1


            # Change Aces from 11 to 1 if necessary
            while dealer_score > 21 and dealer_aces > 0:
                dealer_score = dealer_score - 10
                dealer_aces = dealer_aces - 1


        print("Dealer score is:", dealer_score)


        # Determine the winner
        if dealer_score > 21:
            print("Dealer busted, you win!")

        elif player_score > dealer_score:
            print("Your score is higher, you win!")

        else:
            print("Dealer score is higher or equal, you lose!")


    # Ask whether the player wants another game
    play_again = input("\nAnother game? (yes/no): ")

    if play_again == "no":
        print("Thanks for playing, play again soon!")