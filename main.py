# project : chess game

from kivy.config import Config

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '640')
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import actions
from inspect import currentframe, getframeinfo


class GamePiece(ButtonBehavior, Image):
    """A class to hold game pieces objects on the chessboard"""

    def on_press(self):
        """defines behaviour of game piece when pressed"""
        piece = self
        global current_move_options, piece_selected, current_attack_options  # , piece_attacked

        """check condition : a piece on the board was selected 
        & selected piece has attack options 
        & the two pieces are not of same color """
        if piece_selected is not None \
                and len(current_attack_options) is not 0 \
                and ((str(self.source).__contains__('w_')
                      and str(piece_selected.source).__contains__('b_'))
                     or (str(self.source).__contains__('b_')
                         and str(piece_selected.source).__contains__('w_'))):

            """check condition : self location is an optional move (attack) for the piece chosen"""
            # print('debug --- in condition line 26 : \n piece_selected is : ', piece_selected,
            #       '\npiece selected source is : ', piece_selected.source)
            for key in game_arrey:
                if game_arrey[key].get_pos() == self.pos and game_arrey[key].get_pos_id() in current_attack_options:
                    # piece_attacked = self
                    game_arrey[key].clear_piece()
                    self.set_position([800, 800])
                    # piece_attacked.set_position([800, 800])
                    """find current location of chosen piece on the board, and clear that position"""
                    for i in game_arrey:
                        if game_arrey[i].get_pos_id() == piece_selected.get_my_pos_id():
                            game_arrey[i].clear_piece()
                    """take the move : chosen piece move into current location"""
                    piece_selected.set_position(game_arrey[key].get_pos())
                    """set pointer of current location (field) to the piece that moved in"""
                    game_arrey[key].set_piece(piece_selected)
                    # break

                    """check condition : self location is NOT an optional move (attack) for the piece chosen
                    --> piece pressed is set as new selected piece"""
                elif game_arrey[key].get_pos() == self.pos \
                        and game_arrey[key].get_pos_id() not in current_attack_options:
                    piece_selected = self
                    my_pos_id = -1
                    for j in game_arrey:
                        if game_arrey[j].get_pos() == self.pos:
                            my_pos_id = game_arrey[j].get_pos_id()
                            break

                    arrey_map = get_arrey_map()
                    current_move_options = actions.move_options(self.source, my_pos_id, arrey_map)
                    current_attack_options = actions.attack_options(self.source, my_pos_id, arrey_map)
                    print('debug main cur_attck_opt inside condition (55) = ', current_attack_options)
                    print('piece selcted = ', piece_selected, '\ncurrent move options = ', current_move_options)
                    print('data send = ', self.source, my_pos_id, arrey_map)

        else:
            """case not matching other condition :
            no piece is currently selected 
            OR selected piece has NO attack options 
            OR the two pieces are of same color
            --> piece pressed is set as new selected piece"""
            piece_selected = self
            my_pos_id = -1
            for key in game_arrey:
                if game_arrey[key].get_pos() == self.pos:
                    my_pos_id = game_arrey[key].get_pos_id()
                    break

            arrey_map = get_arrey_map()
            current_move_options = actions.move_options(self.source, my_pos_id, arrey_map)
            current_attack_options = actions.attack_options(self.source, my_pos_id, arrey_map)
            print('debug main cur_attck_opt out of condition (91) = ', current_attack_options)
            print('piece selcted = ', piece_selected, '\ncurrent move options = ', current_move_options)
            print('data send = ', self.source, my_pos_id, arrey_map)

        print('debug 121: ', piece_selected, current_move_options, current_attack_options)

    def set_position(self, position):
        """receives position coordinates on board, and set the game piece at that position"""
        self.pos = position

    def get_my_pos_id(self):
        """return the current game piece position id on the board """
        my_pos_id = -1
        for key in game_arrey:
            if game_arrey[key].get_pos() == self.pos:
                my_pos_id = game_arrey[key].get_pos_id()
                break
        return my_pos_id


"""set global variables"""
frameinfo = getframeinfo(currentframe())
# piece_selected = GamePiece()
piece_selected = None
# piece_attacked = GamePiece()
current_move_options = []
current_attack_options = []
turn = 0


