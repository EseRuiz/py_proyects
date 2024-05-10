import re
list_straight = ["2345A","23456","34567","45678","56789","678910","78910J","8910JQ","910JKQ","10AJKQ","2AJKQ","234AK"]

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

    if all(len(d) == 5 for d in result): #high card vd high card, straight not yet
        hand_strs = [''.join(hand_dict.keys()) for hand_dict in result]
        for i in range(len(result) - 1):
            if list(result[i].keys()) == list(result[i + 1].keys()) and hand_strs[i] not in list_straight and hand_strs[i+1] not in list_straight :
                max_card_hands.append(hands[i])
                max_card_hands.append(hands[i+1])
            elif list(result[i].keys()) > list(result[i + 1].keys()) and hand_strs[i] not in list_straight and hand_strs[i+1] not in list_straight :
                max_card_hands.append(hands[i])
            elif list(result[i].keys()) < list(result[i + 1].keys()) and len(result)<=2 and hand_strs[i] not in list_straight and hand_strs[i+1] not in list_straight :
                max_card_hands.append(hands[i])
            elif list(result[i].keys()) < list(result[i + 1].keys()) and len(result)>2:
                max_card_hands.pop(i-1)
        if hand_strs[0] > hand_strs[1] and hand_strs[0] in list_straight:#straight max
            max_card_hands.append(hands[0])
        if hand_strs[0] < hand_strs[1] and hand_strs[0] in list_straight:
            max_card_hands.append(hands[1])

    if all(len(d) == 4 for d in result):#one pair in both hands
        for i in range(len(result) - 1):#para prueba de dos manos no se nesecita el for solo 0 y 1
            pair1 = [k for k, v in result[i].items() if v == 2]
            pair2 = [k for k, v in result[i+1].items() if v == 2]
            if int(pair1[0]) > int(pair2[0]) :
                max_card_hands.append(hands[i])
            elif int(pair1[0]) < int(pair2[0]) :
                max_card_hands.append(hands[i+1])
            elif int(pair1[0]) == int(pair2[0]) :
                if max(list(result[0].keys())) > max(list(result[1].keys())):
                    max_card_hands.append(hands[0])
                elif max(list(result[0].keys())) < max(list(result[1].keys())):
                    max_card_hands.append(hands[1])


    if any(len(d) == 4 for d in result):#one hand pair vs high card
        for i in range(len(result) - 1):
            if len(list(result[i].keys()))==5 and len(list(result[i+1].keys()))==4:
                max_card_hands.append(hands[i+1])
            if len(list(result[i].keys()))==4 and len(list(result[i+1].keys()))==5:
                max_card_hands.append(hands[i])
        pairs1 = [k for k, v in result[0].items() if v == 2]#two pair in one hands vs one pair
        pairs2 = [k for k, v in result[1].items() if v == 2]
        if len(pairs1)==2 and len(pairs2)==1:
            max_card_hands.append(hands[0])
        elif len(pairs1)==1 and len(pairs2)==2:
            max_card_hands.append(hands[1])    


    if all(len(d) == 3 for d in result):#two pair in both hands
        pairs1 = [k for k, v in result[0].items() if v == 2]
        pairs2 = [k for k, v in result[1].items() if v == 2]
        three1 = [k for k, v in result[0].items() if v == 3]
        three2 = [k for k, v in result[1].items() if v == 3]
        if len(pairs1)==2 and len(pairs2)==2:
            if pairs1 == pairs2:
                no_pair1 = [k for k, v in result[0].items() if v == 1]
                no_pair2 = [k for k, v in result[1].items() if v != 2]
                if no_pair1 > no_pair2:
                    max_card_hands.append(hands[0])
                elif no_pair1 < no_pair2:
                    max_card_hands.append(hands[1])
            if max(pairs1) == max(pairs2):
                if min(pairs1) > min(pairs2):
                    max_card_hands.append(hands[0])
                elif min(pairs1) < min(pairs2):
                    max_card_hands.append(hands[1])
            if max(pairs1) > max(pairs2):
                max_card_hands.append(hands[0])
            elif max(pairs1) < max(pairs2):
                max_card_hands.append(hands[1])
        if len(three1)==1 and len(pairs2)==2:
            max_card_hands.append(hands[0])
        if len(pairs1)==2 and len(three2)==1:
            max_card_hands.append(hands[1]) 
        if len(three1)==1 and len(three2)==1:
            if max(three1) == max(three2):
                nothree1 = [k for k, v in result[0].items() if v == 1]
                nothree2 = [k for k, v in result[1].items() if v == 1]
                if max(nothree1) > max(nothree2):
                    max_card_hands.append(hands[0]) 
                if max(nothree1) < max(nothree2):
                    max_card_hands.append(hands[1])
            if max(three1) > max(three2):
                max_card_hands.append(hands[0]) 
            if max(three1) < max(three2):
                max_card_hands.append(hands[1]) 
    
    if any(len(d) == 3 for d in result):#straight beats three
        hand_strs = [''.join(hand_dict.keys()) for hand_dict in result]
        if hand_strs[0] in list_straight and hand_strs[1] not in list_straight:
            max_card_hands.append(hands[0])
        if hand_strs[0] not in list_straight and hand_strs[1] in list_straight:
            max_card_hands.append(hands[1])
    return max_card_hands


