spider = Actor('cartwheelingspider')

WIDTH = 500
HEIGHT = spider.height + 200

spider.pos = 200, 200


def draw():
    screen.clear()
    spider.draw()