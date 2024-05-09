import re
list_straight = ["2345A","23456","34567","45678","56789","678910","78910J","8910JQ","910JQK","10AJQK","aAJQK","23AQK","234AK"]

def best_hands(hands):
    #filtrado = re.sub(r'[^JQK0-9]', '', *hands)
    #contando = {'10' if carta == 'J' or carta == 'Q' or carta == 'K' else carta: filtrado.count(carta) for carta in filtrado}
    result = []
    max_card_value = None
    max_card_hands = []
    
    if len(hands) == 1:
        return [hands[0]]
    for hand in hands:
        dict_color = {}
        dict_hand = {}
        filtr_color = re.findall(r'[SCDH]', hand.replace(" ", ""))
        dict_color = {letra: filtr_color.count(letra) for letra in filtr_color}
        filtrado = re.sub(r'[^JQKA10-9DSHC]', '', hand)
        for carta in filtrado:
            if carta.isdigit():
                if carta == '1' and hand[hand.index(carta)+1] == '0':
                    carta = '10'
                elif carta == '0':
                    continue
                if carta not in dict_hand:
                    dict_hand[carta] = 1
                else:
                    dict_hand[carta] += 1
            else:
                if carta in ['J', 'Q', 'K' ,'A']:
                    if carta not in dict_hand:
                        dict_hand[carta] = 1
                    else:
                        dict_hand[carta] += 1

        dict_hand = dict(sorted(dict_hand.items(), key=lambda x: (int(x[0]), x[0]) if x[0].isdigit() else (float('inf'), x[0])))
        result.append(dict_hand)
        
    for i in range(len(result) - 1):
        #print(result[i].keys())
        if list(result[i].keys()) == list(result[i + 1].keys()):
            max_card_hands.append(hands[i])
            max_card_hands.append(hands[i+1])
        elif list(result[i].keys()) > list(result[i + 1].keys()):
            max_card_hands.append(hands[i])
        elif list(result[i].keys()) < list(result[i + 1].keys()) and len(result)<=2:
            max_card_hands.append(hands[i])
        elif list(result[i].keys()) < list(result[i + 1].keys()) and len(result)>2:
            max_card_hands.pop(i-1)

    
    return max_card_hands


# a = best_hands(["3S 5H 6S 8D 7H", "2S 5D 6D 8C 7S"])
# #print(a == ["3S 5H 6S 8D 7H"], a)
# b = best_hands(["4D 5S 6S 8D 3C","2S 4C 7S 9H 10H","3S 4S 5D 6H JH","3H 4H 5C 6C JD",])
# #print(b==["3S 4S 5D 6H JH", "3H 4H 5C 6C JD"], b)
# c = best_hands(["3S 5H 6S 8D 7H", "2S 5D 6D 8C 7S"])
# #print(c==["3S 5H 6S 8D 7H"], c)
# d = best_hands(["2S 5H 6S 8D 7H", "3S 4D 6D 8C 7S"])
# #print(d==["2S 5H 6S 8D 7H"], d)
