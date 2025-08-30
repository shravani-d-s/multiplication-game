import random
import time
import matplotlib.pyplot as plt

def multiplication_game():
    """
    Runs a 10-question multiplication game for a single player.
    Returns the score and the time taken to complete the game.
    """
    score = 0
    start_time = time.time()
    print("\n--- Multiplication Game ---")
    print("Answer 10 multiplication questions as fast as you can!")

    for i in range(10):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 * num2
        
        while True:
            try:
                question = f"Question {i + 1}: What is {num1} x {num2}? "
                user_answer = int(input(question))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        if user_answer == correct_answer:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}. 😔")
            
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    
    print("\n--- Game Over ---")
    print(f"Your final score is {score}/10.")
    print(f"You took {time_taken} seconds to complete the game.")
    return time_taken

def award(player_data):
    """
    Awards prizes to the top three players and displays their results.
    
    Args:
        player_data (dict): A dictionary with player names as keys and time taken as values.
    """
    # Sort players by time taken (ascending)
    # The sorted() function returns a list of tuples (player_name, time_taken)
    sorted_players = sorted(player_data.items(), key=lambda item: item[1])
    
    print("\n--- 🏆 Leaderboard & Awards 🏆 ---")
    
    if len(sorted_players) >= 1:
        print(f"🥇 Gold Medal: {sorted_players[0][0]} with {sorted_players[0][1]} seconds!")
    if len(sorted_players) >= 2:
        print(f"🥈 Silver Medal: {sorted_players[1][0]} with {sorted_players[1][1]} seconds!")
    if len(sorted_players) >= 3:
        print(f"🥉 Bronze Medal: {sorted_players[2][0]} with {sorted_players[2][1]} seconds!")

    print("\n--- Full Results ---")
    for i, (player, time_val) in enumerate(sorted_players):
        print(f"{i + 1}. {player}: {time_val} seconds")


def visualize_results(player_data):
    """
    Creates a bar chart to visualize the time taken by each player.

    Args:
        player_data (dict): A dictionary with player names as keys and time taken as values.
    """
    players = list(player_data.keys())
    times = list(player_data.values())
    
    plt.figure(figsize=(12, 6))
    plt.bar(players, times, color='skyblue')
    
    plt.xlabel("Player Names", fontsize=12)
    plt.ylabel("Time Taken (seconds)", fontsize=12)
    plt.title("Time Taken by Each Player in Multiplication Game", fontsize=14)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout() # Adjust layout to make room for rotated x-axis labels
    
    # Add the time value on top of each bar
    for i, time_val in enumerate(times):
        plt.text(i, time_val + 0.5, str(time_val), ha='center', fontweight='bold')
        
    plt.show()

def main():
    """
    Main function to run the program for 10 players.
    """
    player_results = {}
    num_players = 10 
    
    # Pre-defined list of names for demonstration
    player_names = [
        "Alex", "Ben", "Charlie", "David", "Eva", 
        "Frank", "Grace", "Hannah", "Ian", "Jack"
    ]

    print(f"--- Starting the game for {num_players} players ---")

    for i in range(num_players):
        player_name = player_names[i]
        print(f"\n--- It's {player_name}'s turn! ---")
        
        # Run the game for the current player
        time_taken = multiplication_game()
        
        # Store the result
        player_results[player_name] = time_taken
        
        print(f"\nThank you, {player_name}! Your time has been recorded.")
        # A small delay before the next player starts
        if i < num_players - 1:
            print("Next player, get ready...")
            time.sleep(2)

    # Display awards and leaderboard
    award(player_results)
    
    # Visualize the results
    visualize_results(player_results)


if __name__ == "__main__":
    main()
