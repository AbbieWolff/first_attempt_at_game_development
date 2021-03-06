# Define and initialize character (not player or AI yet)
class Character:
    def __init__(self):
        self.name = ""
        self.attributes = []
        self.health = []
        self.level = []
        self.skills = []


# Character Attributes #
Character.attributes = {'name': "", 'level': "", 'skills': [], 'health': "", 'charisma': 0, 'fitness': 0, 'humor': 0,
                        'intelligence': 0, 'swagger': 0, 'creativity': 0}

# Character Attributes - Naming Conventions & Minimum/Maximum Limits #

health = (Character.attributes['health']) = Character.health = {'hp', 'status'}

'''
Health is the same as the character attribute of the same name, health.
It is made up of two parts: HP (the numerical value) and health status (how the character feels, in words).
HP is the total of energy, appetite and resistance to illness scores.
'''

hp = ('energy' + 'appetite' + 'resistance_to_illness')
hp_max = 25
hp_min = 0
hp_current = int()

char = (Character.attributes['charisma'])
char_max = 10
char_min = 0
char_current = []

fit = (Character.attributes['fitness'])
fit_max = 10
fit_min = 0
fit_current = int()
# Come back to fitness and all other attributes & skills to possibly have both an integer and a string value? #

hum = (Character.attributes['humor'])
hum_max = 10
hum_min = 0
hum_current = []

intel = (Character.attributes['intelligence'])
intel_max = 10
intel_min = 0
intel_current = []

swag = (Character.attributes['swagger'])
swag_max = 10
swag_min = 0
swag_current = []

create = (Character.attributes['creativity'])
create_max = 10
create_min = 0
create_current = []

'''
How should attribute and health status updates be implemented in the actual game?
1. Attributes are much more fluid and are the result of ongoing choices, behaviors, etc.
2. Skills are static. Once you gain a skill level, you can't lose it on that character.
3. Status updates on skills should appear every time your character levels up (if they're well-written).
4. Status updates on attributes should not appear every time. But how often? ... TBD
5. Currently, status updates just print to the screen when 'activated' by the appropriate conditions.
6. Once the UI has been created, change these status print functions to be some semblance of
'show up on the UI in [specific way]'.
7. The status updates for both attributes and skills must also be visible in the character menu when
the relevant skill/attribute is hovered over(?) or selected. [MAKE UI & CHARACTER MENU...]
'''

# Character Level #
level = Character.level = Character.attributes['level'] = {'survival' + 'social'}
level_max = 100
level_min = 0
level_current = int()

'''
Character level:
Character level is the same as the character attribute by the same name, level.
Character level is a numerical value between 0 and 100 that is the total of survival and social skill levels.

Leveling:
Character level is maxed when all skills are maxed, with survival level 60 and social level 40.
At the start of the game, player character is at level 0 in all skills until they attribute available skill points.
How many skill points should be available at the start of the game?

Menu:
Need to design the menu to attribute skill points & explain to player how this works.

Character level & other attributes:
How should personality interact with all of this? ...
How should health, including wellness, energy and appetite, effect this?
Obviously, when the character is starving, very sick or passed out, he/she can't work on skill development/leveling.
I don't want this whole game to feel like grinding... :(
'''

'''
Leveling:

In games like Skyrim, you learn skills by doing them. I want to emulate that.

However, as noted elsewhere, I want the character to have some available skill points at the start
so they're not totally useless at surviving and talking to others.

In Skyrim, they also have points to spend when you level up overall. I could also emulate that by
using milestones in the (currently 0-100) rang of character level points.

When the player reaches a level that is a multiple of five(?), she will receive 1 extra point to
spend on any skill the player chooses.

This should help mitigate some of the grinding/fatigue or dislike of practicing certain skills. For instance, if the player dislikes fishing or hunting in the game, it would be possible to always attribute
the extra unattributed skill points available upon 'leveling' (reaching the next 5th level) to those skills.

There should be a way to ensure that some skils compensate for others and that it is NOT
necessary to practice every skill to survive.
a. Add town/tribe NPCs that automatically adapt to be better at skills you're not so you can
purchase or barter for the resources/labor you don't want to do.
b. Do so without making it too easy or possible to rely entirely upon NPCs. You MUST have
something to barter or some way to pay for their help, by doing your own skill-building.

ADD GARDENING/GATHERING. DUH. WHY DIDN'T I THINK OF THIS EARLIER?!
'''


# Character skill sets: survival and social skills #
survival = ['hunting'+ 'fishing' + 'forestry' + 'cooking' + 'woodworking' + 'crafting']
survival_max = 60
survival_min = 0
survival_current = int()

social = ['communication' + 'romance' + 'parenting' + 'friendship']
social_max = 40
social_min = 0
social_current = int()

