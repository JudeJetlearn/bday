import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Greating Card")

img = pygame.image.load("bday.jpg")
img2 = pygame.image.load("cake.jpg")
img3 = pygame.image.load("present.jpg")
image = pygame.transform.scale(img, (WIDTH,HEIGHT))
image2 = pygame.transform.scale(img2, (WIDTH,HEIGHT))
image3 = pygame.transform.scale(img3, (WIDTH,HEIGHT))

while(True):
    font = pygame.font.SysFont("Times New Roman",72)
    text = font.render("Happy",True,(0,0,0))
    text2 = font.render("Birthday",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image,(0,0))
    display_surface.blit(text,(210,180))
    display_surface.blit(text2,(180,264))
    pygame.display.update()
    time.sleep(2)

    font = pygame.font.SysFont("Times New Roman",72)
    text1 = font.render("Good",True,(0,0,0))
    text22 = font.render("Luck",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image2,(0,0))
    display_surface.blit(text1,(210,180))
    display_surface.blit(text22,(180,264))
    pygame.display.update()
    time.sleep(2)

    font = pygame.font.SysFont("Times New Roman",72)
    text12 = font.render("Good",True,(0,0,0))
    text23 = font.render("Luck",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image3,(0,0))
    display_surface.blit(text12,(210,180))
    display_surface.blit(text23,(180,264))
    pygame.display.update()
    time.sleep(2)