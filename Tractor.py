import simplegui
import random
import math

#buttons!
#180 by 80
start_button_img = simplegui.load_image("http://i.imgur.com/8msYc3y.png")
help_button_img = simplegui.load_image("http://i.imgur.com/DUoVUUW.png")
settings_button_img = simplegui.load_image("http://i.imgur.com/PcNyt1l.png")
#100 by 40
deal_button_img = simplegui.load_image("http://i.imgur.com/6PJvLHk.png")
#30 by 30
home_button_img = simplegui.load_image("http://i.imgur.com/4NdWXyZ.png")
#92 by 72 (not 90 by 70 because I am stupid)
cpu1_button_img = simplegui.load_image("http://i.imgur.com/icpVOLG.png")
cpu2_button_img = simplegui.load_image("http://i.imgur.com/uWmq8qy.png")
cpu3_button_img = simplegui.load_image("http://i.imgur.com/C3sTdQY.png")
#82 by 52
on_off_button_img = simplegui.load_image("http://i.imgur.com/GRpjCS4.png")
animation_speed_img = simplegui.load_image("http://i.imgur.com/kcgeaya.png")
#70 by 70
sound_max_img = simplegui.load_image("http://i.imgur.com/Hk3ogQE.png")
sound_two_img = simplegui.load_image("http://i.imgur.com/TR2UWFq.png")
sound_one_img = simplegui.load_image("http://i.imgur.com/TPzGvYm.png")
sound_off_img = simplegui.load_image("http://i.imgur.com/V47PemX.png")
music_on_img = simplegui.load_image("http://i.imgur.com/9eAciKY.png")
music_off_img = simplegui.load_image("http://i.imgur.com/dpDW6qV.png")
#70 by 30
play_button_img = simplegui.load_image("http://i.imgur.com/65MI8an.png")
deposit_button_img = simplegui.load_image("http://i.imgur.com/AvYk3zO.png")
sort_button_img = simplegui.load_image("http://i.imgur.com/Z0A891Q.png")
random_button_img = simplegui.load_image("http://i.imgur.com/CjlFXZb.png")
#20 by 20
hourglass_img = simplegui.load_image("http://i.imgur.com/8c5hNPI.png")

#240 by 160
title_img = simplegui.load_image("http://i.imgur.com/KjCoQJm.png")

#sounds
play_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s1359SPwBdY0&command=download_mp3")
deal_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0U55DIbtLp3&command=download_mp3")
button_sound = simplegui.load_sound("https://freesound.org/data/previews/257/257357_4781497-lq.mp3")
loss_sound = simplegui.load_sound("https://freesound.org/data/previews/194/194624_3544016-lq.mp3")
win_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s1VmygHm4fUV&command=download_mp3")

#music
music1 = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0zTEimtfvV4&command=download_mp3")
music2 = simplegui.load_sound("http://66.90.93.122/ost/pokemon-trading-card-game/zjwcafgylp/17-credits.mp3")
music3 = simplegui.load_sound("http://66.90.93.122/ost/tetris-gameboy-rip-/eeeughvtth/tetris-gameboy-02.mp3")
music4 = simplegui.load_sound("http://66.90.93.122/ost/las-vegas-casino-atari-8-bit-/yiqfqsktqt/02-black-jack.mp3")
music5 = simplegui.load_sound("http://66.90.93.122/ost/las-vegas-casino-atari-8-bit-/yiqfqsktqt/02-black-jack.mp3")
music6 = simplegui.load_sound("")
soundtracks = {0:music1, 1:music2, 2:music3, 3:music4, 4:music5, 5:music6}
for i in soundtracks:
    soundtracks[i].set_volume(0.15)
soundtrack_num = 0
               
#load win/lose images
#400 by 100
blackjack_msg = simplegui.load_image("http://i.imgur.com/EKRkEtC.png")
win_msg = simplegui.load_image("http://i.imgur.com/QlzjBer.png")
lose_msg = simplegui.load_image("http://i.imgur.com/HwFd9Td.png")

#suits image 200 by 200
suits_image = simplegui.load_image("http://i.imgur.com/H7uTKYI.png")

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

joker_images = simplegui.load_image("http://i.imgur.com/5Ide7rb.jpg")
JOKER_SIZE = (260, 358) #261.5
JOKER_CENTER = (130.75, 179) #130.75

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize global variables
# global variables specific to a game
# are stored in home() function
start_buttons = []
setting_buttons = []
help_buttons = []

AI_difficulty = {0:0, 1:1, 2:1, 3:1}
animation = True
animation_speed = 2
deal_timer = 10
spin_timer = 0
volume = 1

# define global constants for cards:
# tuples for suits and ranks
# dictionary of values
SUITS = ('C','S','H','D')
SUITS_IMAGE_ORDER = ('S', 'H', 'D','C')
RANKS = ('A','2','3','4','5','6',
         '7','8','9','10','J','Q','K')
VALUES = {'A':14,'2':2,'3':3,
          '4':4,'5':5,'6':6,
          '7':7,'8':8,'9':9,
          '10':10,'J':11,
          'Q':12,'K':13, "Joker": 15}
POINTS = {'A':0,'2':0,'3':0,
          '4':0,'5':5,'6':0,
          '7':0,'8':0,'9':0,
          '10':10,'J':0,
          'Q':0,'K':10, "Joker": 0}

# text on help page
help_text = [[[20, 50], "Welcome to Sheng Ji, a traditional Chinese card game! This help page is "],
             [[20, 75], "meant as a reference only. For a full set of rules, please refer to the site:"],
             [[20, 100], "https://goo.gl/XGU4p1"],
             [[20, 135], "Points cards:"],
             [[20, 160], "Rank: 5            Rank: 10            Rank: K"],
             [[20, 185], "Points: 5          Points: 10          Points:10"],
             [[20, 220], "Card Values:"],
             [[20, 245], "Rank:  2   3   4   5   6   7   8   9   10   J    Q   K   A   Joker"],
             [[20, 270], "Value: 2   3   4   5   6   7   8   9   10   11  12  13  14  15"],
             [[20, 305], "The power group is all cards with suit = power suit or value = level, "],
             [[20, 330], "as well as the Joker. The power suit is displayed in the center of "],
             [[20, 355], "the game. All remaining cards are split into groups corresponding to "],
             [[20, 380], "their suits. On every turn, each player must put down a card of the same "],
             [[20, 405], "group as the first card played that round. "],
             [[20, 440], "The strength of cards in order from highest to lowest"],
             [[20, 465], "is Red Joker, Black Joker, Power Suit level card, "],
             [[20, 490], "remaining level cards, remaining power group cards"],
             [[20, 515], "from highes to lowest value, remaining cards (of same "],
             [[20, 540], "group) from highest to lowest value." ]
            ]

