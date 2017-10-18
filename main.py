alien = Actor('alien')

WIDTH = 500 + alien.width
HEIGHT = alien.height + 200

alien.pos = WIDTH/2, HEIGHT/2

def draw():
    screen.clear()
    screen.fill((0,0,128))
    alien.draw()
    
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
