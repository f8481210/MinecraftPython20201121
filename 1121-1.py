#1121-1
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
long = 5  #長
width = 10 #寬
length = 9 #高
blockid = 7
air = 0

mc.setBlocks(x,y,z,x+long,y+length,
             z+width,blockid)
mc.setBlocks(x+1,y+1,z+1,x+long-1,
             y+length-1,z+width-1,air)