# a = best_hands(["3S 5H 6S 8D 7H", "2S 5D 6D 8C 7S"])
# print(a == ["3S 5H 6S 8D 7H"], a)
# b = best_hands(["4D 5S 6S 8D 3C","2S 4C 7S 9H 10H","3S 4S 5D 6H JH","3H 4H 5C 6C JD",])
# print(b==["3S 4S 5D 6H JH", "3H 4H 5C 6C JD"], b)
# c = best_hands(["3S 5H 6S 8D 7H", "2S 5D 6D 8C 7S"])
# print(c==["3S 5H 6S 8D 7H"], c)
# d = best_hands(["2S 5H 6S 8D 7H", "3S 4D 6D 8C 7S"])
# print(d==["2S 5H 6S 8D 7H"], d)
# e = best_hands(["4S 5H 6C 8D KH", "2S 4H 6S 4D JH"])
# print(e==["2S 4H 6S 4D JH"],e)
# f = best_hands(["4S 2H 6S 2D JH", "2S 4H 6C 4D JD"])
# print(f == ["2S 4H 6C 4D JD"], f)
# g = best_hands(["4H 4S AH JC 3D", "4C 4D AS 5D 6C"])
# print(g==["4H 4S AH JC 3D"],g)
# h = best_hands(["2S 8H 6S 8D JH", "4S 5H 4C 8C 5C"])
# print(h==["4S 5H 4C 8C 5C"],h)
# i = best_hands(["2S 8H 2D 8D 3H", "4S 5H 4C 8S 5D"])
# print(i==["2S 8H 2D 8D 3H"],i)
# j = best_hands(["2S QS 2C QD JH", "JD QH JS 8D QC"])
# print(j==["JD QH JS 8D QC"],j)
# k = best_hands(["JD QH JS 8D QC", "JS QS JC 2D QD"])
# print(k==["JD QH JS 8D QC"],k)
# l = best_hands(["6S 6H 3S 3H AS", "7H 7S 2H 2S AC"])
# print(l==["7H 7S 2H 2S AC"],l)
# m = best_hands(["5C 2S 5S 4H 4C", "6S 2S 6H 7C 2C"])
# print(m == ["6S 2S 6H 7C 2C"], m)
# n = best_hands(["2S 8H 2H 8D JH", "4S 5H 4C 8S 4H"])
# print(n==["4S 5H 4C 8S 4H"],n)
# o = best_hands(["2S 2H 2C 8D JH", "4S AH AS 8C AD"])
# print(o == ["4S AH AS 8C AD"], o)
# p = best_hands(["5S AH AS 7C AD", "4S AH AS 8C AD"])
# print(p == ["4S AH AS 8C AD"], p)
# q = best_hands(["4S 5H 4C 8D 4H", "3S 4D 2S 6D 5C"])
# print(q == ["3S 4D 2S 6D 5C"] , q)
# r = best_hands(["4S 5H 4C 8D 4H", "10D JH QS KD AC"])
# print(r == ["10D JH QS KD AC"],r)
# s = best_hands(["4S 5H 4C 8D 4H", "4D AH 3S 2D 5C"])
# print(s == ["4D AH 3S 2D 5C"],s)
# t = best_hands(["2C 3D 7H 5H 2S", "QS KH AC 2D 3S"])#one pair gain to bad straight
# print(t == ["2C 3D 7H 5H 2S"], t)
# u = best_hands(["4S 6C 7S 8D 5H", "5S 7H 8S 9D 6H"])
# print(u == ["5S 7H 8S 9D 6H"], u)