#DEFINE POKEMON CLASS
class Pokemon:
  def __init__(self, name, type, level = 5):
    self.name = name
    self.level = level
    self.type = type
    self.max_health = level * 5
    self.health = level * 5
    self.experience = 0
    self.is_knocked_out = False

#Check Pokemon's current stats
  def __repr__(self):
    return '{name} (Level - {level}, Type - {type}, Health - {health}, Experience - {experience})'.format(name = self.name, level = self.level, type = self.type, health = self.health, experience = self.experience)

#Knock out a Pokemon when health = 0
  def knock_out(self):
    self.is_knocked_out = True
    if self.health != 0:
      self.health = 0
    print('{name} was knocked out!'.format(name = self.name))

#Revive a Pokemon
  def revive(self):
    self.is_knocked_out = False
    if self.health == 0:
      self.health = 1
    print('{name} was revived!'.format(name = self.name))

#Lose health in battle, knock out if health reaches 0
  def lose_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.knock_out()
    print('{name} now has {health} health.'.format(name = self.name, health = self.health))

#Gain health, revive if health was 0, health cannot exceed health max
  def gain_health(self, amount):
    if self.health == 0:
      self.revive()
    self.health += amount
    if self.health >= self.max_health:
      self.health = self.max_health
    print('{name} now has {health} health.'.format(name = self.name, health = self.health))

#Attack another Pokemon
  def attack(self, opponent):
    #Method if offense has an advantage over opponent
    def opp_adv(self, opponent):
      damage_amt = round(self.level * 2)
      print('{name} attacked {opp_name} for {damage} damage points. It was super effective!'.format(name = self.name, opp_name = opponent.name, damage = damage_amt))
      opponent.lose_health(damage_amt)
      self.experience += 5
      if self.experience >= 20:
        self.level += 1
        self.experience = 0
        print('{name} leveled up!'.format(name = self.name))
    #Method if offense has  has an disadvantage over opponent
    def opp_dis(self, opponent):
      damage_amt = round(self.level * 0.5)
      print('{name} attacked {opp_name} for {damage} damage points. It wasn\'t very effective.'.format(name = self.name, opp_name = opponent.name, damage = damage_amt))
      opponent.lose_health(damage_amt)
      self.experience += 2
      if self.experience >= 20:
        self.level += 1
        self.experience = 0
        print('{name} leveled up!'.format(name = self.name))
    #If offense is knocked out
    if self.is_knocked_out:
      print('{pokemon} is knocked out an cannot attack.'.format(pokemon = self.name))
    #If opponent is already knocked out
    elif opponent.is_knocked_out:
      print('{pokemon} is knocked out an cannot be attacked.'.format(pokemon = opponent.name))
    #Pokemon offense advantage types
    elif self.type == opponent.type or self.type == 'Fire' and opponent.type == 'Grass' or self.type == 'Water' and opponent.type == 'Fire' or self.type == 'Grass' and opponent.type == 'Water':
      opp_adv(self, opponent)
    #Pokemon offense disadvantage types
    elif self.type == 'Fire' and opponent.type == 'Water' or self.type == 'Water' and opponent.type == 'Grass' or self.type == 'Grass' and opponent.type == 'Fire':
      opp_dis(self, opponent)

#DEFINE TRAINER CLASS
class Trainer:
  def __init__(self, pokemon_list, name, num_potions = 3):
    self.pokemons = pokemon_list
    self.name = name
    self.potions = num_potions
    self.current_pokemon = 0

#Check Trainer's Pokemon, current Pokemon, and potions
  def __repr__(self):
    print('Trainer {name} has the following Pokemon and potions:'.format(name = self.name))
    for pokemon in self.pokemons:
      print(pokemon)
    print('Potions - {amt}'.format(amt = self.potions))
    return 'Their current active pokemon is {name}.'.format(name = self.pokemons[self.current_pokemon].name)

#Use potion and revive a knocked out Pokemon
  def use_potion(self, potion):
    if self.potions > 0:
      self.potions -= potion
      print('You used a potion on {pokemon}.'.format(pokemon = self.pokemons[self.current_pokemon].name))
      #Revive Pokemon if it's health was 0
      if self.pokemons[self.current_pokemon].health == 0:
        self.pokemons[self.current_pokemon].revive()
      self.pokemons[self.current_pokemon].gain_health(10)
      #Potion cannot increase health beyond health max
      if self.pokemons[self.current_pokemon].health > self.pokemons[self.current_pokemon].max_health:
        self.pokemons[self.current_pokemon].health = self.pokemons[self.current_pokemon].max_health
    else:
      print('You have no potions to use.')

  #Attack another trainer's Pokemon
  def attack_opponent(self, opp_trainer):
    self.pokemons[self.current_pokemon].attack(opp_trainer.pokemons[opp_trainer.current_pokemon])

  #Switch current pokemon to another in your list
  def switch_current_pokemon(self, new_pokemon):
    if new_pokemon <= len(self.pokemons) and new_pokemon >= 0:
      #You cannot switch to a knocked out Pokemon
      if self.pokemons[new_pokemon].is_knocked_out:
        print('{pokemon} is knocked out. Choose another Pokemon.'.format(pokemon = self.pokemons[new_pokemon].name))
      #You cannot switch to your current Pokemon
      elif self.pokemons[new_pokemon] == self.pokemons[self.current_pokemon]:
        print('Choose another Pokemon. {pokemon} is already your current Pokemon.'.format(pokemon = self.pokemons[new_pokemon].name))
      #Switch to a new Pokemon in your list
      elif self.pokemons[new_pokemon] != self.pokemons[self.current_pokemon]:
        self.current_pokemon = new_pokemon
        print('Go {pokemon}, you\'re up!'.format(pokemon = self.pokemons[self.current_pokemon].name))

#POKEMON TO PLAY
Charmander = Pokemon('Charmander', 'Fire', level = 8)
Scorbunny = Pokemon('Scorbunny', 'Fire', level = 5)
Squirtle = Pokemon('Squirtle', 'Water', level = 6)
Blastoise = Pokemon('Blastoise', 'Water', level = 4)
Bulbasaur = Pokemon('Bulbasaur', 'Grass', level = 1)
Lotad = Pokemon('Lotad', 'Grass', level = 7)

#TRAINERS TO PLAY
Ash = Trainer([Charmander, Bulbasaur], 'Ash', num_potions = 10)
Blaine = Trainer([Squirtle, Lotad], 'Blaine', num_potions = 7)
Misty = Trainer([Scorbunny, Blastoise], 'Misty', num_potions = 8)

#Testing attacking
# Ash.attack_opponent(Blaine)
# Misty.attack_opponent(Ash)

#Testing using potions
# Charmander.knock_out()
# print(Ash)
# Ash.use_potion(1)
# print(Ash)

#Testing switching Pokemon
# Lotad.knock_out()
# Blaine.switch_current_pokemon(0)
# Blaine.switch_current_pokemon(1)