# buttons!
class Button:
    def __init__(self, pos1, pos2, image, link):
        self.pos1 = pos1
        self.pos2 = pos2
        self.image = image
        self.link = link
        self.clicked = False
    def draw(self, canvas):
        if self.image != None:
            size_x, size_y = self.pos2[0] - self.pos1[0], self.pos2[1] - self.pos1[1]
            pos_x, pos_y = (self.pos2[0] + self.pos1[0])/2.0, (self.pos2[1] + self.pos1[1])/2.0
            canvas.draw_image(self.image, (size_x/2, size_y/2), (size_x, size_y), \
                              (pos_x, pos_y), (size_x, size_y))
        
        # following are the texts that specific button show
        if self.link == "Confirm Yes":
            canvas.draw_text("Yes", [self.pos1[0], self.pos2[1]], 25, 'black')
        elif self.link == "Confirm No":
            canvas.draw_text("No", [self.pos1[0], self.pos2[1]], 25, 'black')
        elif self in setting_buttons:
            if self.link[5:] == "difficulty":
                canvas.draw_text(str(AI_difficulty[int(self.link[3])]), [self.pos1[0]+35, self.pos2[1]+30], 30, 'Black')
            elif self.link == "Animation":
                if animation:
                    canvas.draw_text("On", [self.pos2[0] + 15, self.pos2[1]-15], 30, 'black')
                else:
                    canvas.draw_text("Off", [self.pos2[0] + 15, self.pos2[1]-15], 30, 'black')
            elif self.link == "Animation Speed":
                canvas.draw_text(str(animation_speed), [self.pos2[0] + 20, self.pos2[1]-15], 30, 'black')
        elif self.link == 'Back':
            canvas.draw_text('Back', [self.pos1[0], self.pos2[1]-5], 25, 'black')
                              
    def click(self, position):
        global playing, temp_playing, animation, animation_speed, volume, soundtrack_num
        if self.pos1[0] <= position[0] <= self.pos2[0] and self.pos1[1] <= position[1] <= self.pos2[1]:
            # :,)
            button_sound.rewind()
            button_sound.play()
            
            # performs actions of buttons
            # start buttons take you to different pages
            if self.link == "Start":
                start_new_game()
            elif self.link == "Settings":
                playing = "Settings"
            elif self.link == "Help":
                playing = "Help"
                
            # adjusts skill levels of the cpu
            elif self.link == "cpu1_difficulty":
                AI_difficulty[1] = (AI_difficulty[1]+1)%3
            elif self.link == "cpu2_difficulty":
                AI_difficulty[2] = (AI_difficulty[2]+1)%3
            elif self.link == "cpu3_difficulty":
                AI_difficulty[3] = (AI_difficulty[3]+1)%3
                
            # controls animation on/off, volume, and music
            elif self.link == "Animation":
                if animation:
                    animation = False
                else:
                    animation = True
            elif self.link == "Animation Speed":
                if animation_speed == 4:
                    animation_speed = 1
                else:
                    animation_speed += 1
            elif self.link == "Sound":
                if volume == 0:
                    self.image = sound_one_img
                    change_volume(0.33)
                    volume = 0.33
                elif volume == 0.33:
                    self.image = sound_two_img
                    change_volume(0.66)
                    volume = 0.66
                elif volume == 0.66:
                    self.image = sound_max_img
                    change_volume(1)
                    volume = 1
                else:
                    self.image = sound_off_img
                    change_volume(0)
                    volume = 0
            elif self.link == "Music":
                soundtracks[soundtrack_num].rewind()
                soundtrack_num = (soundtrack_num + 1)%6
                if soundtrack_num == 5:
                    self.image = music_off_img
                elif soundtrack_num == 0:
                    self.image = music_on_img
                    
            # in game buttons
            elif self.link == "Deal":
                deal()
            elif self.link == "Deposit" and selected_card != None:
                play_deposit(selected_card, player_hand, len(deposit))
            elif self.link == "Deposit Random":
                play_deposit(random.choice(player_hand.cards), player_hand, len(deposit))
            elif self.link == "Play":
                if selected_card != None:
                    play_card(selected_card, player_hand)
            elif self.link == "Play Random":
                decide_move(player_hand)
            elif self.link == "Sort":
                sort(player_hand.cards, 0)
            elif self.link == "Back":
                playing = "Home"
                
            # quit game and confirm quit buttons
            elif self.link == "Quit":
                temp_playing = playing
                playing = "Confirm"
                deal_sound.rewind()
            elif self.link == "Confirm Yes":
                home()
            elif self.link == "Confirm No":
                playing = temp_playing
                

# define card class
class Card:
    def __init__(self, suit, rank,):
        self.suit = suit
        self.rank = rank
        self.pos = [300, 300]

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank
    
    def get_group(self):
        # returns what group the card belongs to
        if self.suit == power_suit:
            return 'power'
        if VALUES[self.rank] == level:
            return 'power'
        if self.get_rank() == "Joker":
            return 'power'
        return self.suit

    def draw(self, canvas, direction):
        if self.rank != "Joker":
            card_img_loc = (CARD_CENTER[0] + RANKS.index(self.rank)*CARD_SIZE[0],
                              CARD_CENTER[1] + SUITS.index(self.suit)*CARD_SIZE[1])
            canvas.draw_image(card_images,
                              card_img_loc,
                              CARD_SIZE,
                              self.pos,
                              CARD_SIZE,
                             direction)
        else:
            joker_img_loc = [JOKER_CENTER[0], JOKER_CENTER[1]]
            if self.suit == "H":
                joker_img_loc[0] += JOKER_SIZE[0]
            canvas.draw_image(joker_images,
                              joker_img_loc,
                              JOKER_SIZE,
                              self.pos,
                              CARD_SIZE,
                             direction)    
    def draw_back(self, canvas, direction):
        canvas.draw_image(card_back,
                          CARD_BACK_CENTER,
                          CARD_BACK_SIZE,
                          self.pos,
                          CARD_BACK_SIZE,
                            direction)
    

# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        s = ""
        for card in self.cards:
            s += str(card) + " "
        return s   
    
        self.cards.append(card)
    
    def draw(self, canvas, pos, direction):
        # determines position of cards by spacing them by 20 and centering
        for card in self.cards:
            if self == player_hand:
                dy = 0
                if card == selected_card:
                    dy = 10
                card.pos = [pos[0]-10*len(self.cards) + 20*self.cards.index(card), pos[1] - dy]
                card.draw(canvas, direction)
            elif self == cpu1_hand:
                card.pos = [pos[0], pos[1] - 10*len(self.cards) + 20*self.cards.index(card)]
                card.draw_back(canvas, direction)
            elif self == cpu2_hand:
                card.pos = [pos[0]-10*len(self.cards) + 20*self.cards.index(card), pos[1]]
                card.draw_back(canvas, direction)
            else:
                card.pos = [pos[0], pos[1] - 10*len(self.cards) + 20*self.cards.index(card)]
                card.draw_back(canvas, direction)
            
            
       
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.cards.append(Card(SUITS[i],RANKS[j]))
        self.cards.append(Card("H", "Joker"))
        self.cards.append(Card("S", "Joker"))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self, i):
        return self.cards[i]
    
    def __str__(self):
        s = ""
        for card in self.cards:
            s += str(card) + " "
        return s
    def draw(self, canvas):
        for i in range(int(math.ceil(len(self.cards)/8.0))):
            canvas.draw_image(card_back,
                          CARD_BACK_CENTER,
                          CARD_BACK_SIZE,
                          [295+i, 295+i],
                          CARD_BACK_SIZE,
                          0)
            
