from setup_activities.FourBlocksMinigame import FourBlocksMinigame
from setup_activities.F1PitstopMinigame import F1PitstopMinigame
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math

mc = minecraft.Minecraft.create()

# 1. Teletransporta el jugador a la zona de jocs
mc.player.setTilePos(1, 4, 1)


# 2. Minijoc blocs de colors
blocks_minigame = FourBlocksMinigame()
game, sequence = blocks_minigame.generate_challenge()
# blocks_minigame.start_game(game, sequence)

# 3. Minijoc Pitstop F1
f1_minigame = F1PitstopMinigame()
f1_minigame.build_car()
# f1_minigame.start_game()


def chat_events():
    chat_events = mc.events.pollChatPosts()

    for e in chat_events:
        return e.message
    

def bloc_trepitjat():
    pos_jugador = mc.player.getTilePos()
    return mc.getBlock(pos_jugador.x, pos_jugador.y-2, pos_jugador.z)
    

def calcular_distancia(pos1, pos2):
    distancia = math.sqrt((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2 + (pos1.z - pos2.z) ** 2)
    return distancia

def obtener_direccion(pos_jugador, pos_cofre):
    """Determina la dirección cardinal del cofre respecto al jugador"""
    diff_x = pos_cofre.x - pos_jugador.x
    diff_z = pos_cofre.z - pos_jugador.z
    
    # Determinar dirección principal en eje X (este/oeste)
    if abs(diff_x) > abs(diff_z):
        if diff_x > 0:
            direccion_x = "este"
        else:
            direccion_x = "oeste"
    # Determinar dirección principal en eje Z (norte/sur)
    else:
        if diff_z > 0:
            direccion_x = "sur"  # En Minecraft, Z positivo es sur
        else:
            direccion_x = "norte"  # En Minecraft, Z negativo es norte
    
    return direccion_x


def calcular_distancia_cofres():
    posicio_jugador = mc.player.getTilePos()
    posicio_cofre1 = minecraft.Vec3(11, 4, 19)
    posicio_cofre2 = minecraft.Vec3(24, 4, 34)
    posicio_cofre3 = minecraft.Vec3(7, 4, 47)
    posicio_cofre4 = minecraft.Vec3(24, 4, 43)
    distancia1 = calcular_distancia(posicio_jugador, posicio_cofre1)
    distancia2 = calcular_distancia(posicio_jugador, posicio_cofre2)
    distancia3 = calcular_distancia(posicio_jugador, posicio_cofre3)
    distancia4 = calcular_distancia(posicio_jugador, posicio_cofre4)
    
    # Obtener direcciones
    direccion1 = obtener_direccion(posicio_jugador, posicio_cofre1)
    direccion2 = obtener_direccion(posicio_jugador, posicio_cofre2)
    direccion3 = obtener_direccion(posicio_jugador, posicio_cofre3)
    direccion4 = obtener_direccion(posicio_jugador, posicio_cofre4)
    
    mc.postToChat("Distancies als cofres:")
    time.sleep(1)
    mc.postToChat("Recorda, son posicions aproximades!")
    time.sleep(1)
    mc.postToChat("--------------------------------------------------")
    mc.postToChat(f"Cofre 1: {int(distancia1)} blocs al {direccion1}")
    mc.postToChat(f"Cofre 2: {int(distancia2)} blocs al {direccion2}")
    mc.postToChat(f"Cofre 3: {int(distancia3)} blocs al {direccion3}")
    mc.postToChat(f"Cofre 4: {int(distancia4)} blocs al {direccion4}")
    mc.postToChat("--------------------------------------------------")

def llegir_poema():
        mc.postToChat("Dins el laberint dels colors brillants,")
        time.sleep(1)
        mc.postToChat("molts camins et volen trair.")
        time.sleep(1)
        mc.postToChat("Però l'herba parla en tons elegants,")
        time.sleep(1)
        mc.postToChat("i et diu per on has de seguir.")
        time.sleep(1)
        mc.postToChat("Trepitja el verd amb pas sincer,")
        time.sleep(1)
        mc.postToChat("i el secret s'obrira davant teu, viatger.")

def comprovar_xat():
    missatge = chat_events()
    if missatge == "start blocks":
        blocks_minigame.start_game(game, sequence)
    elif missatge == "start f1":
        f1_minigame.start_game()
    elif missatge == "distancia blocks":
        posicio_jugador = mc.player.getTilePos()
        posicio_blocs = minecraft.Vec3(2, 4, 18)
        distancia = calcular_distancia(posicio_jugador, posicio_blocs)
        mc.postToChat(f"Distància als blocs de colors: {int(distancia)} blocs")
    elif missatge == "distancia f1":
        posicio_jugador = mc.player.getTilePos()
        posicio_f1 = minecraft.Vec3(3, 4, 37)
        distancia = calcular_distancia(posicio_jugador, posicio_f1)
        mc.postToChat(f"Distància al cotxe de F1: {int(distancia)} blocs")
    elif missatge == "distancia sortida":
        posicio_jugador = mc.player.getTilePos()
        posicio_sortida = minecraft.Vec3(24, 4, 67)
        distancia = calcular_distancia(posicio_jugador, posicio_sortida)
        mc.postToChat(f"Distància a la sortida del laberint: {int(distancia)} blocs")
    elif missatge == "cofres":
        calcular_distancia_cofres()
    elif missatge == "poema":
        llegir_poema()
    elif missatge == "ajuda":
        mc.postToChat("Comandes disponibles:")
        mc.postToChat("- start blocks: Inicia el minijoc dels blocs de colors")
        mc.postToChat("- start f1: Inicia el minijoc del Pitstop F1")
        mc.postToChat("- distancia blocks: Mostra la distància als blocs de colors")
        mc.postToChat("- distancia f1: Mostra la distància al cotxe de F1")
        mc.postToChat("- distancia sortida: Mostra la distància a la sortida del laberint")
        mc.postToChat("- cofres: Mostra les distàncies als cofres amagats")
        mc.postToChat("- poema: Escolta un poema amb una pista especial")

start = True
temps_inici = time.time()
while start:
    comprovar_xat()
    
    pos = mc.player.getTilePos()
    if pos.x == 7 and pos.y == 3 and pos.z == 67:
        mc.setBlock(11, 5, 67, block.AIR.id)
        mc.setBlock(11, 4, 67, block.AIR.id)
    elif pos.x == 28 and pos.y == 3 and pos.z == 67:
        start = False
        
    time.sleep(1)

temps_final = time.time()
total_temps = temps_final - temps_inici
mc.postToChat("Felicitats! Has escapat del laberint!")
mc.postToChat(f"Temps total: {int(total_temps/60)} minuts i {int(total_temps%60)} segons")