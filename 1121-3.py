#1121-3
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
while True:
    x,y,z = mc.player.getPos()
    mc.setBlock(x,y,z,38)
    time.sleep(1)