# function for changing volume in settings
def change_volume(volume):
    play_sound.set_volume(volume)
    deal_sound.set_volume(volume)
    button_sound.set_volume(volume)
    loss_sound.set_volume(volume)
    win_sound.set_volume(volume)
    for i in range(6):
        soundtracks[i].set_volume(0.15*volume)
    
#AI for deciding move
def decide_move(hand): 
    skill = AI_difficulty[turn]
    
    # if player is first to go in a round
    # will play a power card if it has enough to spare
    # player who played deposit may or may not play power
    # depending on if deposited points are worth
    # saving
    if len(played_cards) == 0 and skill  >= 1:
        power_count = 0.0
        for card in hand.cards:
            if card.get_group() == 'power':
                power_count += 1.0   
        if power_count == 1.0: #to save last power card
            power_count = 0
        # this is the player that played deposit, will
        # likely play power if there are points to be saved
        if deposit_turn == turn:
            if get_points(deposit) >= 10 and power_count/len(hand.cards) > 0.33 and \
            ('power' in known_groups[(turn+1)%4] and 'power' in known_groups[(turn+3)%4]):
                for card in hand.cards:
                    # this is to ensure they don't always play smallest power card
                    if card.get_group() == 'power' and random.random() > 0.7:
                        play_card(card, hand)
                        return
        # a player will play power if they have enough to
        # spare, to drain power cards of opponents
        elif power_count/len(hand.cards) > 0.33 and ('power' in known_groups[(turn+1)%4] and 'power' in known_groups[(turn+3)%4]):
            for card in hand.cards:
                if card.get_group() == 'power' and random.random() > 0.7:
                    play_card(card, hand)
                    return
        # highest skill player will play largest card in non power group
        # (this is a common move among actual players)
        if skill == 2:
            for card in hand.cards:
                if VALUES[card.get_rank()] >= 13 and str(card) not in power_group:
                    if str(unplayed[card.get_group()][-1]) == str(card):
                        play_card(card, hand)
                        return
        # play random in all other cases, as it doesn't really matter
        card = random.choice(hand.cards)
        if POINTS[card.get_rank()] > 0 and random.random() > 0.7:
            play_card(card, hand)
            return                
        play_card(random.choice(hand.cards), hand)
        return
    elif len(played_cards) == 0: #skill = 0
        play_card(random.choice(hand.cards), hand)
        return
    
    # all the code that follows are if you're not first to go in a turn
    # group cards is all cards of hand that have same group as the initial
    # group. played group is group of first card played
    group_cards = []
    played_group = played_cards[0].get_group()

    for card in hand.cards:
        if card.get_group() == played_group:
            group_cards.append(card)
    # max_played is largest card played so far in turn
    max_played = get_max(played_cards)
    
    # if you only have one group card, that's the only card you can play
    if len(group_cards) == 1:
        play_card(group_cards[0], hand)
        return
    
    # on weakest skill level, the AI will just play any
    # card that is allowed, at random
    if skill == 0:
        if len(group_cards) > 0:
            play_card(random.choice(group_cards), hand)
            return
        else:
            play_card(random.choice(hand.cards), hand)
            return    
    
    # Medium skill level
    elif skill == 1:
        # if 10+ points are present, try to top the opponent's cards
        if get_points(played_cards) >= 10:
            if len(group_cards) > 0:
                for card in group_cards:
                    if compare(max_played, card)[1] == card:
                        play_card(card, hand)
                        return
                forfeit(group_cards, hand)
                return
            else:
                for card in hand.cards:
                    if compare(max_played, card)[1] == card:
                        play_card(card, hand)
                        return
                forfeit(group_cards, hand)
                return
        elif len(group_cards) > 0:
            # if you are last to play and your partner is leading the round,
            # play a points card
            if (init_turn - turn)%4 == 1:
                if played_cards.index(max_played) == 1:
                    for card in group_cards:
                        if POINTS[card.get_rank()] > 0:
                            play_card(card, hand)
                            return
                # play random if you are not last to move, or if you can't win
                # the round
                forfeit(group_cards, hand)
                return
            else:
                play_card(random.choice(group_cards), hand)
                return
        else:
            # same as before, but in the case that you are out of group cards
            if (init_turn - turn)%4 == 1:
                if played_cards.index(max_played) == 1:
                    for card in hand.cards:
                        if POINTS[card.get_rank()] == 10:
                            play_card(card, hand)
                            return
                forfeit(group_cards, hand)
                return
            else:
                play_card(random.choice(hand.cards), hand)
                return
            
    # Highest Skill Level
    # decides move if player is last to go in a round
    if (init_turn - turn)%4 == 1:
        # if partner is already winning round, either
        # place points or place smallest card you can
        if played_cards.index(max_played) == 1:
            if len(group_cards) > 0:
                for card in group_cards:
                    if POINTS[card.get_rank()] > 0:
                        play_card(card, hand)
                        return
                forfeit(group_cards, hand)
                return
            forfeit(group_cards, hand)
            return
        # if there are points to be won, place the smallest
        # card possible that will win the round
        # otherwise, place smallest card possible
        elif get_points(played_cards) >= 10:
            if len(group_cards) > 0:
                for card in group_cards:
                    if compare(card, max_played)[1] == card:
                        play_card(card, hand)
                        return
                forfeit(group_cards, hand)
                return
            elif played_group != "power":
                for card in hand.cards:
                    if card.get_group() == "power" and POINTS[card.get_rank()] > 0:
                        play_card(card, hand)
                        return
                for card in hand.cards:
                    if card.get_group() == "power":
                        play_card(card, hand)
                        return
        elif len(group_cards) > 0:
            forfeit(group_cards, hand)
            return
        forfeit(group_cards, hand)
        return
    
    
    # if second to last to move
    elif (turn - init_turn)%4 == 2:
        #if your partner currently has largest card
        if played_cards.index(max_played) == 0:
            if len(group_cards) > 0:
                # if last player still has cards of suit
                if played_group in known_groups[(turn+1)%4]:
                    for card in group_cards:
                        # will risk playing a points card with a probability 
                        # 1 / number of cards unplayed that is greater than it
                        if POINTS[card.get_rank()] == 10:
                            for i in range(len(unplayed[played_group])):
                                if compare(card, unplayed[played_group][-i])[1] == card:
                                    if random.random() < 1.0/(i+1):
                                        play_card(card, hand)
                                        return
                    # will otherwise just play largest non-points card unless power
                    if played_group != 'power':
                        for i in range(len(group_cards)):
                            if POINTS[group_cards[-i].get_rank()] == 0:
                                play_card(group_cards[-1], hand)
                                return
                    # will otherwise just play smallest card
                    forfeit(group_cards, hand)
                    return
                #if last player has power cards
                elif 'power' in known_groups[(turn+1)%4]:
                    forfeit(group_cards, hand)
                    return
                for card in group_cards:
                    if POINTS[card.get_rank()] > 0:
                        play_card(card, hand)
                        return
                forfeit(group_cards, hand)
                return
            
            # if partner not in lead
            else:
                if played_group in known_groups[(turn+1)%4]:
                    # check if other player can possibly top your teammate
                    for card in hand.cards:
                        if POINTS[card.get_rank()] > 0 and compare(max_played, card)[1] == card:
                            for i in range(len(unplayed[played_group])):
                                if compare(max_played, unplayed[played_group][-i])[1] == max_played:
                                    if random.random() < 1.0/(i+1):
                                        play_card(card, hand)
                                        return
                    
                    forfeit(group_cards, hand)
                    return
                
                # if opponent is out of group but has power          
                elif 'power' in known_groups[(turn+1)%4]:
                    if get_points(played_cards) >= 10 or random.random() > 0.6:
                        if len(hand.cards) >= 3:
                            play_card(hand.cards[-3], hand)
                            return
                        else:
                            play_card(hand.cards[-1], hand)
                            return
                    else:
                        forfeit(group_cards, hand)
                        return
                # if opponent is out of group and power, you're guaranteed
                # a win. Play points if possible
                else:
                    for card in hand.cards:
                        if POINTS[card.get_rank()] == 10:
                            play_card(card, hand)
                            return
                    for card in hand.cards:
                        if POINTS[card.get_rank()] == 5:
                            play_card(card, hand)
                            return
                    forfeit(group_cards, hand)
                    return
                
        #if your partner isn't in the lead                                                  
        else:
            if len(group_cards) > 0:
                # if next player is out of cards of this group
                # but has power card, forfeit the round
                if played_group not in known_groups[(turn+1)%4] and 'power' in known_groups[(turn+1)%4]:
                    forfeit(group_cards, hand)
                    return
                # if points were played or can be played, play your largest card
                # if it's larger than the current largest card
                # otherwise, forfeit the round
                elif get_points(played_cards) >= 10 or (get_points(unplayed[played_group]) >= 15 and random.random() < 1.0/(len(unplayed[played_group]))):
                    if compare(max_played, group_cards[-1])[1] == group_cards[-1]:
                        play_card(group_cards[-1], hand)
                        return
                    forfeit(group_cards, hand)
                    return
                # if your largest card is a points card, play with probability
                # 1 / number of cards left larger than it + 1
                elif POINTS[group_cards[-1].get_rank()] > 10 and compare(group_cards[-1], max_played)[1] == group_cards[-1]:
                    for i in range(len(unplayed[played_group])):
                        if compare(group_cards[-1], unplayed[played_group][-i])[1] == group_cards[-1] and random.random() < 1.0/(i+1):
                            play_card(group_cards[-1], hand)
                            return
                    forfeit(group_cards, hand)
                    return
                # otherwise, forfeit the round
                forfeit(group_cards, hand)
                return
            else:
                # same as before, will play power card if points to be won
                if get_points(played_cards) >= 10 or (get_points(unplayed[played_group]) >= 15 and random.random() < 1.0/(len(unplayed[played_group]))):
                    for card in hand.cards:
                        if card.get_group() == 'power':
                            play_card(card, hand)
                            return
                    forfeit(group_cards, hand)
                    return    
                forfeit(group_cards, hand)
                return
                
    
    # if second to move
    else:
        if len(group_cards) > 0:
            # if your partner can play power card, give a point card
            if played_group not in known_groups[(turn+2)%4] and 'power' in known_groups[(turn+2)%4]:
                for card in group_cards:
                    if POINTS[card.get_rank()] == 10:
                        play_card(card, hand)
                        return
                for card in group_cards:
                    if POINTS[card.get_rank()] == 5:
                        play_card(card, hand)
                        return 
                forfeit(group_cards, hand)
                return
            # if your partner can't play power but opponent can, forfeit
            elif played_group not in known_groups[(turn+1)%4] and 'power' in known_groups[(turn+1)%4]:
                forfeit(group_cards, hand)
                return
            # if neither can play random card
            else:
                # if your largest card is a points card, play it with 
                # 1 / number of cards larger probability
                for card in group_cards:
                    if POINTS[card.get_rank()] == 10 and compare(card, max_played)[1] == card:
                        for i in range(len(unplayed[played_group])):
                            if compare(card, unplayed[played_group][-i])[1] == card and random.random() < 1.0/(i+1):
                                play_card(card, hand)
                                return
                play_card(random.choice(group_cards), hand)
                return
        else:
            # if your partner can play power card, give a point card
            if played_group not in known_groups[(turn+2)%4] and 'power' in known_groups[(turn+2)%4]:
                for card in hand.cards:
                    if POINTS[card.get_rank()] == 10:
                        play_card(card, hand)
                        return
                for card in hand.cards:
                    if POINTS[card.get_rank()] == 5:
                        play_card(card, hand)
                        return 
                forfeit(group_cards, hand)
                return
            # if your partner can't play power but opponent can, forfeit
            elif played_group not in known_groups[(turn+1)%4] and 'power' in known_groups[(turn+1)%4]:
                forfeit(group_cards, hand)
                return
            else:
                # if you have a point power card, play that card
                for card in hand.cards:
                    if POINTS[card.get_rank()] == 10 and card.get_group() == 'power':
                        play_card(card, hand)
                        return
                # if there are points to be won, play power card
                if get_points(unplayed[played_group]) >= 10 or get_points(played_cards) >= 10 or played_group not in known_groups[(turn+2)%4]:
                    for card in hand.cards:
                        if card.get_group() == 'power':
                            play_card(card, hand)
                            return
                play_card(hand.cards[0], hand)
                return 
     
    forfeit(group_cards, hand)

