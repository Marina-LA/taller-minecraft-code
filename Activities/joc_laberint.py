from setup_activities.FourBlocksMinigame import FourBlocksMinigame
from setup_activities.F1PitstopMinigame import F1PitstopMinigame
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math

mc = minecraft.Minecraft.create()

#####################################################################
#                              REPTE 1                              #
#####################################################################
# QUÈ VOLEM FER?
# Teletransportar el jugador a la posició inicial del laberint
# x = 1, y = 4, z = 1

"""
    AFEGEGIU AQUÍ EL CODI PER TELETRANSPORTAR EL JUGADOR
"""


# 1r Minijoc: Blocks Minigame -> hem de generar el repte i retornar el joc i la seqüència
# 2n Minijoc: F1 Pitstop Minigame -> hem de construir el cotxe. No hem de retornar res.

blocks_minigame = FourBlocksMinigame()
game, sequence = blocks_minigame.generate_challenge()

f1_minigame = F1PitstopMinigame()
f1_minigame.build_car()


#####################################################################
#                            PREGUNTA 1                             #
#####################################################################
# QUÈ VOLEM FER?
# Crear una funció que comprovi els missatges del xat i ens retorni el missatge rebut.

"""
    ENGANXEU AQUÍ EL CODI PER COMPROVAR ELS MISSATGES DEL XAT
"""
    

#####################################################################
#                            PREGUNTA 2                             #
#####################################################################
# QUÈ VOLEM FER?
# Crear una funció que calculi la distància entre dues posicions, i que retorni aquesta distància.

"""
    ENGANXEU AQUÍ EL CODI PER CALCULAR LA DISTÀNCIA ENTRE DUES POSICIONS
"""


#####################################################################
#                            PREGUNTA 3                             #
#####################################################################
# QUÈ VOLEM FER?
# Crear una funció que donada la posició del jugador i la posició de l'objectiu,
# retorni la direcció cardinal (nord, sud, est, oest) de l'objectiu respecte al jugador.
# Completeu la funció següent:

def obtenir_direccio(pos_jugador, pos_objectiu):
    """Determina la direcció cardinal del cofre respecte al jugador"""
    diff_x = pos_objectiu.x - pos_jugador.x
    diff_z = pos_objectiu.z - pos_jugador.z
    
    if abs(diff_x) > abs(diff_z):   # Determinar la direcció principal a l’eix X (est/oest)
        """
            ENGANXEU AQUÍ EL CODI X
        """


    else:   # Determinar la direcció principal a l’eix Z (nord/sud)
        """
            ENGANXEU AQUÍ EL CODI Z
        """

    
    return direccio


# Un preciós poema amb una pista especial
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


#####################################################################
#                            PREGUNTA 4                             #
#####################################################################
def comprovar_xat():
    # obtenim missatge del xat
    missatge = chat_events()

    # QUÈ VOLEM FER?
    # Si el missatge és "start blocks", iniciem el minijoc dels blocs de colors
    # Si el missatge és "start f1", iniciem el minijoc del Pitstop F1
    # Si el missatge és "distancia blocks", calculem i mostrem la distància als blocs de colors
    # Si el missatge és "distancia f1", calculem i mostrem la distància al cotxe de F1
    # Si el missatge és "distancia sortida", calculem i mostrem la distància a la sortida del laberint
    # Si el missatge és "poema", llegim el poema amb la pista especial

    # IMPORTANT:
    # En el fitxer de les opcions només us proporcionem la base del codi.

    if missatge == "start blocks":
        blocks_minigame.start_game(game, sequence)

    elif missatge == "start f1":
        f1_minigame.start_game()

    elif missatge == "distancia blocks":
        """
            Calcula i mostra la distància i la direcció als blocs de colors
        """
        posicio_blocs = minecraft.Vec3(2, 4, 18)

        """
            AFEGEGIU AQUÍ EL CODI PER CALCULAR LA DISTÀNCIA I DIRECCIÓ ALS BLOCS DE COLORS
        """



    elif missatge == "distancia f1":
        """
            Calcula i mostra la distància i la direcció al cotxe de F1
        """
        posicio_f1 = minecraft.Vec3(3, 4, 37)

        """
            AFEGEGIU AQUÍ EL CODI PER CALCULAR LA DISTÀNCIA I DIRECCIÓ AL COTXE DE F1
        """


    elif missatge == "distancia sortida":
        """
            Calcula i mostra la distància i la direcció a la sortida del laberint
        """
        posicio_sortida = minecraft.Vec3(24, 4, 67)

        """
            AFEGEGIU AQUÍ EL CODI PER CALCULAR LA DISTÀNCIA I DIRECCIÓ A LA SORTIDA DEL LABERINT
        """


    elif missatge == "poema":
        llegir_poema()

    elif missatge == "ajuda":
        mc.postToChat("Comandes disponibles:")
        mc.postToChat("- start blocks: Inicia el minijoc dels blocs de colors")
        mc.postToChat("- start f1: Inicia el minijoc del Pitstop F1")
        mc.postToChat("- distancia blocks: Mostra la distància als blocs de colors")
        mc.postToChat("- distancia f1: Mostra la distància al cotxe de F1")
        mc.postToChat("- distancia sortida: Mostra la distància a la sortida del laberint")
        mc.postToChat("- poema: Llegeix un poema amb una pista especial")


#####################################################################
#                      BUCLE PRINCIPAL DEL JOC                      #
#####################################################################
start = True
temps_inici = time.time()
while start:

    comprovar_xat()
    
    pos = mc.player.getTilePos()

#####################################################################
#                              REPTE 2                              #
#####################################################################
# QUÈ VOLEM FER?
# Volem definir una condició per a desbloquejar l'accés a la següent zona del laberint
# quan el jugador arribi a una posició concreta.
#   Si el jugador està a la posició (7, 4, 67):
#       - Treure els blocs que tanquen el pas (11, 5, 67) i (11, 4, 67) -> block.AIR.id
#   Si el jugador està a la posició (28, 3, 67):
#       - Acabar el joc (start = False)

    """
        AFEGEGIU AQUÍ EL CODI
    """ 
        
    time.sleep(1)

temps_final = time.time()
total_temps = temps_final - temps_inici
mc.postToChat("Felicitats! Has escapat del laberint!")
mc.postToChat(f"Temps total: {int(total_temps/60)} minuts i {int(total_temps%60)} segons")