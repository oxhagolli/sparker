import pygame
import math
import time

car_height = 301
car_width = 167

def rotate_image(surface, angle, pivot, offset):
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)
    rotated_offset = offset.rotate(angle)
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    run = True

    # Update background:
    bg_img = pygame.image.load("parkinglot.png")

    # Load car image
    car_original = pygame.image.load("car.png")
    screen.blit(bg_img, (0, 0))
    car_x, car_y, car_theta = 600, 320, 0
    d_theta = 0
    dy,dx = 1,0
    pivot= [83, 300]
    offset = pygame.math.Vector2(150, 83)

    while run:
        # Redraw background
        screen.blit(bg_img, (0, 0))
        # Draw car:
        #car = pygame.transform.rotate(car_original, car_theta)
        #screen.blit(car, (car_x, car_y))

        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_UP]:
            car_theta -= d_theta
            car_y -= dy*abs(math.cos(math.radians(car_theta)))
            car_x -= dy*abs(math.sin(math.radians(car_theta)))
        if keys[pygame.K_DOWN]:
            car_theta += d_theta
            car_y += dy*abs(math.cos(math.radians(car_theta)))
            car_x += dy*abs(math.sin(math.radians(car_theta)))
        if keys[pygame.K_LEFT]:
            d_theta += 0.1
            d_theta = min(d_theta,1)
            print(d_theta)
        if keys[pygame.K_RIGHT]:
            d_theta -= 0.1
            d_theta = max(d_theta,-1)
            print(d_theta)
        if keys[pygame.K_SPACE]:
            d_theta = 0


        rotated_image, rect = rotate_image(car_original, car_theta, [car_x, car_y], offset)
        screen.blit(rotated_image, rect)

        # Frame update
        time.sleep(0.003)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



if __name__ == "__main__":
    main()
