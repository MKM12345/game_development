import pygame

class Game:
    def __init__(self, width, height, title):
        """
        Initialize a game with a window of the specified dimensions and title.
        :param width: Width of the window
        :param height: Height of the window
        :param title: Title of the window
        """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = False
        self.game_objects = []

    def add_game_object(self, game_object):
        """
        Add a game object to the game for rendering and updates.
        :param game_object: An instance of a game object (e.g., GameSprite)
        """
        self.game_objects.append(game_object)

    def handle_input(self):
        """
        Handle user input events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """
        Update game logic and game object states.
        """
        for game_object in self.game_objects:
            game_object.update()

    def draw(self):
        """
        Draw game objects on the screen.
        """
        self.screen.fill((0, 0, 0))
        for game_object in self.game_objects:
            game_object.draw(self.screen)
        pygame.display.update()

    def run(self):
        """
        Start the game loop.
        """
        self.running = True
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)

    def quit(self):
        """
        Quit the game and clean up resources.
        """
        pygame.quit()

class GameSprite:
    def __init__(self, x, y, width, height, image_path):
        """
        Initialize a game sprite with its position and image.
        :param x: X-coordinate of the sprite
        :param y: Y-coordinate of the sprite
        :param width: Width of the sprite
        :param height: Height of the sprite
        :param image_path: Path to the image file for the sprite
        """
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """
        Update the game sprite's state or perform logic (if needed).
        """
        pass

    def draw(self, screen):
        """
        Draw the sprite on the screen.
        :param screen: Pygame display surface
        """
        screen.blit(self.image, self.rect.topleft)

class Text:
    def __init__(self, text, x, y, font_size, color):
        """
        Initialize a text object with text, position, font size, and color.
        :param text: Text content
        :param x: X-coordinate of the text
        :param y: Y-coordinate of the text
        :param font_size: Font size
        :param color: Text color (e.g., (255, 255, 255) for white)
        """
        self.font = pygame.font.Font(None, font_size)
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        """
        Draw the text on the screen.
        :param screen: Pygame display surface
        """
        screen.blit(self.text, self.rect.topleft)

# Other functions for game development can be added to this module as needed.