'''
Character Skills

Skills include two distinct categories: survival skills and social skills.

Survival skill level is the total of all skill levels in the category, with a max of level 60.
These skills include hunting, fishing, forestry, cooking, woodworking and crafting.

Social skill level is the total of all skill levels in the category, with a max of level 40.
These skills include communication, romance, parenting and friendship.

Each individual skill within both sets will have a numerical value from 0 to 10.
Should I change this to a scale of beginner, intermediate and advanced or low-, mid- and high-level?

I need to add:
-corresponding phrases upon each level-up (eventually).
-character menu to view skill progression and leveling
-relationship between other attributes and skills:
   - when health is low,
'''

# Skills - Naming Conventions & Minimum/Maximum Limits #
skill_hunt = 'hunting'
skill_hunt_max = 10
skill_hunt_min = 0
skill_hunt_current = ""

skill_fish = 'fishing'
skill_fish_max = 10
skill_fish_min = 0
skill_fish_current = ""

skill_cook = 'cooking'
skill_cook_max = 10
skill_cook_min = 0
skill_cook_current = ""

skill_comm = 'communication'
skill_comm_max = 10
skill_comm_min = 0
skill_comm_current = ""

skill_wood = 'woodworking'
skill_wood_max = 10
skill_wood_min = 0
skill_wood_current = ""

skill_rom = 'romance'
skill_rom_max = 10
skill_rom_min = 0
skill_rom_current = ""

skill_parent = 'parenting'
skill_parent_max = 10
skill_parent_min = 0
skill_parent_current = ""

skill_friend = 'friendship'
skill_friend_max = 10
skill_friend_min = 0
skill_friend_current = ""

skill_forest = 'forestry'
skill_forest_max = 10
skill_forest_min = 0
skill_forest_current = ""

skill_craft = 'crafting'
skill_craft_max = 10
skill_craft_min = 0
skill_craft_current = ""


# Attributes - health - Conditions - Define energy and appetite, including minimums & maximums & conditions #
energy = []
energy_max = 10
# higher energy = less tired #
energy_min = 0
# lower energy = more tired #
energy_current = int()
# used to be called fatigue, but that screwed up the HP system #

appetite = []
appetite_max = 10
# higher appetite = less hungry, more satiated #
appetite_min = 0
# lower appetite = more hungry #
appetite_current = int()


# Attributes - health - Conditions - Define wellness and immunity and their relationship #
resistance_to_illness = 'wellness' + 'immunity'

wellness = []
wellness_max = 5
# higher wellness = more ill #
wellness_min = 0
# lower wellness = less ill #
wellness_current = int()

immunity = []
immunity_max = 10
# higher immunity = less likely to get sick and faster recovery from illnesses #
immunity_min = 0
# lower immunity = more likely to get sick and slower recovery from illnesses #
immunity_current = int()


'''
IDEA: Notifications about wellness & immunity will be separate, despite their relationship.
IDEA: Notifications will show up when the section is hovered over in the UI during game play.
IDEA: When the game is paused and the character menu/panel is open, these stats will show 24/7.
IMPLEMENTATION OF PRECEDING IDEAS: Still need to program the character, the UI, the menu, etc....
'''


if immunity_current is immunity_min and wellness_current is wellness_max:
    wellness_current = (wellness_min + 2)
    # if your immunity falls to 0 but your wellness is max, your wellness will drop to 2 (you'll get sick).

if immunity_current is immunity_min:
    wellness_current -= 1
    # lose one wellness point upon complete loss of immunity. #
    print("You have experienced a complete loss of immune system function! As a result, you are sick.")

if immunity_current is immunity_min and wellness_current <= (wellness_min +1):
    wellness_current = wellness_min
    print("You are deathly ill with a completely useless immune system! "
          "As a result, you are dangerously fatigued and have lost all health points.")
    energy_level = energy_min
    # By reaching min wellness and 0 immunity, your energy level decreases to min. #
    hp_current = hp_min
    # By reaching min wellness and 0 immunity, your current health drops to 0. You pass out. #

if wellness_current is wellness_min and immunity_current <= ((immunity_max / 2) - 1):
    immunity_current -= 1
    print("You are fatally ill!")

if immunity_current is (immunity_min + 1):
    print("You are highly susceptible to illness.")

if wellness_current is (wellness_min + 1):
    print("You are very ill.")

if immunity_current is 2:
    print("Your immune response is slow and increasingly ineffective.")

if wellness_current is (wellness_min + 2):
    print("You are sick.")

if immunity_current is (immunity_min + 3) or (immunity_min + 4):
    print("You have an average immunity to illnesses.")

if wellness_current is (wellness_max - 2):
    print("You're just a bit sick.")

if wellness_current is (wellness_max - 1):
    print("You are actively fighting off an illness")

if immunity_current >= 5:
    wellness_current += 1
    # if current immunity is at least 5, gain one current wellness level as a benefit #
    print("Your immune system is functioning well. You are unlikely to get sick(er).")