class field(ButtonBehavior, Image):
    """A class to hold chessboard coordinates info
    attributes
    ___________
    position : list
        holds field coordinates in format - [x, y] relative to grid 0,0 point
    pos_id : int
        holds field id number (1, 2...) - relative to first field on grid - starts from left bottom (A1, B1...)
    piece_in_field : GamePiece object / None
        holds pointer to the GamePiece object at current location ( = None when location is empty)
    button_color : bool
        determines each location background color (True --> light / False --> dark)"""

    def __init__(self, x, y, color, **kwargs):
        super(field, self).__init__(**kwargs)
        self.position = [x, y]
        self.pos_id = int
        self.piece_in_field = None
        self.button_color = color
        if self.button_color:
            print("debug 72 : set light", self.position)
            self.source = 'Images/light_field.png'
        else:
            print("debug 72 : set dark", self.position)
            self.source = 'Images/dark_field.png'

    def set_pos_id(self, spot_id):
        """receives position id on board, and set self pos_id accordingly"""
        self.pos_id = spot_id

    def get_pos_id(self):
        """return self position id on board"""
        return self.pos_id

    def get_pos(self):
        """return self position coordinates on board"""
        return self.position

    def get_color(self):
        """return self color - location background color (True --> light / False --> dark)"""
        return self.button_color

    def get_piece_in_field(self):
        """return pointer to  GamePiece object at current location (when location is empty, return : None)"""
        return bool(self.piece_in_field)

    # *** check : to delete if not used ***
    # def get_background(self):
    #     return self.background

    def set_piece(self, piece):
        """receives GamePiece object, and set self piece_in_field accordingly
        happens when a piece is moving INTO current location"""
        self.piece_in_field = piece

    def clear_piece(self):
        """set self piece_in_field to : None
        happens when a piece is moving OUT OF current location"""
        self.piece_in_field = None

    def on_press(self):
        """defines behaviour of game field when pressed"""
        if self.source == 'Images/light_field.png':
            self.source = 'Images/light_field_pressed.png'
        elif self.source == 'Images/dark_field.png':
            self.source = 'Images/dark_field_pressed.png'

        global piece_selected, current_move_options, current_attack_options

        """CASE : a piece on the board was selected (previous to current click, user chose a piece)
        check if current location is optional for that piece to move into
        if so : the move is taken"""

        # for debug :
        print('debug 221: ', piece_selected, current_move_options, current_attack_options)

        """check condition : a piece on the board was selected"""
        if piece_selected is not None:
            """check condition : self location is an optional move for the piece chosen"""
            for key in game_arrey:
                if game_arrey[key].get_pos() == self.position and game_arrey[key].get_pos_id() in current_move_options:
                    """find current location of chosen piece on the board, and clear that position"""
                    for i in game_arrey:
                        if game_arrey[i].get_pos_id() == piece_selected.get_my_pos_id():
                            game_arrey[i].clear_piece()
                    """take the move : chosen piece move into current location"""
                    piece_selected.set_position(self.position)
                    """set pointer of current location (field) to the piece that moved in"""
                    game_arrey[key].set_piece(piece_selected)
                    break
            """clear/empty global variables : piece_selected, move_options
            game ready for next move (choose new piece to move)"""
            piece_selected = None
            current_move_options = None

    def on_release(self):
        """defines behaviour of game field when released"""
        if self.source == 'Images/light_field_pressed.png':
            self.source = 'Images/light_field.png'
        elif self.source == 'Images/dark_field_pressed.png':
            self.source = 'Images/dark_field.png'


game_arrey = {}
raw = 'A'
line = 1
x = 0
y = 0
color = 0
id = 1

for j in range(8):
    for i in range(8):
        current = raw + str(line)
        game_arrey[current] = field(x * 80, y, color)
        game_arrey[current].set_pos_id(id)
        id += 1
        x += 1
        raw = chr(ord(raw) + 1)
        color = not color
    line += 1
    raw = 'A'
    y += 80
    x = 0
    color = not color

# for debugging :
# print(game_arrey)
for key in game_arrey:
    print('debug : id - ', key, game_arrey[key].get_pos_id(), game_arrey[key].get_pos(), game_arrey[key].get_color())


def get_pos_by_index(index):
    for key in game_arrey:
        if game_arrey[key].get_pos_id() == index:
            return key
    return 0


def get_arrey_map():
    arrey_map = {}
    for key in game_arrey:
        arrey_map[game_arrey[key].get_pos_id()] = (key, game_arrey[key].get_pos(), game_arrey[key].get_piece_in_field())
    # for debugging :
    # print(arrey_map)
    return arrey_map


class RootWidget(FloatLayout):
    pass


