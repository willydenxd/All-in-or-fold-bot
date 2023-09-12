import pyautogui
import poker
import cv2
import time
suit = ['s','h','d','c']
Tsuit = ['ss','hh','dd','cc']
rank_left = ['A','K','Q','J','T','9','8','7','6','5','4','3',]
rank_right = ['K','Q','J','T','9','8','7','6','5','4','3','2']
pair = "22,33,44,55,66,77,88,99,TT,JJ,QQ,KK,AA,"
AXs = "AKs,AQs,AJs,ATs,A9s,A8s,A7s,A6s,A5s,A4s,A3s,A2s,"
AXo = "AKo,AQo,AJo,ATo,A9o,A8o,A7o,A6o,A5o,A4o,A3o,A2o,"
KXs = "KQs,KJs,KTs,K9s,K8s,K7s,K6s,K5s,K4s,K3s,K2s,"
KXo = "KQo,KJo,KTo,K9o,K8o,K7o,K6o,K5o,K4o,K3o,K2o,"
QXs = "QJs,QTs,Q9s,Q8s,Q7s,Q6s,Q5s,Q4s,Q3s,Q2s,"
QXo = "QJo,QTo,Q9o,Q8o,Q7o,Q6o,Q5o,Q4o,Q3o,Q2o,"
JXs = "JTs,J9s,J8s,J7s,J6s,J5s,J4s,J3s,J2s,"

