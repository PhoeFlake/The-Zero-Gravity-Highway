from spaceship_game import SpaceshipGame
from constellations_data import ConstellationsData
import random
import time
import os
import sys

class SpaceCatAdventure:
    def __init__(self, cat_name):
        self.constellation_data = ConstellationsData()
        self.spaceship = SpaceshipGame(cat_name)
        self.cat_name = cat_name
        self.achievements = {
            "total_distance_traveled": 0,
            "constellations_explored": set(),
            "special_discoveries": []
        }

    def cosmic_trivia(self):
        """Generate a random cosmic trivia question."""
        trivia_questions = [
            {
                "question": "Which constellation is known as the Great Bear?",
                "answer": "Ursa Major"
            },
            {
                "question": "What is the brightest star in the night sky?",
                "answer": "Sirius"
            },
            {
                "question": "Which constellation represents a hunter in Greek mythology?",
                "answer": "Orion"
            }
        ]
        return random.choice(trivia_questions)

    def space_event_generator(self):
        """Generate random space events during journey."""
        events = [
            f"{self.cat_name} encounters a cosmic dust cloud! Visibility is low.",
            f"A meteor shower lights up {self.cat_name}'s view!",
            f"{self.cat_name} detects unusual radio signals from a distant star system.",
            f"Gravitational waves ripple past {self.cat_name}'s spaceship.",
            "A rare stellar phenomenon appears briefly in the distance!"
        ]
        return random.choice(events)

    def play_game(self):
        print(f"\n🚀 Welcome aboard, Captain {self.cat_name}! 🐱")
        print("Prepare for an interstellar adventure through cosmic folklore!")
        
        while True:
            print("\n--- Cosmic Journey Menu ---")
            print("1. Move Spaceship")
            print("2. Explore Nearby Constellations")
            print("3. Learn Constellation Folklore")
            print("4. Check Space Achievements")
            print("5. Cosmic Trivia")
            print("6. Quit Mission")

            choice = input("Choose your cosmic adventure: ")

            if choice == '1':
                # Move spaceship and potentially trigger space events
                move_result = self.spaceship.move_spaceship()
                print(move_result)
                
                # Random chance of space event
                if random.random() < 0.3:
                    print(self.space_event_generator())
                
                # Update total distance
                self.achievements['total_distance_traveled'] += abs(sum(self.spaceship.position))

            elif choice == '2':
                print(self.spaceship.list_nearby_constellations())

            elif choice == '3':
                const = input("Which constellation's folklore do you want to explore? ").strip().title()
                folklore_result = self.spaceship.explore_constellation(const)
                print(folklore_result)
                
                # Track explored constellations
                if const in self.spaceship.nearby_constellations:
                    self.achievements['constellations_explored'].add(const)

            elif choice == '4':
                print("\n--- Space Cat's Log: Achievements ---")
                print(f"Total Distance Traveled: {self.achievements['total_distance_traveled']} light-years")
                print("Constellations Explored:")
                for const in self.achievements['constellations_explored']:
                    print(f"  🌟 {const}")

            elif choice == '5':
                trivia = self.cosmic_trivia()
                print(trivia['question'])
                answer = input("Your answer: ").strip().title()
                
                if answer == trivia['answer']:
                    print("🎉 Correct! You're a true space explorer!")
                    # Potential small reward/achievement
                    self.achievements['special_discoveries'].append("Cosmic Trivia Master")
                else:
                    print(f"Oops! The correct answer was {trivia['answer']}.")

            elif choice == '6':
                print(f"{self.cat_name} 🐾: Farewell, space explorer! See you among the stars!")
                break

            else:
                print(f"{self.cat_name} 🐾: Invalid choice. Let's try that again!")

            # Small pause for dramatic effect
            time.sleep(1)

def launch_game():
    """
    Safely launch the game in an external terminal
    """
    # Get the full path to the current script
    script_path = os.path.abspath(sys.argv[0])
    
    # Use start command to open a new CMD window and run the script
    os.system(f'start cmd /c "python "{script_path}" & pause"')

def main():
    if 'LAUNCHED_FROM_EXTERNAL' not in os.environ:
        # Set environment variable to prevent recursive launching
        os.environ['LAUNCHED_FROM_EXTERNAL'] = '1'
        launch_game()
        sys.exit()
    print("\n🌌 Welcome to The Zero Gravity Highway 🐱🚀")
    cat_name = input("Name your space-faring feline companion: ").strip() or "Luna"
    game = SpaceCatAdventure(cat_name)
    game.play_game()

if __name__ == "__main__":
    main()