class chess_board(App):
    def __init__(self):
        App.__init__(self)

    def build(self):
        A = RootWidget()
        for position in game_arrey:
            x = game_arrey[position].get_pos()[0]
            y = game_arrey[position].get_pos()[1]
            if game_arrey[position].get_color():
                self.spot = field(x, y, True)
                self.spot.pos = (x, y)
                self.spot.size_hint = (0.125, 0.125)
                A.add_widget(self.spot)
            else:
                self.spot = field(x, y, False)
                self.spot.pos = (x, y)
                self.spot.size_hint = (0.125, 0.125)
                A.add_widget(self.spot)

        # set all white pawns in staring position
        for position in game_arrey:
            if position.__contains__('2'):
                self.piece = GamePiece(source='Images/w_pawn.png')
                self.piece.size_hint = (0.120, 0.120)
                self.piece.pos = game_arrey[position].get_pos()
                game_arrey[position].set_piece(self.piece)
                A.add_widget(self.piece)

            # set all white rooks in staring position
            elif position in ('A1', 'H1'):
                self.piece = GamePiece(source='Images/w_rook.png')
                self.piece.size_hint = (0.120, 0.120)
                self.piece.pos = game_arrey[position].get_pos()
                game_arrey[position].set_piece(self.piece)
                A.add_widget(self.piece)

            # set all white knights in staring position
            elif position in ('B1', 'G1'):
                self.piece = GamePiece(source='Images/w_knight.png')
                self.piece.size_hint = (0.120, 0.120)
                self.piece.pos = game_arrey[position].get_pos()
                game_arrey[position].set_piece(self.piece)
                A.add_widget(self.piece)

            # set all white bishops in staring position
            elif position in ('C1', 'F1'):
                self.piece = GamePiece(source='Images/w_bishop.png')
                self.piece.size_hint = (0.120, 0.120)
                self.piece.pos = game_arrey[position].get_pos()
                game_arrey[position].set_piece(self.piece)
                A.add_widget(self.piece)

            # set white queen in staring position
            elif position == 'D1':
                self.piece = GamePiece(source='Images/w_queen.png')
                self.piece.size_hint = (0.120, 0.120)
                self.piece.pos = game_arrey[position].get_pos()
                game_arrey[position].set_piece(self.piece)
                A.add_widget(self.piece)

            # set white king in staring position
            elif position == 'E1':
                self.piece = GamePiece(source='Images/w_king.png')
                self.piece.size_hint = (0.120, 0.120)
                self.piece.pos = game_arrey[position].get_pos()
                game_arrey[position].set_piece(self.piece)
                A.add_widget(self.piece)

            # set all black pawns in staring position
            elif position.__contains__('7'):
                self.piece = GamePiece(source='Images/b_pawn.png')
                self.piece.size_hint = (0.120, 0.120)
                self.piece.pos = game_arrey[position].get_pos()
                game_arrey[position].set_piece(self.piece)
                A.add_widget(self.piece)

            # set all black rooks in staring position
            elif position in ('A8', 'H8'):
                self.piece = GamePiece(source='Images/b_rook.png')
                self.piece.size_hint = (0.120, 0.120)
                self.piece.pos = game_arrey[position].get_pos()
                game_arrey[position].set_piece(self.piece)
                A.add_widget(self.piece)

            # set all black knights in staring position
            elif position in ('B8', 'G8'):
                self.piece = GamePiece(source='Images/b_knight.png')
                self.piece.size_hint = (0.120, 0.120)
                self.piece.pos = game_arrey[position].get_pos()
                game_arrey[position].set_piece(self.piece)
                A.add_widget(self.piece)

            # set all black bishops in staring position
            elif position in ('C8', 'F8'):
                self.piece = GamePiece(source='Images/b_bishop.png')
                self.piece.size_hint = (0.120, 0.120)
                self.piece.pos = game_arrey[position].get_pos()
                game_arrey[position].set_piece(self.piece)
                A.add_widget(self.piece)

            # set black queen in staring position
            elif position == 'D8':
                self.piece = GamePiece(source='Images/b_queen.png')
                self.piece.size_hint = (0.120, 0.120)
                self.piece.pos = game_arrey[position].get_pos()
                game_arrey[position].set_piece(self.piece)
                A.add_widget(self.piece)

            # set black king in staring position
            elif position == 'E8':
                self.piece = GamePiece(source='Images/b_king.png')
                self.piece.size_hint = (0.120, 0.120)
                self.piece.pos = game_arrey[position].get_pos()
                game_arrey[position].set_piece(self.piece)
                A.add_widget(self.piece)

        return A


if __name__ == "__main__":
    chess_board().run()
