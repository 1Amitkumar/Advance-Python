from enum import Enum


class LightWarning(Enum):
    RED = 1                      # enum definition
    YELLOW = 2
    GREEN = 3


print(LightWarning)


LightWarning = Enum('LightWarning', ["RED", "YELLOW", "GREEN"])            # functional interface
print(LightWarning)


print()
print(LightWarning.RED)
print(LightWarning.RED.name)
print(LightWarning.RED == 1)                                 # comparing values
print(LightWarning.RED is LightWarning.GREEN)

crossing = LightWarning.RED
print(crossing is LightWarning.RED)

print()
for tl in LightWarning:                     # iterating items
    print(tl)

