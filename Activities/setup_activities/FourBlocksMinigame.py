import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

# Connect to Minecraft
mc = minecraft.Minecraft.create()

colors = {
    "blue": block.Block(35, 9),
    "red": block.Block(35, 14),
    "yellow": block.Block(35, 4),
    "green": block.Block(35, 13),
    "purple": block.Block(35, 10)
}

block_positions = {
    0: (0, 7, 18),  # 1st block
    1: (0, 6, 18),  # 2nd block
    2: (0, 5, 18),  # 3rd block
    3: (0, 4, 18)   # 4th block
}

class FourBlocksMinigame:
    def __init__(self):
        self.sequence = []
        self.rules = self.create_rules()

    def generate_sequence(self):
        """Generates a random sequence of 4 blocks"""
        available_colors = list(colors.keys())
        self.sequence = [random.choice(available_colors) for _ in range(4)]
        elem1 = colors[self.sequence[0]]
        elem2 = colors[self.sequence[1]]
        elem3 = colors[self.sequence[2]]
        elem4 = colors[self.sequence[3]]
        # place 1st random block
        mc.setBlock(0, 7, 18, elem1)
        # place 2nd random block
        mc.setBlock(0, 6, 18, elem2)
        # place 3rd random block
        mc.setBlock(0, 5, 18, elem3)
        # place 4th random block
        mc.setBlock(0, 4, 18, elem4)
        return self.sequence
    
    def create_rules(self):
        """Creates the rulebook to determine which block should be hit"""
        return [
            # Rule 1: If there are exactly 3 blocks of the same color, hit the first one
            {
                "condition": lambda seq: any(seq.count(color) == 3 for color in set(seq)),
                "action": "Hit the first block",
                "block_to_hit": 0
            },
            
            # Rule 2: If the first and second blocks are the same color and the last one is not green
            {
                "condition": lambda seq: seq[0] == seq[1] and seq[3] != "green",
                "action": "Hit the second block",
                "block_to_hit": 1
            },
            
            # Rule 3: If there are exactly 2 purple blocks, hit the last one
            {
                "condition": lambda seq: seq.count("purple") == 2,
                "action": "Hit the last block",
                "block_to_hit": 3
            },
            
            # Rule 4: If all blocks are different colors, hit the third one
            {
                "condition": lambda seq: len(set(seq)) == 4,
                "action": "Hit the third block",
                "block_to_hit": 2
            },
            
            # Rule 5: If the second block is blue and the third is red, hit the first one
            {
                "condition": lambda seq: seq[1] == "blue" and seq[2] == "red",
                "action": "Hit the first block",
                "block_to_hit": 0
            },
            
            # Rule 6: If there are more yellow blocks than green ones, hit the fourth
            {
                "condition": lambda seq: seq.count("yellow") > seq.count("green"),
                "action": "Hit the fourth block",
                "block_to_hit": 3
            },
            
            # Rule 7: If there are no purple blocks, hit the second
            {
                "condition": lambda seq: "purple" not in seq,
                "action": "Hit the second block",
                "block_to_hit": 1
            },
            
            # Rule 8: If the first and last blocks are the same color, hit the third
            {
                "condition": lambda seq: seq[0] == seq[3],
                "action": "Hit the third block",
                "block_to_hit": 2
            },
            
            # Default rule: If no other rule applies, hit the fourth block
            {
                "condition": lambda seq: True,
                "action": "Hit the fourth block (default rule)",
                "block_to_hit": 3
            }
        ]
    
    def determine_block_to_hit(self, sequence=None):
        """Determines which block should be hit according to the rules"""
        if sequence is None:
            sequence = self.sequence
        
        # Evaluate the rules in order
        for rule in self.rules:
            if rule["condition"](sequence):
                return {
                    "block": rule["block_to_hit"],
                    "action": rule["action"],
                    "applied_rule": rule["action"]
                }
        

        return {
            "block": 3,
            "action": "Hit the fourth block (fallback)",
            "applied_rule": "Fallback"
        }

    def block_events(self):
        block_events = mc.events.pollBlockHits()

        for e in block_events:
            pos = e.pos
            return pos
    
    def verify_hit(self, sequence=None):
        """Checks if the player hit the correct block"""
        if sequence is None:
            sequence = self.sequence

        result = self.determine_block_to_hit(sequence)
        block_pos = block_positions[result["block"]]
        hit_pos = self.block_events()
        if hit_pos is None:
            return False
        if block_pos[0] == hit_pos.x and block_pos[1] == hit_pos.y and block_pos[2] == hit_pos.z:
            return True
        else: 
            return ""
    
    def generate_challenge(self):
        game = FourBlocksMinigame()
        sequence = game.generate_sequence()
        return game, sequence

    def start_game(self, game, sequence):
        mc.postToChat("Colpeja el bloc correcte per obrir la porta!")
        mc.postToChat("Nomes hi ha una oportunitat!")
        mc.postToChat("Bona sort!")
        completed = False

        while not completed:
            result = game.verify_hit(sequence)

            if result:
                completed = True
                mc.postToChat("Perfecte! Has encertat el bloc correcte.")
                time.sleep(1)
                mc.setBlock(3, 4, 20, block.AIR.id)
                mc.setBlock(3, 5, 20, block.AIR.id)
                mc.postToChat("S'ha obert la porta!")
                time.sleep(1)
                mc.postToChat("Segueix endavant per escapar del laberint.")
            elif result == "":
                mc.postToChat("T'has equivocat de bloc!")
                mc.player.setTilePos(1, 4, 1)
                break
            
            time.sleep(0.1)