if immunity_current >= 5 and wellness_current >= (wellness_max / 2):
    wellness_current = 3
    # current wellness must be at least 3 if current immunity is at least 5 #
    print("Your high-functioning immune response cured you of illness (mostly).")

if immunity_current is immunity_max or (immunity_max - 1):
    print("All illnesses have been cured! You are now disease-free and, at least momentarily, immune to illness! "
          "You have also earned an increase in health and fitness!")
    wellness_current = wellness_max
    # reaching max immunity cures all illnesses #

    if hp_current != hp_max:
        hp_current += 1
    # reaching max immunity and 0 wellness grants +1 health unless maxed #

    if fit_current != fit_max:
        fit_current += 1
    # reaching max immunity and 0 wellness grants +1 Fitness unless maxed #

if wellness_current is wellness_max and immunity_current is not immunity_max:
    immunity_current += 1
    # being cured of all illnesses grants one current immunity level (except if already max level) #

if wellness_current is wellness_max and immunity_current < (immunity_max / 2):
    immunity_current = (immunity_max / 2)
    # current immunity must be at least at the midpoint if all illnesses were cured #
    print("By curing yourself of all illnesses, you boosted your immune response.")


# Attributes - health - Conditions - Set conditions of energy #
if energy_current is energy_min:
    hp_current = 0
    # min energy results in complete loss of health and thus loss of consciousness #

    if immunity_current is not immunity_min:
        immunity_current -= 1
    # min energy (high fatigue) results in a lower immune response #

    if wellness_current is not wellness_min:
        wellness_current -= 1
    # min energy level (high fatigue) results in a lower wellness level (more illness) #

    print("You are dangerously exhausted! "
          "As a result, you have become more susceptible to illness and have lost all health points.")

if energy_current is energy_max:

    if hp_current is not hp_max:
        hp_current += 1
    # max energy results in increased health (if not max) #

    if hp_current is not immunity_max:
        immunity_current += 1
    # max energy results in increased immunity (if not max) #

    if wellness_current is not wellness_max:
        wellness_current += 1
    # max energy results in less illness / more wellness (if not max) #

    print("Oh, yeah! You are bursting with energy! "
          "As a result, you have increased resistance to illness and increased health points.")


# Attributes - health - Status and printed comments about status are dependent upon current health (0-10) #
if hp_current is hp_min:
    health.status = 'unconscious'
    print("You fainted!")

    if fit_current is not fit_min:
        fit_current -= 1
    # lose one fitness point each time you faint #

elif hp_current is (hp_min + 1) or (hp_min + 2):
    health.status = 'ill'
    print("The darkness is closing in.... If you don't get help immediately, you'll pass out!")
    # final warning #

elif hp_current > (hp_min + 2) <= (hp_min + 5):
    health.status = 'unwell'
    print("You are dizzy. You need rest, medicine and sustenance.")
    # first warning #

    if energy_current is not energy_min:
        energy -= 1
    # lose one energy point, becoming more fatigued, when you reach low health #

    if wellness_current is not wellness_min:
        wellness_current -= 1
    # lose one wellness point, becoming more prone to illness, when you reach low health #

elif hp_current > (hp_min + 5) <= (hp_min + 10):
    health.status = 'mediocre'
    print("You're alright. Find food and shelter to feel better.")
    # Remove the warning? Will this be annoying? #

elif hp_current > (hp_min + 10) <= (hp_max - 10):
    health.status = 'good'
    print("You're doing well.")

elif hp_current > (hp_max - 10) < (hp_max - 5):
    health.status = 'excellent'
    print("You feel great!")

    if fit_current is not fit_max:
        fit_current += 1
    # gain one fitness point each time you reach high health #

elif hp_current >= (hp_max - 5):
    health.status = 'very healthy'
    print("You've developed increased immunity, wellness, energy and appetite!")

    if fit_current is not fit_max:
        fit_current += 2
    # gain two fitness points each time you reach max health #

    if energy_current is not energy_max:
        energy_current += 1
    # gain one energy point, becoming more energized, when you reach max health #

    if wellness_current is not wellness_max:
        wellness_current += 1
    # gain one wellness point, becoming less prone to illness, when you reach max health #

    if appetite_current is not appetite_max:
        appetite += 1
    # gain one appetite point, becoming more satiated & less prone to starvation, when you reach max health #


# Attributes - health - Create health status, make a list of health status options #

'''
 want to show the health status in the UI when hovered over and as it changes, with a color gradient from green-red
 >>>health.status_bar is ['green', 'yellow-green', 'yellow', 'yellow-orange', 'orange', 'orange-red', 'red']
 make colors correspond with distinct status states, not just health values?
 colors to show sickly green vs healthy red... or reverse? healthy green and blood red is standard... hm
'''


