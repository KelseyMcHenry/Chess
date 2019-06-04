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


class ChessPiece(Sprite):

    def __init__(self, screen, color, type, rank, file):
        self.rank = rank
        self.file = file
        self.color = color
        self.type = type
        width = 50
        height = 50
        rank = rank.lower()
        screen_pos = (65 * (ord(rank) - 97) + 28 + 7, 65 * (8-file) + 28 + 5)
        sprite_filename = color + type + '.png'
        Sprite.__init__(self, screen, width, height, screen_pos, sprite_filename)

