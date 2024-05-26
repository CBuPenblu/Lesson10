#Creation of Hero Class
class Hero:
    #Creation of Hero class definitions
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} attack {other.name} and make {damage} of damage!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Attack power: {self.attack_power}"

#Creation of Game class
class Game:
    #Creation of Game class definitions
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("The game has begun!")
        print(self.player)
        print(self.computer)
        print()

        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.computer.name} has fallen! {self.player.name} win!")
                break

            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.player.name} has fallen! {self.computer.name} win!")
                break

            self.show_health_status()

    def player_turn(self):
        self.player.attack(self.computer)

    def computer_turn(self):
        self.computer.attack(self.player)

    def show_health_status(self):
        print(f"\n{self.player.name} - Health: {self.player.health}")
        print(f"{self.computer.name} - Health: {self.computer.health}")
        print()

#Creation of characters
player = Hero(name="Player")
computer = Hero(name="Computer")

#Creation of game initialization
game = Game(player, computer)
game.start()
