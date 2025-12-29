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
    "green": block.Block(35, 13)
}

wheels = {
    "front_left": (8, 4, 41), # blue
    "front_right": (8, 4, 39), # red
    "back_left": (14, 4, 41),  # yellow
    "back_right": (14, 4, 39)  # green
}


class F1PitstopMinigame:

    def __init__(self):
        self.car_color = random.choice(list(colors.values()))


    def build_car(self):
            mc.setBlock(12, 5, 40, self.car_color)
            mc.setBlock(12, 4, 41, self.car_color)
            mc.setBlock(11, 4, 41, self.car_color)
            mc.setBlock(10, 4, 41, self.car_color)
            mc.setBlock(12, 4, 39, self.car_color)
            mc.setBlock(11, 4, 39, self.car_color)
            mc.setBlock(10, 4, 39, self.car_color) 
            mc.setBlock(9, 4, 40, self.car_color)
            mc.setBlock(8, 4, 40, self.car_color)
            mc.setBlock(7, 4, 40, self.car_color)


    def block_events(self):
        block_events = mc.events.pollBlockHits()

        for e in block_events:
            pos = e.pos
            return pos


    def start_game(self):
        mc.postToChat("Colpeja la roda correcta!")

        hitted = False
        
        while not hitted:    

            hitted_block_pos = self.block_events()
            
            if hitted_block_pos is None:
                time.sleep(0.1)
                continue
            

            if self.car_color == colors["blue"]:
                if (hitted_block_pos.x == wheels["front_left"][0] and
                    hitted_block_pos.y == wheels["front_left"][1] and
                    hitted_block_pos.z == wheels["front_left"][2]):
                    hitted = True
            elif self.car_color == colors["red"]:
                if (hitted_block_pos.x == wheels["front_right"][0] and
                    hitted_block_pos.y == wheels["front_right"][1] and
                    hitted_block_pos.z == wheels["front_right"][2]):
                    hitted = True
            elif self.car_color == colors["yellow"]:
                if (hitted_block_pos.x == wheels["back_left"][0] and
                    hitted_block_pos.y == wheels["back_left"][1] and
                    hitted_block_pos.z == wheels["back_left"][2]):
                    hitted = True
            elif self.car_color == colors["green"]:
                if (hitted_block_pos.x == wheels["back_right"][0] and
                    hitted_block_pos.y == wheels["back_right"][1] and
                    hitted_block_pos.z == wheels["back_right"][2]):
                    hitted = True


        mc.postToChat("Perfecte! Has canviat la roda correcta.")
        time.sleep(1)
        mc.setBlock(3, 4, 43, block.AIR.id)
        mc.setBlock(3, 5, 43, block.AIR.id)
        mc.postToChat("S'ha obert la porta!")
        time.sleep(1)
        mc.postToChat("Segueix endavant per escapar del laberint.")
        return True
