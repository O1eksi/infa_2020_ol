import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30

# SIZE_X - height
SIZE_X = 1000
# SIZE_Y - width
SIZE_Y = 800

screen = pygame.display.set_mode((SIZE_Y, SIZE_X))

BACKGROUND_COLOR = (170, 255, 230)
BACKGROUND = rect(screen, BACKGROUND_COLOR, (0, 0, SIZE_Y, SIZE_X))


def face(size_x, size_y):
    """
    draws a smiley in the middle of the given coordinates (dimensions)
    :param size_x: input your height
    :param size_y: input your width

    """
    # smiley radius is calculated relative to the smaller size (size_x or size_y)
    radius = (min(size_x, size_y))*0.3
    # calculate coordinates of the center circle
    centr_x = size_x/2
    centr_y = size_y/2
    #draw circle and perimeter
    circle(screen, (255, 255, 0), (centr_y, centr_x), radius)
    circle(screen, (0, 0, 0), (centr_y, centr_x), radius, 1)

    mouth(centr_x, centr_y, radius)

    eyes(centr_x, centr_y, radius)


def mouth(centr_x, centr_y, radius):
    """
    draws a rectangle (mouth) at coordinates (centr_x, centr_y),
    the radius is used to compute the dimensions of the rectangle
    :param centr_x: center coordinate x
    :param centr_y: center coordinate x
    :param radius: length of the rectangle
    """

    start_y = centr_y - radius*0.5
    start_x = centr_x + radius/2
    fin_y = radius
    fin_x = radius/5
    rect(screen, (0, 0, 0), (start_y, start_x, fin_y, fin_x))


def eyes(centr_x, centr_y, radius):
    right_x = centr_x - radius/4
    right_y = centr_y - radius/2
    right_radius_iris = radius*0.2

    radius_pupil = radius*0.08

    left_x = right_x
    left_y = centr_y + radius/2
    left_radius_iris = radius*0.1

    draw_eye(right_x, right_y, right_radius_iris, radius_pupil, centr_y, centr_x, radius)
    draw_eye(left_x, left_y, left_radius_iris, radius_pupil, centr_y, centr_x, radius)

def draw_eye(eye_centr_x, eye_centr_y, radius_iris, radius_pupil, centr_y, centr_x, radius):
    eye_iris = circle(screen, (255, 0, 0), (eye_centr_y, eye_centr_x), radius_iris)
    eye_iris = circle(screen, (0, 0, 0), (eye_centr_y, eye_centr_x), radius_iris, 1)
    eye_pupil = circle(screen, (0, 0, 0), (eye_centr_y, eye_centr_x), radius_pupil)

    eyebrows(centr_y, centr_x, eye_centr_x, eye_centr_y, radius_pupil, radius_iris, radius)


def eyebrows(centr_y, centr_x, eye_centr_x, eye_centr_y, radius_pupil, radius_iris, radius):
    if centr_y > eye_centr_y: #right eye
        start_x = eye_centr_x - radius_pupil
        start_y = eye_centr_y + radius/3
        tg_al = (radius_iris - radius_pupil) /(start_y - eye_centr_y)
        hypotenuse = radius
        fin_y = start_y - ((hypotenuse**2)/(tg_al**2 + 1))**0.5
        fin_x = start_x - (hypotenuse**2 - (hypotenuse**2)/(tg_al**2 + 1))**0.5

        eyebrow = polygon(screen, (0, 0, 0), [(start_y,start_x), (fin_y,fin_x)], math.ceil(radius*0.1))
    else:
        start_x = eye_centr_x - radius_pupil
        start_y = eye_centr_y - radius / 3
        tg_al = (radius_iris - radius_pupil) / (start_y - eye_centr_y)
        hypotenuse = radius
        fin_y = start_y + ((hypotenuse ** 2) / (tg_al ** 2 + 1)) ** 0.5
        fin_x = start_x - (hypotenuse ** 2 - (hypotenuse ** 2) / (tg_al ** 2 + 1)) ** 0.5

        eyebrow = polygon(screen, (0, 0, 0), [(start_y, start_x), (fin_y, fin_x)], math.ceil(radius * 0.1))



face(SIZE_X, SIZE_Y)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
