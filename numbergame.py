# Import the random module
import random
import sys

def main():
    # Set the number of attempts to 0
    number_of_attempts = 0
    
    # Generate a random number between 1 and 10
    correct_number = random.randint(1, 10)
         
    # Use a while loop to repeat the game as long as the user has not used up all attempts
    while number_of_attempts < 3:
        
        # Ask the user to guess a number between 1 and 10
        user_guess = input("Guess a number between 1 and 10: ")
        
        # Handle potential errors from non-integer guesses
        try:
            # Convert the user's input to an integer
            user_guess = int(user_guess)

            # Check if the user's guess is equal to the correct number
            if user_guess == correct_number:
                # Congratulate the user and end the program
                print("Congratulations! You guessed the correct number.")
                play_again()
                
            # Check if the user's guess is smaller than the correct number
            elif user_guess < correct_number:
                # Give a hint and ask the user to guess again
                print("Too small. Guess again.")
                number_of_attempts += 1
            # If the above did not apply, the user's guess must be larger
            else:
                # Give a hint and ask the user to guess again
                print("Too large. Guess again.")
                number_of_attempts += 1
        # If the user's input cannot be converted to an integer, display an error message
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
        
        # If the user ran out of attempts without guessing the correct number, display a "lose" message
        if number_of_attempts == 3:
            print("Too bad, you ran out of attempts. The correct number was " + str(correct_number) + ".")
            play_again()
    return
          
def play_again():
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (Y/N)")

    # Restart game if player chooses 'yes'.
    if play_again.lower() == "y":
        main()

    # Otherwise, end the program
    else:
        print("Thank you for playing the number guessing game!")
        sys.exit()
    return

if __name__ == "__main__":
    main()