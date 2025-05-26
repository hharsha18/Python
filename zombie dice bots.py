print("Harsha D S, USN:1AY24AI041, SEC:M")
import random

DICE_POOL = {
    'green': ['brain', 'brain', 'brain', 'footsteps', 'footsteps', 'shotgun'],
    'yellow': ['brain', 'brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun'],
    'red': ['brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun', 'shotgun']
}
ALL_DICE = ['green'] * 6 + ['yellow'] * 4 + ['red'] * 3

def roll_die(color):
    return random.choice(DICE_POOL[color])

def draw_dice(dice_pool, n=3):
    return [dice_pool.pop(random.randint(0, len(dice_pool)-1)) for _ in range(min(n, len(dice_pool)))]

def zombie_bot_turn(name="Bot"):
    dice_pool = ALL_DICE.copy()
    random.shuffle(dice_pool)

    brains, shotguns, footprints = 0, 0, []

    while True:
        needed = 3 - len(footprints)
        drawn_dice = footprints + draw_dice(dice_pool, needed)
        footprints = []
        results = [roll_die(color) for color in drawn_dice]

        for i, res in enumerate(results):
            if res == 'brain': brains += 1
            elif res == 'shotgun': shotguns += 1
            else: footprints.append(drawn_dice[i])

        if shotguns >= 3:
            return 0  
        if brains >= 2 or shotguns == 2:
            return brains 

def simulate_game():
    scores = {'Bot A': 0, 'Bot B': 0}
    players = list(scores.keys())
    turn = 0

    print("\nGame Start!\n")
    while max(scores.values()) < 13:
        p = players[turn % 2]
        gained = zombie_bot_turn(p)
        scores[p] += gained
        print(f"{p}: +{gained} -> {scores[p]}")
        turn += 1

    winner = max(scores, key=scores.get)
    print(f"\n🏆 {winner} wins with {scores[winner]} brains!")

if __name__ == "__main__":
    simulate_game()
