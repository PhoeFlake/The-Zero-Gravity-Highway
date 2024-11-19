import random
from constellations_data import ConstellationsData

class SpaceshipGame:
    def __init__(self, cat_name):
        self.position = [0, 0, 0]
        self.cat_name = cat_name
        self.constellation_manager = ConstellationsData()
        self.nearby_constellations = []

    def _cat_speaks(self, message):
        """Format the cat's dialogues."""
        return f"{self.cat_name} 🐾: {message}"

    def move_spaceship(self):
        """Move the spaceship in a random direction."""
        movement = random.randint(-10, 10)
        direction = random.choice(['x', 'y', 'z'])

        if direction == 'x':
            self.position[0] += movement
        elif direction == 'y':
            self.position[1] += movement
        else:
            self.position[2] += movement

        self._generate_nearby_constellations()
        position_info = f"We moved {movement} units along the {direction}-axis. Current position: {self.position}."
        return self._cat_speaks(position_info)

    def _generate_nearby_constellations(self):
        """Generate nearby constellations based on current position."""
        possible_constellations = list(self.constellation_manager.folklores.keys())
        self.nearby_constellations = random.sample(
            possible_constellations, 
            min(3, len(possible_constellations))
        )

    def list_nearby_constellations(self):
        """List constellations near the spaceship."""
        if not self.nearby_constellations:
            return self._cat_speaks("Looks like the stars are shy today. No constellations nearby.")
        return self._cat_speaks(f"Nearby constellations: {', '.join(self.nearby_constellations)}")

    def explore_constellation(self, constellation):
        """Explore a constellation's folklore."""
        if constellation not in self.nearby_constellations:
            return self._cat_speaks("This constellation is not nearby. We need to move closer!")
        
        folklores = self.constellation_manager.get_folklore(constellation)
        if folklores:
            return self._cat_speaks(f"Here's the tale of {constellation}:\n{folklores}")
        return self._cat_speaks(f"Even I don't know the stories of {constellation} yet.")

def main():
    print("\nWelcome to the Space Exploration Game!")
    cat_name = input("Name your cat astronaut: ").strip() or "Luna"
    game = SpaceshipGame(cat_name)

    while True:
        print("\n--- Space Exploration Menu ---")
        print("1. Move Spaceship")
        print("2. Check Nearby Constellations")
        print("3. Explore a Constellation")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(game.move_spaceship())
        elif choice == '2':
            print(game.list_nearby_constellations())
        elif choice == '3':
            const = input("Enter the name of a constellation to explore: ").strip().title()
            print(game.explore_constellation(const))
        elif choice == '4':
            print(f"{game.cat_name} 🐾: Goodbye, space explorer! May your stars always shine bright!")
            break
        else:
            print(f"{game.cat_name} 🐾: That's not a valid choice. Try again!")

if __name__ == "__main__":
    main()
