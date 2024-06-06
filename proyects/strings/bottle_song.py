song = [
    "Ten green bottles hanging on the wall,",
    "Ten green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be nine green bottles hanging on the wall.",
    "",
    "Nine green bottles hanging on the wall,",
    "Nine green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be eight green bottles hanging on the wall.",
    "",
    "Eight green bottles hanging on the wall,",
    "Eight green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be seven green bottles hanging on the wall.",
    "",
    "Seven green bottles hanging on the wall,",
    "Seven green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be six green bottles hanging on the wall.",
    "",
    "Six green bottles hanging on the wall,",
    "Six green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be five green bottles hanging on the wall.",
    "",
    "Five green bottles hanging on the wall,",
    "Five green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be four green bottles hanging on the wall.",
    "",
    "Four green bottles hanging on the wall,",
    "Four green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be three green bottles hanging on the wall.",
    "",
    "Three green bottles hanging on the wall,",
    "Three green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be two green bottles hanging on the wall.",
    "",
    "Two green bottles hanging on the wall,",
    "Two green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be one green bottle hanging on the wall.",
    "",
    "One green bottle hanging on the wall,",
    "One green bottle hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be no green bottles hanging on the wall.",
]
def recite(start, take=1):
    song_string = '\n'.join(song)
    strofas = song_string.split('\n\n')
    if take == 1:
        result = [strofas[10-start]]
        return [line for line in result[0].split('\n')]
    elif take > 1:
        result = strofas[10-start:10-start+take]
        lines = []
        for strofa in result:
            lines += strofa.split('\n')
            lines.append('') 
        return lines[:-1]

# expected = [
#     "Three green bottles hanging on the wall,",
#     "Three green bottles hanging on the wall,",
#     "And if one green bottle should accidentally fall,",
#     "There'll be two green bottles hanging on the wall.",
#     "",
#     "Two green bottles hanging on the wall,",
#     "Two green bottles hanging on the wall,",
#     "And if one green bottle should accidentally fall,",
#     "There'll be one green bottle hanging on the wall.",
#     "",
#     "One green bottle hanging on the wall,",
#     "One green bottle hanging on the wall,",
#     "And if one green bottle should accidentally fall,",
#     "There'll be no green bottles hanging on the wall.",
# ]
# print(recite(start=3, take=3)==expected)