#function for a player who has no way of taking advantage of a turn
def forfeit(group_cards, hand):
    if len(group_cards) > 0:
        for card in group_cards:
            if POINTS[card.get_rank()] == 0:
                play_card(card, hand)
                return
        play_card(group_cards[0], hand)
        return
    else:
        for card in hand.cards:
            if POINTS[card.get_rank()] == 0:
                play_card(card, hand)
                return
        play_card(hand.cards[0], hand)
        return
                
    
# calculate the point value of a group of cards
# by searching POINTS dictionary and adding point values
def get_points(cards):
    points = 0
    for i in range(len(cards)):
        card = cards[i]
        points += POINTS[card.get_rank()]
    return points

# THIS IS NOT GET POINTS. This is for adding points cards
# to the moving (animation) list
def add_points(cards):
    cards_list = []
    cards_list.extend(cards)
    dx = 10*len(points_cards)
    shift = 0
    points = []
    for i in range(len(cards_list)):
        card = cards_list[i]
        if POINTS[card.get_rank()] > 0:
            shift += 10
            moving.append([card, [card.pos[0], card.pos[1]], [card.pos[0], card.pos[1]], [50+dx+shift, 50], points_cards])
            cards.remove(card)

# moves cards to the discard pile
def discard(cards):
    dx = 10*len(discarded)
    shift = 0
    for card in cards:
        shift += 10
        moving.append([card, [card.pos[0], card.pos[1]], [card.pos[0], card.pos[1]], [100+dx+shift, 650], discarded, cards])
        