four_max_UTG = pair + AXs + "AKo,AQo,AJo,ATo,A9o,A8o,A7o,A6o,A5o,A4o,A3o,KQs,KJs,KTs,K9s,K8s,K7s,K6s,KQo,KJo,KTo,QJs,QTs,Q9s,Q8s,QJo,QTo,JTs,J9s,J8s,JTo,T9s,T8s,98s,97s,87s,76s"
four_max_BTN = pair + AXs + AXo + "KQs,KJs,KTs,K9s,K8s,K7s,K6s,K5s,K4s,K3s,KQo,KJo,KTo,K9o,QJs,QTs,Q9s,Q8s,Q7s,Q6s,QJo,QTo,JTs,J9s,J8s,J7s,JTo,T9s,T8s,T7s,T9o,98s,97s,96s,87s,86s,76s,65s"
four_max_BTNvsUTG = "44,55,66,77,88,99,TT,JJ,QQ,KK,AA,AKs,AQs,AJs,ATs,A9s,A8s,A7s,A6s,A5s,AKo,AQo,AJo,ATo,A9o,A8o,KQs,KJs,KTs,KQo,QJs"
four_max_SB = pair + AXs + AXo + KXs + KXo + QXs + JXs + "QJo,QTo,Q9o,Q8o,Q7o,Q6o,Q5o,JTo,J9o,J8o,J7o,T9s,T8s,T7s,T6s,T5s,T4s,T3s,T9o,T8o,T7o,98s,97s,96s,95s,98o,97o,87s,86s,85s,84s,87o,86o,76s,75s,74s,76o,65s,64s,63s,65o,54s,53s,43s"
four_max_SBvsUTG = "33,44,55,66,77,88,99,TT,JJ,QQ,KK,AA,AKs,AQs,AJs,ATs,A9s,A8s,A7s,A6s,A5s,A4s,AKo,AQo,AJo,ATo,A9o,A8o,A7o,KQs,KJs,KTs,KQo,KJo,QJs"
four_max_SBvsBTN = AXs + "33,44,55,66,77,88,99,TT,JJ,QQ,KK,AA,AKo,AQo,AJo,ATo,A9o,A8o,A7o,A6o,A5o,KQs,KJs,KTs,K9s,KQo,KJo,KTo,QJs,QTs"
four_max_SBvsUTGBTN = "55,66,77,88,99,TT,JJ,QQ,KK,AA,AKs,AQs,AJs,ATs,AKo,AQo,AJo,KQs,KJs,KTs,KQo,QJs,QTs,JTs,"
four_max_BBvsUTG = pair + AXs + "AKo,AQo,AJo,ATo,A9o,A8o,A7o,A6o,A5o,KQs,KJs,KTs,K9s,KQo,KJo,KTo,QJs,QTs,QJo"
four_max_BBvsBTN = pair + AXs + AXo + "KQs,KJs,KTs,K9s,K8s,K7s,KQo,KJo,KTo,K9o,QJs,QTs,Q9s,QJo,QTo,JTs"
four_max_BBvsSB = pair + AXs + AXo + KXs + "KQo,KJo,KTo,K9o,K8o,K7o,K6o,K5o,K4o,QJs,QTs,Q9s,Q8s,Q7s,Q6s,Q5s,QJo,QTo,Q9o,Q8o,JTs,J9s,J8s,JTo,J9o,T9s,T8s"
four_max_BBvsBTNSB = "44,55,66,77,88,99,TT,JJ,QQ,KK,AA,AKs,AQs,AJs,ATs,A9s,A8s,A7s,AKo,AQo,AJo,ATo,A9o,KQs,KJs,KTs,K9s,KQo,KJo,QJs,QTs,Q9s,QJo,JTs,J9s,T9s,98s"
four_max_BBvsUTGBTN = "44,55,66,77,88,99,TT,JJ,QQ,KK,AA,AKo,AQo,AJo,ATo,AKs,AQs,AJs,ATs,A9s,KQs,KJs,KTs,KQo,QJs,QTs,JTs,J9s,T9s"
four_max_BBvsUTGSB = "44,55,66,77,88,99,TT,JJ,QQ,KK,AA,AKo,AQo,AJo,ATo,AKs,AQs,AJs,ATs,A9s,KQs,KJs,KTs,KQo,QJs,QTs,JTs,J9s,T9s"
four_max_BBvsALL = "88,99,TT,JJ,QQ,KK,AA,AQo,AKo,AJs,AQs,AKs"
three_max_BTN = pair + AXs + AXo + "KQs,KJs,KTs,K9s,K8s,K7s,K6s,K5s,K4s,KQo,KJo,KTo,K9o,QJs,QTs,Q9s,Q8s,Q7s,QJo,QTo,JTs,J9s,J8s,J7s,JTo,T9s,T8s,T7s,98s,97s,87s,86s,76s,65s"
three_max_SB = pair + AXs + AXo + KXs + KXo + QXs + JXs + "QJo,QTo,Q9o,Q8o,Q7o,Q6o,Q5o,JTo,J9o,J8o,J7o,T9s,T8s,T7s,T6s,T5s,T4s,T9o,T8o,T7o,98s,97s,96s,95s,98o,97o,87s,86s,85s,87o,76s,75s,74s,76o,65s,64s,54s,53s"
three_max_SBvsBTN = AXs + "33,44,55,66,77,88,99,TT,JJ,QQ,KK,AA,AKo,AQo,AJo,ATo,A9o,A8o,A7o,A6o,A5o,KQs,KJs,KTs,K9s,KQo,KJo,KTo,QJs,QTs,JTs"
three_max_BBvsBTN = pair + AXs + AXo + "KQs,KJs,KTs,K9s,K8s,K7s,K6s,KQo,KJo,KTo,K9o,QJs,QTs,Q9s,QJo,QTo,JTs,J9s"
three_max_BBvsSB = pair + AXs + AXo + KXs + KXo + "QJs,QTs,Q9s,Q8s,Q7s,Q6s,Q5s,Q4s,QJo,QTo,Q9o,Q8o,JTs,J9s,J8s,J7s,JTo,J9o,T9s,T9o,T8s,98s"
three_max_BBvsBTNSB = "33,44,55,66,77,88,99,TT,JJ,QQ,KK,AA,AKs,AQs,AJs,ATs,A9s,A8s,A7s,AKo,AQo,AJo,ATo,A9o,KQs,KJs,KTs,K9s,KQo,KJo,QJs,QTs,Q9s,QJo,JTs,J9s,T9s,98s"
two_max_BB = pair + AXs + AXo + KXs + KXo + "QJs,QTs,Q9s,Q8s,Q7s,Q6s,Q5s,Q4s,QJo,QTo,Q9o,Q8o,JTs,J9s,J8s,J7s,JTo,J9o,T9s,T8s,T9o,98s"
two_max_SB = pair + AXs + AXo + KXs + KXo + QXs + JXs + "QJo,QTo,Q9o,Q8o,Q7o,Q6o,Q5o,JTo,J9o,J8o,J7o,T9s,T8s,T7s,T6s,T5s,T4s,T9o,T8o,T7o,98s,97s,96s,95s,98o,97o,87s,86s,85s,87o,76s,75s,74s,76o,65s,64s,54s,53s"
def find_hand():
    ctr = 0
    global hand
    hand = ''
    left_boo = 0 
    right_boo = 0
    for i in rank_left:
        for j in suit:
            if pyautogui.locateCenterOnScreen("left_"+i+j+".png", region=[335,780,50,60],confidence=0.97) != None:
                print(i+j)
                hand = hand + i + j
                ctr = ctr + 1
                left_boo = 1
    for i in rank_right:
        for j in suit:
            if pyautogui.locateCenterOnScreen("right_"+i+j+".png", region=[370,780,50,60],confidence=0.97) != None:
                print(i+j)
                hand = hand + i + j
                ctr = ctr + 1
                right_boo = 1
    if ctr == 2:
        if hand[0] == hand[2]:
            hand = hand[0] + hand[2]
        elif hand[1] == hand[3]:
            hand = hand[0] + hand[2] + 's'
        elif hand[1] != hand[3]:
            hand = hand[0] + hand[2] + 'o'
    elif ctr == 1 and left_boo == 0:
        hand = "22"
    elif ctr == 1 and right_boo == 0:
        hand = "AA"
    elif ctr == 0:
        hand = ''
    print(hand)
    return hand
    
