import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        #need to override
        pass

    def update(self, dt):
        #need to override
        pass

    def collison_check(self, circleShapeObj):
        return self.position.distance_to(circleShapeObj.position) <= self.radius + circleShapeObj.radius