# has two main functions    
def play_card(card, hand):
    global group, power_suit, status, turn, wait_timer
    # first function is during dealing, when playing a level card
    # decides the power suit and, in a stalemate, the status of
    # each team
    if playing == "Dealing":
        if power_suit != None:
            return
        # if status is already decided, playing level card only
        # decides power suit
        elif status != None and VALUES[card.get_rank()] == level:
            power_suit = card.get_suit()
            return
        # in a stalemate, first team to play level card becomes landlord
        elif hand == player_hand or hand == cpu2_hand:
            if VALUES[card.get_rank()] == player_level:
                power_suit = card.get_suit()
                status = 'landlord'
        else:
            if VALUES[card.get_rank()] == opp_level:
                power_suit = card.get_suit()
                status = 'peasant'
        return 
       
    # second function is adding a card to played cards list
    # in the middle of a round
    if len(played_cards) > 0:
        # if played card is not the group of the first played card
        # then move is only valid if player no longer has original
        # group in its hand
        if played_cards[0].get_group() != card.get_group():
            for hand_card in hand.cards:
                if hand_card.get_group() == played_cards[0].get_group() and str(hand_card) != str(card):
                    print 'You have a ' + str(hand_card) + ' but tried to play a ' + str(card)
                    print 'You have a card of group: ' + hand_card.get_group()
                    print 'The original group this turn is: ' + str(played_cards[0])
                    return
    
    # updates memory lists for AI (memory of which cards have been played) 
    if card.get_group() in known_groups[turn]:
        known_groups[turn].remove(card.get_group())
        
    for unplayed_card in unplayed[card.get_group()]:
        if str(unplayed_card) == str(card):
            unplayed[card.get_group()].remove(unplayed_card)
            
    # card, start pos, current pos, end pos, dest
    moving.append([card, [card.pos[0],card.pos[1]], [card.pos[0], card.pos[1]], [300 - 50*(2-turn)*((turn)%2), 300 + 50*(1-turn)*((turn+1)%2)], played_cards])
    hand.cards.remove(card)
    turn = (turn+1)%4
    if turn == 0 and len(played_cards) < 3:
        wait_timer = 80/animation_speed
    else:
        wait_timer = 200/animation_speed
    
# Used by AI to decide which cards to deposit
def decide_deposit(hand):
    cards = hand.cards
    suits = {'C':[], 'S':[], 'H':[], 'D':[], 'power':[]}
    deposit_count = 0
    
    for suit in SUITS:
        for card in cards:
            if card.get_group() == suit:
                suits[suit].append(card)
    for card in cards:
        if card.get_group() == 'power':
            suits['power'].append(card)
            
    # will try to completely remove a non power group in deposit
    for suit in SUITS:
        if 0 < len(suits[suit]) <= 6:
            if get_points(suits[suit]) <= 10 or len(suits['power']) >= 5:
                for card in suits[suit]:
                    play_deposit(card, hand, deposit_count)
                    deposit_count += 1
                    if deposit_count == 6:
                        return
                    
    for suit in SUITS:
        if len(suits[suit]) > 6:
            for i in range(len(suits[suit])):
                card = suits[suit][i]
                play_deposit(card, hand, deposit_count)
                deposit_count += 1
                if deposit_count == 6:
                    return   
                
    for card in hand.cards:
        play_deposit(card, hand, deposit_count)
        deposit_count += 1
        if deposit_count == 6:
            return
                
# adds card to deposit pile
def play_deposit(card, hand, num):
    #hand.cards.remove(card)
    dx = 10*num
    moving.append([card, [card.pos[0], card.pos[1]], [card.pos[0], card.pos[1]], [550-dx, 50], deposit, hand.cards])
        
# NEED power suit, played_cards, power_group, level for this to work
# compares two cards and returns as list [weaker, stronger]
def compare(card1, card2):
    turn_suit = played_cards[0].get_suit()
    # if card is of wrong group and not in power group, it loses automatically
    if card1.get_suit() != turn_suit and str(card1) not in power_group:
        return [card1, card2]
    elif card2.get_suit() != turn_suit and str(card2) not in power_group:
        return [card2, card1]
    # power group trumps non power group
    elif str(card1) in power_group and str(card2) not in power_group:
        return [card2, card1]
    elif str(card2) in power_group and str(card1) not in power_group:
        return [card1, card2]
    # if both cards not in power group, winner is higher value
    elif str(card1) not in power_group:
        if VALUES[card1.get_rank()] > VALUES[card2.get_rank()]:
            return [card2, card1]
        else:
            return [card1, card2]
    else:
        # The rest are ranking power group comparisons within each other
        # starting with HJoker, SJoker, level card power suit, level cards,
        # then rank
        if card1.get_rank() == "Joker":
            if card2.get_rank() == "Joker" and card2.get_suit() == "H":
                return [card1, card2]
        elif VALUES[card1.get_rank()] == level:
            if card2.get_rank() == "Joker":
                return [card1, card2]
            elif VALUES[card2.get_rank()] == level:
                if card2.get_suit() == power_suit:
                    return [card1, card2]
        elif VALUES[card2.get_rank()] == level:
            return [card1, card2]
        elif VALUES[card2.get_rank()] > VALUES[card1.get_rank()]:
            return [card1, card2]
        return [card2, card1]

# finds strongest card in list of cards with recursion :)
def get_max(cards):
    temp_cards = []
    temp_cards.extend(cards)
    if len(temp_cards) == 1:
        return cards[0]
    else:
        temp_cards.remove(compare(temp_cards[0], temp_cards[1])[0])
        return get_max(temp_cards)

# finds weakest card in list of cards with recursion :)
def get_min(cards):
    temp_cards = []
    temp_cards.extend(cards)
    if len(temp_cards) == 1:
        return cards[0]
    else:
        temp_cards.remove(compare(temp_cards[0], temp_cards[1])[1])
        return get_max(temp_cards)
    
# sorts cards by their respective groups, and from smallest to largest
# within those groups
def sort(cards, player):
    global player_hand
    temp_suits = ['H', 'C', 'S', 'D']
    random.shuffle(temp_suits)
    sort_cards = []
    for suit in temp_suits:
        for i in range(2, 15):
            for card in cards:
                if str(card) not in power_group and VALUES[card.get_rank()] == i and card.get_suit() == suit:
                    sort_cards.append(card)
    for i in range(2,15):
        for card in cards:
            if str(card) in power_group and i != level and VALUES[card.get_rank()] == i:
                sort_cards.append(card)
    for card in cards:
        if VALUES[card.get_rank()] == level and card.get_suit() != power_suit:
            sort_cards.append(card)
    for card in cards:
        if VALUES[card.get_rank()] == level and card.get_suit() == power_suit:
            sort_cards.append(card)
            break
    for suit in ['S', 'H']:
        for card in cards:
            if VALUES[card.get_rank()] == 15 and card.get_suit() == suit:
                sort_cards.append(card)
                
    if player == 0:
        player_hand.cards = []
        for i in range(len(sort_cards)):
            card = sort_cards[i]
            moving.append([card, [card.pos[0], card.pos[1]], [card.pos[0], card.pos[1]], [310-10*len(sort_cards) + 20*i, 500], player_hand.cards])
    else:
        return sort_cards
    
