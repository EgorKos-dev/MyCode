from monsters import Monster

zombie = Monster("Richard Stevenson the Third", 50, "May I perchance acquire some brains?")

globber = Monster("Globbler the Insatiable", 120, "Gloop.")

xorg = Monster("Xorg the Unfathomable", 200, "I am xorg the unfathomable")

print({zombie.get_name()})
print(f"Richard Stevenson the Third: {zombie.get_speech()}")

zombie.set_health(70)
zombie.take_damage(20)
print((zombie.get_health()))

print({globber.get_name()})
print(f"Globbler the Insatiable: {globber.get_speech()}")

globber.take_damage(50)
print((globber.get_health()))

print({xorg.get_name()})
print(f"Xorg the Unfathomable: {xorg.get_speech()}")

xorg.take_damage(190)
print((xorg.get_health()))