while True:
    hand = ''
    self_fold_pos = pyautogui.locateCenterOnScreen("self_fold.png",confidence=0.95,region=[188,773,280,190])
    not_holding_pos = pyautogui.locateCenterOnScreen("not_holding.png",confidence=0.95,region=[137,26,140,70])
    self_allin_pos = pyautogui.locateCenterOnScreen("self_allin.png",confidence=0.95,region=[188,773,280,190])
    if not_holding_pos == None and (self_allin_pos == None or self_fold_pos == None):
        left_pos = pyautogui.locateCenterOnScreen("left_hand.png",region=[0,490,150,180],confidence=0.9)
        if left_pos == None:
            time.sleep(0.5)
            left_pos = pyautogui.locateCenterOnScreen("left_hand.png",region=[0,490,150,180],confidence=0.9)
        right_pos = pyautogui.locateCenterOnScreen("right_hand.png",region=[390,500,180,180],confidence=0.9)
        if right_pos == None:
            time.sleep(0.5)
            right_pos = pyautogui.locateCenterOnScreen("right_hand.png",region=[390,500,180,180],confidence=0.9)
        middle_pos = pyautogui.locateCenterOnScreen("middle_hand.png",region=[200,80,160,140],confidence=0.9)
        if middle_pos == None:
            time.sleep(0.5)
            middle_pos = pyautogui.locateCenterOnScreen("middle_hand.png",region=[200,80,160,140],confidence=0.9)

        left_dealer_pos = pyautogui.locateCenterOnScreen("left_dealer.png",region=[0,490,150,180],confidence=0.9)
        right_dealer_pos = pyautogui.locateCenterOnScreen("right_dealer.png",region=[390,500,180,180],confidence=0.9)
        middle_dealer_pos = pyautogui.locateCenterOnScreen("middle_dealer.png",region=[200,80,160,140],confidence=0.9)
        hero_dealer_pos = pyautogui.locateCenterOnScreen("hero_dealer.png",region=[170,700,60,60],confidence=0.9)
        left_allin_pos = pyautogui.locateCenterOnScreen("left_allin.png", confidence=0.95,region=[0,490,150,180])
        right_allin_pos = pyautogui.locateCenterOnScreen("right_allin.png",confidence=0.95,region=[390,500,180,180])
        middle_allin_pos = pyautogui.locateCenterOnScreen("middle_allin.png", confidence=0.95,region=[200,80,160,140])

        left_fold_pos = pyautogui.locateCenterOnScreen("left_fold.png", confidence=0.95,region=[0,490,150,180])
        right_fold_pos = pyautogui.locateCenterOnScreen("right_fold.png", confidence=0.95,region=[390,500,180,180])
        middle_fold_pos = pyautogui.locateCenterOnScreen("middle_fold.png",confidence=0.95,region=[200,80,160,140])
        up_sign_pos = pyautogui.locateCenterOnScreen("up_sign.png",confidence=0.95,region=[140,80,80,30])

        judge = [0,0,0,0] #0=not sitting 1=sit not yet 2=fold 3=allin 
        if left_pos == None and left_fold_pos == None:
            judge[0] = 0
        if middle_pos == None and middle_fold_pos == None:
            judge[1] = 0
        if right_pos == None and right_fold_pos == None:
            judge[2] = 0

        if left_pos != None and left_allin_pos == None:
            judge[0] = 1
        if middle_pos != None and middle_allin_pos == None:
            judge[1] = 1
        if right_pos != None and right_allin_pos == None:
            judge[2] = 1

        if left_fold_pos != None:
            judge[0] = 2
        if middle_fold_pos != None:
            judge[1] = 2
        if right_fold_pos != None:
            judge[2] = 2

        if left_allin_pos != None:
            judge[0] = 3
        if middle_allin_pos != None:
            judge[1] = 3
        if right_allin_pos != None:
            judge[2] = 3

        if hero_dealer_pos != None:
            judge[3] = 0
        elif left_dealer_pos != None:
            judge[3] = 1
        elif middle_dealer_pos != None:
            judge[3] = 2
        elif right_dealer_pos != None:
            judge[3] = 3

        if judge[0] == 0:
            if judge[1] == 0:
                if judge[2] == 1:
                    if judge[3] == 0:
                        find_hand()
                        if hand != '' and up_sign_pos == None:
                            if two_max_SB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("2max SB")
                elif judge[2] == 3:
                    if judge[3] == 3:
                        find_hand()
                        if hand != '':
                            if two_max_BB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("2max BB vs SB all in")
            elif judge[1] == 1:
                if judge[2] == 0:
                    if judge[3] == 0:
                        find_hand()
                        if hand != '' and up_sign_pos == None:
                            if two_max_SB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("2max SB")
                elif judge[2] == 1:
                    if judge[3] == 0:
                        find_hand()
                        if hand != '':
                            if three_max_BTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max BTN")
                elif judge[2] == 2:
                    if judge[3] == 3:
                        find_hand()
                        if hand != '':
                            if three_max_SB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max SB")
                elif judge[2] == 3:
                    if judge[3] == 3:
                       find_hand()
                       if hand != '':
                            if three_max_SBvsBTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max SB vs BTN all in")
            elif judge[1] == 2:
                if judge[2] == 3: 
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if three_max_BBvsSB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max BB vs SB all in")
            elif judge[1] == 3:
                if judge[2] == 0:
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if two_max_BB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("2max BB")
                elif judge[2] == 2:
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if three_max_BBvsBTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max BB vs BTN all in")
                elif judge[2] == 3:
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if three_max_BBvsBTNSB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max BB vs BTN SB all in")
        elif judge[0] == 1:
            if judge[1] == 0:
                if judge[2] == 0:
                    if judge[3] == 0:
                        find_hand()
                        if hand != '' and up_sign_pos == None:
                            if two_max_SB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("2max SB")
                elif judge[2] == 1:
                    if judge[3] == 0:
                        find_hand()
                        if hand != '':
                            if three_max_BTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max BTN")
                elif judge[2] == 2:
                    if judge[3] == 3:
                        find_hand()
                        if hand != '':
                            if three_max_SB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max SB")
                elif judge[2] == 3:
                    if judge[3] == 3:
                        find_hand()
                        if hand != '':
                            if three_max_SBvsBTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max SB vs BTN all in")
            elif judge[1] == 1:
                if judge[2] == 0:
                    if judge[3] == 0:
                        find_hand()
                        if hand != '':
                            if three_max_BTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max BTN")
                elif judge[2] == 1:
                    if judge[3] == 1:
                        find_hand()
                        if hand != '':
                            if four_max_UTG.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max UTG")
                elif judge[2] == 2:
                    if judge[3] == 0:
                        find_hand()
                        if hand != '':
                            if four_max_BTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max BTN")
                elif judge[2] == 3:
                    if judge[3] == 0:
                        find_hand()
                        if hand != '':
                            if four_max_BTNvsUTG.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max BTN vs UTG all in")
            elif judge[1] == 2:
                if judge[2] == 0:
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if three_max_SB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max SB")
                elif judge[2] == 2:
                    if judge[3] == 3:
                        find_hand()
                        if hand != '':
                            if four_max_SB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max SB")
                elif judge[2] == 3:
                    if judge[3] == 3:
                        find_hand()
                        if hand != '':
                            if four_max_SBvsBTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max SB vs BTN all in")
            elif judge[1] == 3:
                if judge[2] == 0:
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if three_max_SBvsBTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max SB vs BTN all in")
                elif judge[2] == 2:
                    if judge[3] == 3:
                        find_hand()
                        if hand != '':
                            if four_max_SBvsUTG.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max SB vs UTG all in")
                elif judge[2] == 3:
                    if judge[3] == 3:
                        find_hand()
                        if hand != '':
                            if four_max_SBvsUTGBTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max SB vs UTG BTN all in")
        elif judge[0] == 2:
            if judge[1] == 0:
                if judge[2] == 3:
                    if judge[3] == 1:
                        find_hand()
                        if hand != '':
                            if three_max_BBvsSB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max BB vs SB all in")
            elif judge[1] == 2:
                if judge[2] == 3:
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if four_max_BBvsSB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max BB vs SB all in")
            elif judge[1] == 3:
                if judge[2] == 0:
                    if judge[3] == 1:
                        find_hand()
                        if hand != '':
                            if four_max_BBvsSB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max BB vs SB all in")
                elif judge[2] == 2:
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if four_max_BBvsBTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max BB vs BTN all in")
                elif judge[2] == 3:
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if four_max_BBvsBTNSB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max BB vs BTN SB all in")
        elif judge[0] == 3:
            if judge[1] == 0:
                if judge[2] == 0:
                    if judge[3] == 1:
                        find_hand()
                        if hand != '':
                            if two_max_BB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("2max BB")
                elif judge[2] == 2:
                    if judge[3] == 1:
                        find_hand()
                        if hand != '':
                            if three_max_BBvsBTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max BB vs BTN all in")
                elif judge[2] == 3:
                    if judge[3] == 1:
                        find_hand()
                        if hand != '':
                            if three_max_BBvsBTNSB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max BB vs BTN SB all in")
            elif judge[1] == 2:
                if judge[2] == 0:
                    if judge[3] == 1:
                        find_hand()
                        if hand != '':
                            if three_max_BBvsBTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max BB vs BTN")
                elif judge[2] == 2:
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if four_max_BBvsUTG.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max BB vs UTG")
                elif judge[2] == 3:
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if four_max_BBvsUTGSB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max BB vs UTG SB all in")
            elif judge[1] == 3:
                if judge[2] == 0:
                    if judge[3] == 1:
                        find_hand()
                        if hand != '':
                            if three_max_BBvsBTNSB.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("3max BB vs BTN SB all in")
                elif judge[2] == 2:
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if four_max_BBvsUTGBTN.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max BB vs UTG BTN all in")
                elif judge[2] == 3:
                    if judge[3] == 2:
                        find_hand()
                        if hand != '':
                            if four_max_BBvsALL.find(hand) == -1:
                                pyautogui.click(101,948) #fold
                            else:
                                pyautogui.click(266,944) #allin
                            print("4max BB vs UTG BTN SB all in")
    else:
        continue
    hand = ''