# function for ending a round
def end_round():
    global peasant_points, level, player_level, opp_level, status
    global power_suit, power_group, selected_card, playing
        
    # is peasant wins last round, give them points in deposit
    if (status == 'peasant' and init_turn%2 == 0) or (status == 'landlord' and init_turn%2 == 1):
        peasant_points += get_points(deposit)
        add_points(deposit)
        
    # decides status of next level by seeing is peasant gained 45 points    
    # 75 points will level up peasants immediately
    # if peasants earn fewer than 45 points, landlords level up
    if peasant_points >= 45:
        if status == 'peasant':
            if peasant_points >= 75:
                player_level += 1
            status = 'landlord'
            level = player_level
            win_sound.play()
        else:
            if peasant_points >= 75:
                opp_level += 1
            status = 'peasant'
            level = opp_level
            loss_sound.play()
    else:
        if status == 'peasant':
            opp_level += 1
            level = opp_level
            loss_sound.play()
        else:
            player_level += 1
            level = player_level
            win_sound.play()
            
    # resets data for next round
    peasant_points = 0
    power_suit = None
    power_group = []
    selected_card = None
    
    playing = "Game Over"
    
# initializes conditions for a new round   
def initialize_round():
    global turn, init_turn, deposit_turn, wait_timer, unplayed, known_groups
    
    temp_deck = Deck()
    # decides power group for round
    for card in temp_deck.cards:
        if card.get_suit() == power_suit:
            power_group.append(str(card))
        elif VALUES[card.get_rank()] == level:
            power_group.append(str(card))
        elif card.get_rank() == "Joker":
            power_group.append(str(card))
    # person who gets deposit is randomly chosen from landlords
    if status == 'peasant':
        deposit_turn = random.choice([1,3])
    else:
        deposit_turn = random.choice([0,2])
     
    init_turn, turn = deposit_turn, deposit_turn
    
    # adds deposit cards to respective hands 
    for i in range(6):
        card = deck.deal_card(i)
        if init_turn == 0:
            moving.append([card, [300, 300], [300,300], [420 + 10*i, 500], player_hand.cards, deck.cards])
        elif init_turn == 1:
            moving.append([card, [300, 300], [300,300], [100, 420 + 10*i], cpu1_hand.cards, deck.cards])
        elif init_turn == 2:
            moving.append([card, [300, 300], [300,300], [180 - 10*i, 100], cpu2_hand.cards, deck.cards])
        elif init_turn == 3:
            moving.append([card, [300, 300], [300,300], [500, 180 - 10*i], cpu3_hand.cards, deck.cards])
    
    # initializes AI memory of which player has which groups and which
    # cards have not been played
    known_groups = {0:['C', 'S', 'H', 'D'], 1:['C', 'S', 'H', 'D'],
                    2:['C', 'S', 'H', 'D'], 3:['C', 'S', 'H', 'D']}
    temp_deck = Deck()
    temp_deck.cards = sort(temp_deck.cards, 1)
    unplayed = {}
                                                                              
    for i in range(4):
        for j in range(4):
            if power_suit == known_groups[i][j]:
                known_groups[i][j] = 'power'
    
    for group in known_groups[0]:
        unplayed[group] = []
            
    for card in temp_deck.cards:
        unplayed[card.get_group()].append(card)
    
    wait_timer = 200/animation_speed

# decides the result of a turn
def end_turn():
    global played_cards, turn, init_turn, peasant_points, playing, wait_timer
    
    top_card = get_max(played_cards)
    winner = (init_turn + played_cards.index(top_card))%4
    
    # adds points if winner of turn is peasant
    if (winner%2 == 0 and status == 'peasant') or (winner%2 == 1 and status == 'landlord'):
        peasant_points += get_points(played_cards)
        add_points(played_cards)
        
    discard(played_cards)
        
    # winner goes first next round
    turn = winner
    init_turn = winner
    wait_timer = 200/animation_speed
    if winner == 0:
        wait_timer = 100/animation_speed
    
    # when any player is out of cards, the round ends
    if len(player_hand.cards) == 0:
        playing = "End Round"
        wait_timer = 200/animation_speed
        
# computer AI for deciding if they should play level card
# during dealing to set the power suit
def set_power_suit(cards):
    level_cards = []
    
    if cards == player_hand.cards:
        hand = player_hand
    elif cards == cpu1_hand.cards:
        hand = cpu1_hand
    elif cards == cpu2_hand.cards:
        hand = cpu2_hand
    else:
        hand = cpu3_hand
        
    for card in cards:
        if VALUES[card.get_rank()] == level:
            level_cards.append(card)
            
    # if status is not decided, play level card to clain landlord status        
    if status == None and len(level_cards) > 0:
        play_card(level_cards[0], hand)
        return
    
    # otherwise, only play level card if you have at least 3 
    # other cards of that suit
    for level_card in level_cards:
        count = 0
        for card in cards:
            if VALUES[card.get_rank()] != level and card.get_suit() == level_card.get_suit():
                count += 1
        if count >= 3:
            play_card(level_card, hand)
            return
        
# initializes new game conditions (NOT new round conditions)
# restarts game from level 2
def home():
    global moving, playing, turn, init_turn, deposit_turn, selected_card
    global group, played_cards, points_cards, deposit, discarded
    global power_suit, power_group, player_level, opp_level, level, wait_tier 
    global status, peasant_points, deck, wait_timer
    
    moving = []
    playing = "Home"
    turn = 0
    init_turn = 0
    deposit_turn = 0
    selected_card = None
    group = None

    played_cards = []
    points_cards = []
    deposit = []
    discarded = []

    power_suit = None
    power_group = []
    player_level = 2
    opp_level = 2
    level = 2
    wait_timer = 30
    status = None
    peasant_points = 0
    
    deck = Deck()
    
# naming error, should be start new round :( either way,
# sets up deck for new round
def start_new_game():
    global player_hand, cpu1_hand, cpu2_hand, cpu3_hand, deck, playing
    # player and cpu2 are against cpu1 and cpu3
    player_hand = Hand()
    cpu1_hand = Hand()
    cpu2_hand = Hand()
    cpu3_hand = Hand()
    deal_sound.play()
    for card in discarded:
        moving.append([card, [card.pos[0], card.pos[1]], [card.pos[0], card.pos[1]], [300, 300], deck.cards, discarded])
    for card in points_cards:
        moving.append([card, [card.pos[0], card.pos[1]], [card.pos[0], card.pos[1]], [300, 300], deck.cards, points_cards])
    for card in deposit:
        moving.append([card, [card.pos[0], card.pos[1]], [card.pos[0], card.pos[1]], [300, 300], deck.cards, deposit])
    playing = "Pause"
    
