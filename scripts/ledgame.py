#daniella 1/20
# Turns on led light on if favcolor is blue and age > 13

from include.rcc_library import Raft

myraft = Raft()

favcolor = "blue"
age = 24

if favcolor == "blue" and age > 13:
    myraft.led_on()