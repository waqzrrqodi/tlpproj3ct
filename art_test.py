not_art = set(dir())

import art

all_art = set(dir(art)) - not_art

print(f"Du kan välja mellan {all_art}")

for i in all_art:
    art[i] = art[i]
    print(art[i])