# shuffles and deal cards to each player
def deal():
    global deck, moving, playing, wait_timer
    deck.shuffle()
    moving = []
    player_hand.cards = []
    cpu1_hand.cards = []
    cpu2_hand.cards = []
    cpu3_hand.cards = []
    
    for i in range(12):
        #card, start pos, current pos, end pos, dest
        moving.append([deck.deal_card(4*i), [300, 300], [300, 300], [300+10*i, 500], player_hand.cards, deck.cards])
        moving.append([deck.deal_card(1 + 4*i), [300, 300], [300, 300], [100, 300+10*i], cpu1_hand.cards, deck.cards])
        moving.append([deck.deal_card(2 + 4*i), [300, 300], [300, 300], [300-10*i, 100], cpu2_hand.cards, deck.cards])
        moving.append([deck.deal_card(3 + 4*i), [300, 300], [300, 300], [500, 300-10*i], cpu3_hand.cards, deck.cards])
    playing = "Dealing"
    wait_timer = 200
    
def sort_decks():
    cpu1_hand.cards = sort(cpu1_hand.cards, 1)
    cpu2_hand.cards = sort(cpu2_hand.cards, 1)
    cpu3_hand.cards = sort(cpu3_hand.cards, 1)
    
def mouse_handler(position):
    global selected_card, wait_timer
    
    # home button buttons that take you to different pages
    # or to start new game
    if playing == "Home":
        for button in start_buttons:
            button.click(position)
    elif playing == "Settings":
        for button in setting_buttons:
            button.click(position)
        back_button.click(position)
    elif playing == "Help":
        back_button.click(position)
    if playing == "Home" or playing == "Settings" or playing == "Help":
        return
    
    quit_button.click(position)
    if playing == "Confirm":
        yes_button.click(position)
        no_button.click(position)
    elif playing == "Pause" and wait_timer <= 0:
        deal_button.click(position)
    elif playing == "In Game" or playing == "Deposit" or playing == "Dealing":
        # checks if you are clicking on a card in your hand
        # makes that the selected card
        if 300-10*len(player_hand.cards) - 25 < position[0] < 300+10*len(player_hand.cards)+25 and len(player_hand.cards) > 0 and 450 <= position[1] <= 550:
            num = min((position[0]-(300-10*len(player_hand.cards))+25)/20, len(player_hand.cards)-1)
            selected_card = player_hand.cards[num]
            if playing == "Dealing":
                play_card(selected_card, player_hand)
        # buttons needed to play the game :)
        if playing == "Deposit" and turn == 0 and len(moving) == 0:
            deposit_button.click(position)
            sort_button.click(position)
            deposit_random_button.click(position)
        elif playing == "In Game" and turn == 0 and wait_timer <= 0 and len(moving) == 0:
            play_button.click(position)
            sort_button.click(position)
            play_random_button.click(position)
    elif playing == "Game Over":
        # "Click anywhere to continue" set up next round
        if level == 15: #final level
            home()
            return
        start_new_game()
        wait_timer = 1000/animation_speed
    
# initializes all buttons at the very start of the frame
def start():
    global deal_button, deposit_button, sort_button, play_button, back_button
    global yes_button, no_button, quit_button
    global play_random_button, deposit_random_button
    
    #home page buttons
    # pos1, pos2, image, colour, outline_colour, link
    start_buttons.append(Button([210, 210], [390, 290], start_button_img, "Start"))
    start_buttons.append(Button([210, 310], [390, 390], help_button_img, "Help"))
    start_buttons.append(Button([210, 410], [390, 490], settings_button_img, "Settings"))
    
    # controls sound, music, toggle animation, animation speed, and ai skills
    setting_buttons.append(Button([150, 145], [220, 215], sound_max_img, "Sound"))
    setting_buttons.append(Button([230, 145], [300, 215], music_on_img, "Music"))
    setting_buttons.append(Button([149, 274], [231, 326], on_off_button_img, "Animation"))
    setting_buttons.append(Button([319, 274], [401, 326], animation_speed_img, "Animation Speed"))
    setting_buttons.append(Button([144, 389], [236, 461], cpu1_button_img, "cpu1_difficulty"))
    setting_buttons.append(Button([254, 389], [346, 461], cpu2_button_img, "cpu2_difficulty"))
    setting_buttons.append(Button([364, 389], [456, 461], cpu3_button_img, "cpu3_difficulty"))
    
    # In game buttons
    deal_button = Button([250, 360], [350, 400], deal_button_img, 'Deal')
    
    deposit_button = Button([185, 560], [255, 590], deposit_button_img, "Deposit")
    sort_button = Button([265, 560], [335, 590], sort_button_img, "Sort")
    deposit_random_button = Button([345, 560], [415, 590], random_button_img, "Deposit Random")
    
    play_button = Button([185, 560], [255, 590], play_button_img, "Play")
    play_random_button = Button([345, 560], [415, 590], random_button_img, "Play Random")
    
    # back button for exiting help and settings page
    back_button = Button([20, 560], [70, 590], None, "Back")
    
    # quit button to exiting game 
    quit_button = Button([560, 560], [590, 590], home_button_img, "Quit")

    yes_button = Button([250, 290], [290, 320], None, "Confirm Yes")
    no_button = Button([310, 290], [350, 320], None, "Confirm No")
    
