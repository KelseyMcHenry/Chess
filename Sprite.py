from PIL import Image
import pygame


class Sprite:

    def __init__(self, screen, width, height, screen_pos, sprite_filename):
        self.screen = screen
        self.screen_pos = screen_pos
        self.width_px = width
        self.height_px = height
        self.sprite_directory_path = r'C:\Users\d5ffpr\PycharmProjects\Chess\Sprites'
        self.sprite_path = self.sprite_directory_path + '\\' + sprite_filename

        # open image in PIL, convert to RGBA
        pil_img = Image.open(self.sprite_path)
        pil_img = pil_img.convert("RGBA")
        self.image = pygame.image.frombuffer(pil_img.tobytes(), pil_img.size, pil_img.mode)

        # scale image
        self.image = pygame.transform.scale(self.image, (self.width_px, self.height_px))

        # set the image's position on the screen
        self.image_rectangle = self.image.get_rect()
        self.image_rectangle.topleft = self.screen_pos

    def get_screen_pos(self):
        return self.screen_pos

    def set_screen_pos(self, newpos):
        self.screen_pos = newpos
        self.image_rectangle.topleft = self.screen_pos

    def get_width(self):
        return self.width_px

    def get_height(self):
        return self.height_px

    def get_image_path(self):
        return self.sprite_path

    def set_image(self, image):
        self.image = image
        # update image rectangle and image's screen position
        self.image_rectangle = self.image.get_rect()
        self.image_rectangle.topleft = self.screen_pos

    def blit(self):
        self.screen.blit(self.image, self.image_rectangle)

    def get_screen(self):
        return self.screen


class ChessBoard(Sprite):
    def __init__(self, screen, width, height, screen_pos, sprite_filename):
        self.highlighted = []
        Sprite.__init__(self, screen, width, height, screen_pos, sprite_filename)

    def render(self):
        self.blit()

    def render_highlights(self):
        for pos in self.highlighted:
            rank = pos[0]
            file = pos[1]
            pygame.draw.rect(self.screen, (255,0,0), (65 * (ord(rank) - 97) + 28, 65 * (8-file) + 28, 65, 65), 3)

    def rank_file_from_pos(self, position):
        rank = chr(((position[0] - 28) // 65) + 97)
        file = -((position[1] - 28) // 65) + 8
        if rank in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] and file > 0 and file < 9:
            return rank, file
        else:
            return None

    def clear_highlights(self):
        self.highlighted = []

    def set_highlighted(self, rank, file):
        self.highlighted.append((rank, file))

    def get_highlighted(self):
        return self.highlighted


class ChessPiece(Sprite):

    def __init__(self, screen, color, type, rank, file):
        self.rank = rank.lower()
        self.file = file
        self.color = color.lower()
        self.type = type.lower().capitalize()
        width = 50
        height = 50
        screen_pos = (65 * (ord(self.rank) - 97) + 28 + 7, 65 * (8-self.file) + 28 + 5)
        sprite_filename = self.color + self.type + '.png'
        Sprite.__init__(self, screen, width, height, screen_pos, sprite_filename)
        self.type = type.lower()

    def __repr__(self):
        return f'{self.color} {self.type} at {self.rank}{self.file}'

    def __eq__(self, other):
        return self.rank == other.rank and self.file == other.file and self.color == other.color and self.type == other.type

    def get_type(self):
        return self.type

    def get_color(self):
        return self.color

    def get_rank(self):
        return self.rank

    def get_file(self):
        return self.file

    def set_position(self, rank, file):
        self.rank = rank
        self.file = file
        screen_pos = (65 * (ord(self.rank) - 97) + 28 + 7, 65 * (8 - self.file) + 28 + 5)
        self.set_screen_pos(screen_pos)
