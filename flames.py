you = "" # Enter name
them = "" # Enter name
code = "FLAMES"

val = {
    'F': "Just friends :(",
    'L': "Congrats... lovveeee",
    'A': "Affection.. bruhhh",
    'M': "Marriage... Invite me though",
    'E': "Stay away.. She is an enemy",
    'S': "Sweet Home Alabama"
}

def scrap(letter):
    return val[letter]

def flames(you, them):
    you = you.lower().replace(' ', '')
    them = them.lower().replace(' ', '')

    for ch in you[:]:
        if ch in them:
            you = you.replace(ch, '', 1)
            them = them.replace(ch, '', 1)

    name_len = len(you + them)
    
    flames_list = list(code)
    idx = 0

    while len(flames_list) > 1:
        idx = (idx + name_len - 1) % len(flames_list)
        flames_list.pop(idx)

    return val[flames_list[0]]

print(flames(you, them))