def draw(canvas):
    global playing, wait_timer, power_suit, turn, init_turn, status, deal_timer, spin_timer
    soundtracks[soundtrack_num].play()
    #home screen, display title and navigation buttons
    if playing == "Home": 
        canvas.draw_image(title_img, [120, 80], [240, 160],
                          [300, 100], [240*1.2, 160*1.2])
        for button in start_buttons:
            button.draw(canvas)
    # settings page for controlling sound, animation, and AI skills
    elif playing == "Settings":
        for button in setting_buttons:
            button.draw(canvas)
        back_button.draw(canvas)
        
        canvas.draw_text("Sound:", [145, 130], 30, 'black')
        canvas.draw_text("Animation:", [145, 250], 30, 'black')
        canvas.draw_text("AI Skill Levels:", [145, 370], 30, 'black')
    # displays lines of text for help page
    elif playing == "Help":
        for line in help_text:
            canvas.draw_text(line[1], line[0], 20, 'Black')
        back_button.draw(canvas)
    # everything after this is for In Game
    if playing == "Home" or playing == "Settings" or playing == "Help":
        return
    
    # displays power suit in center of canvas
    if power_suit != None:
        canvas.draw_image(suits_image,
                          [50+100*(SUITS_IMAGE_ORDER.index(power_suit)%2), 50+100*int(SUITS_IMAGE_ORDER.index(power_suit)/2)],
                          [100, 100], [300, 300], [200, 200])        
    # 
    if playing == "Pause":
        if wait_timer <= 0:
            deal_button.draw(canvas)
            deal_sound.rewind()
        else:
            wait_timer -= 1
    # moving contains all cards to be dealt
    # if moving is 0, will initialize round or decide power suit  
    # if it hasn't been already by the players
    elif playing == "Dealing":
        if len(moving) != 0:
            card = moving[0]
        else:
            wait_timer -= 1
            if power_suit != None:
                playing = "Deposit"
            elif wait_timer <= 0:
                power_suit = deck.cards[0].get_suit()
                playing = "Deposit"
                if status == None:
                    status = random.choice(['peasant', 'landlord'])
            if playing == "Deposit":
                deal_sound.rewind()
                initialize_round()
       
    # will draw deposit buttons if player is depositing,
    # otherwise, wait for AI to decide their deposit
    elif playing == "Deposit":
        if turn == 0 and len(moving) == 0:
            deposit_button.draw(canvas)
            sort_button.draw(canvas)
            deposit_random_button.draw(canvas)
        elif wait_timer <= 0:

            if turn == 1 and len(cpu1_hand.cards) > 12:
                decide_deposit(cpu1_hand)
                wait_timer = 200
            elif turn == 2 and len(cpu2_hand.cards) > 12:
                decide_deposit(cpu2_hand)
                wait_timer = 200
            elif turn == 3 and len(cpu3_hand.cards) > 12:
                decide_deposit(cpu3_hand)
                wait_timer = 200
            deal_sound.play()
        else:
            wait_timer -= 1
        if len(deposit) == 6:
            sort_decks()
            playing = "In Game"
            deal_sound.rewind()
            
    # this is just meant to create a slight pause between end of round
    # and initializing next round
    elif playing == "End Round":
        if wait_timer <= 0:
            end_round()
        else:
            wait_timer -= 1
    # displays game over message after each round, and status
    elif playing == "Game Over":
        if status == 'peasant':
            canvas.draw_text("You Lose!", [200, 270], 50, 'gold')
        else:
            canvas.draw_text("You Win!", [200, 270], 50, 'gold')
        if level < 15:
            canvas.draw_text('Next Level: ' + str(level), [210, 300], 25, 'gold')
            canvas.draw_text('Status: ' + status[0].upper() + status[1:], [210, 330], 25, 'gold')
        else:
            canvas.draw_text('Good Game!', [210, 300], 25, 'gold')
            canvas.draw_text('Final Status: ' + status[0].upper() + status[1:], [210, 330], 25, 'gold')
        canvas.draw_text('Click anywhere to continue.', [170, 550], 25, 'gold')
        
    # displays game information such as status and level
    # draws play buttons if it's player's turn
    # calls decide move function if it's AI's turn
    # calls end turn function if all four players have played a card
    elif playing == "In Game":
        canvas.draw_text('Player Level: ' + str(player_level), [20, 500], 20, 'black')
        canvas.draw_text('Opp Level: ' + str(opp_level), [20, 530], 20, 'black')
        canvas.draw_text('Game Level: ' + str(level), [460, 500], 20, 'black')
        canvas.draw_text('Status: ' + status[0].upper() + status[1:], [460, 530], 20, 'black')
        if len(moving) == 0 and len(played_cards) < 4:
            canvas.draw_image(hourglass_img, [10, 10], [20, 20], [300 + 130*(turn%2)*(turn-2), 300 + 130*((turn+1)%2)*(1-turn)], [20, 20], spin_timer)
            spin_timer = (spin_timer + 0.05) - int(spin_timer / (2*math.pi))*2*math.pi
        if turn == 0 and wait_timer <= 0 and len(moving) == 0:
            play_button.draw(canvas)
            sort_button.draw(canvas)
            play_random_button.draw(canvas)
        for card in played_cards:
            card.draw(canvas, 0)
        if len(played_cards) < 4 and wait_timer <= 0:
            if turn == 1:
                decide_move(cpu1_hand)
            elif turn == 2:
                decide_move(cpu2_hand)
            elif turn == 3:
                decide_move(cpu3_hand)
        elif len(played_cards) == 4 and wait_timer <= 0:
            end_turn()
        else:
            wait_timer -= 1
    
    # draws all piles of cards, such as the deck, hands, points, and deposit
    deck.draw(canvas)
    player_hand.draw(canvas, [310, 500], 0)
    cpu1_hand.draw(canvas, [100, 310], math.pi/2)
    cpu2_hand.draw(canvas, [310, 100], math.pi)
    cpu3_hand.draw(canvas, [500, 310], 3*math.pi/2)
    for card in points_cards:
        card.draw(canvas, 0)
    for card in deposit:
        card.draw_back(canvas, 0)
    
    # confirm quit menu
    if playing == "Confirm":
        canvas.draw_polygon(([220, 350], [220, 230], [380, 230], [380, 350]), 4, 'black', 'tan')
        canvas.draw_text("Are you sure?", (232, 267), 25, 'black')
        yes_button.draw(canvas)
        no_button.draw(canvas)
        return
    
    # animation for when cards transfer from lists
    if len(moving) != 0:
        if playing == "Dealing" or (playing == "Deposit" and turn != 0):
                deal_sound.play()
        # if animation, will update the position of the cards gradually
        # to their final destination based on animation speed
        if animation:
            card = moving[0] # THIS IS A LIST, NOT AN OBJECT
            if card[1] == card[2] and playing == "In Game":
                play_sound.play()
            speed = {1:0.05, 2:0.125, 3:0.2, 4:0.25}[animation_speed]
            if len(card) > 5 and card[0] in card[5]:
                card[5].remove(card[0])
            if int(card[2][0]) != int(card[3][0]):
                card[2][0] += speed*int((card[3][0] - card[1][0]))

            if int(card[2][1]) != int(card[3][1]):
                card[2][1] += speed*int((card[3][1] - card[1][1]))
            
            # will compare card's current position to destination
            if int(card[2][0]/10) == int(card[3][0]/10) and int(card[2][1]/10) == int(card[3][1]/10):
                # remove card from previous list (only applies to some cards)
                if power_suit == None and playing == "Dealing" and card[4] != player_hand.cards:
                    set_power_suit(card[4])
                # set position ot final destination
                card[2][0] = card[3][0]
                card[2][1] = card[3][1]
                # adds card to destination list
                card[4].append(moving.pop(0)[0])
                
                
            card[0].pos = card[2]
            card[0].draw(canvas, 0)
            
            # in list of cards that are not appropriate to display
            if playing == "Dealing" or playing == "Deposit": 
                card[0].draw_back(canvas, 0)
        else:
            # if no animation, will use a tick timer to teleport cards one by one
            # based on animation speed
            card = moving[0]
            if len(card) > 5 and card[0] in card[5]:
                card[5].remove(card[0])
            if deal_timer <= 0:
                if playing == "In Game":
                    play_sound.play()
                if power_suit == None and playing == "Dealing" and card[4] != player_hand.cards:
                    set_power_suit(card[4])
                card[0].pos = card[3]
                card[4].append(moving.pop(0)[0])
                deal_timer = 20 - 4*animation_speed
            else:
                deal_timer -= 1
    else:
        deal_sound.rewind()
            
    quit_button.draw(canvas)
    
    

frame = simplegui.create_frame("Cards", 600, 600)
frame.set_canvas_background("Green") 

frame.set_mouseclick_handler(mouse_handler)

frame.set_draw_handler(draw)

# get things rolling
frame.start()
home()
start()

    
    
    
    
    
    

