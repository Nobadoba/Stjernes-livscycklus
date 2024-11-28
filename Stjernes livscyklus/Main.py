import pygame
# Astronomi halløj
pygame.init()
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
font_title = pygame.font.SysFont("Courier", 40)
font_text = pygame.font.SysFont("Courier", 20)

bodies = [
    ['StellarNursery', 'Stjernestøv', 'blablablablablablabla'],
    ['SmallSun', 'Lille Sol', 'blablablablablablabla'],
    ['LargeSun', 'Stor Sol', 'blablablablablablabla'],
    ['RedGiant', 'Rød Kæmpe', 'blablablablablablabla'],
    ['RedSuperGiant', 'Rød Superkæmpe', 'blablablablablablabla'],
    ['PlanetaryNebula', 'Planetarisk tåge', 'blablablablablablabla'],
    ['WhiteDwarf', 'Hvid Dværg', 'blablablablablablabla'],
    ['BlackDwarf', 'Sort Dværg', 'blablablablablablabla'],
    ['Supernova', 'Supernova', 'blablablablablablabla'],
    ['BlackHole', 'Sort Hul', 'blablablablablablabla'],
    ['Xray', 'X-ray', 'blablablablablablabla'],
    ['NeutronStar', 'Neutron Stjerne', 'blablablablablablabla'],
    ['Pulsar', 'Pulsar', 'blablablablablablabla']
]


class Scene1:
    def __init__(self, img):
        self.lst = []
        self.img = pygame.transform.scale(pygame.image.load('graphics/'+img+'.jpg').convert_alpha(), (200, 200))
        self.img_rect = self.img.get_rect()
        self.img_rect.center = (screen_width / 4, screen_height / 2)
        for i in bodies:
            if img == bodies[bodies.index(i)][0]:
                self.title = bodies[bodies.index(i)][1]
                self.text = bodies[bodies.index(i)][2]
                self.title_render = font_title.render(self.title, True, 'white')
                self.text_render = font_text.render(self.text, True, 'white')

    def click(self):
        return [self.img_rect, 0]

    def show(self):
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, screen_width, screen_height))
        screen.blit(self.img, self.img_rect)
        screen.blit(font_text.render('Klik på billedet for at gå videre', True, 'white'),
                    (screen_width/4-100, screen_height-screen_height/4))
        screen.blit(self.title_render, (screen_width / 4 + 100, 10))
        screen.blit(self.text_render, (screen_width / 4 + 150, screen_height/2 - 100))


class Scene2:
    def __init__(self, img1, img2):
        self.img1 = pygame.transform.scale(pygame.image.load('graphics/'+img1+'.jpg').convert_alpha(), (200, 200))
        self.img1_rect = self.img1.get_rect()
        self.img1_rect.center = (screen_width - screen_width / 4, screen_height / 2)

        for i in bodies:
            if img1 == bodies[bodies.index(i)][0]:
                self.title1 = bodies[bodies.index(i)][1]
                self.text1 = bodies[bodies.index(i)][2]
                self.text1_render = font_text.render(self.text1, True, 'white')
                self.title1_render = font_title.render(self.title1, True, 'white')

            if img2 == bodies[bodies.index(i)][0]:
                self.title2 = bodies[bodies.index(i)][1]
                self.text2 = bodies[bodies.index(i)][2]
                self.text2_render = font_text.render(self.text2, True, 'white')
                self.title2_render = font_title.render(self.title2, True, 'white')

        self.img2 = pygame.transform.scale(pygame.image.load('graphics/'+img2+'.jpg').convert_alpha(), (200, 200))
        self.img2_rect = self.img2.get_rect()
        self.img2_rect.center = (screen_width / 4, screen_height / 2)

    def show(self):
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, screen_width, screen_height))

        screen.blit(self.img1, self.img1_rect)
        screen.blit(self.title1_render, ((screen_width - screen_width / 4)-100, 75))
        screen.blit(self.text1_render, ((screen_width - screen_width / 4)-100, screen_height/2 + 110))

        screen.blit(self.img2, self.img2_rect)
        screen.blit(self.title2_render, (screen_width / 4 - 100, 75))
        screen.blit(self.text2_render, (screen_width / 4 - 100, screen_height / 2 + 110))

        screen.blit(font_text.render('Klik på et billede for at gå videre', True, 'white'),
                    (screen_width / 4, screen_height - screen_height / 9))

    def click(self):
        if pygame.mouse.get_pos()[0] >= screen_width/2:
            print(1)
            return [self.img1_rect, 1]
        else:
            print(2)
            return [self.img2_rect, 2]


scene0 = Scene1('StellarNursery')
scene1 = Scene2('SmallSun', 'LargeSun')
scene1a = Scene1('RedGiant')
scene2a = Scene1('PlanetaryNebula')
scene3a = Scene1('WhiteDwarf')
scene4a = Scene1('BlackDwarf')
scene1b = Scene1('RedSuperGiant')
scene2b = Scene1('Supernova')
scene3b = Scene2('BlackHole', 'NeutronStar')
scene1c = Scene1('Pulsar')
scene1d = Scene1('Xray')

scenes = [scene0, scene1]
path1 = [scene1a, scene2a, scene3a, scene4a]
path2 = [scene1b, scene2b, scene3b, scene1c, scene1d]
cur_scene = scenes
ind = [0]

while True:
    if cur_scene[ind[-1]] != scene3b or cur_scene[ind[-1]] != scene4a:
        current_scene = cur_scene[ind[-1]]
    current_scene.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if cur_scene[ind[-1]]  != path1[-1] or cur_scene[ind[-1]] != path2[-1]:
            if (event.type == pygame.MOUSEBUTTONDOWN):
                x, y = event.pos
                if current_scene.click()[0].collidepoint(x, y):
                    ind.append(len(ind)-1+1)
                    if current_scene.click()[1] == 1:
                        cur_scene = path1
                        ind.clear()
                        ind = [0]
                    if current_scene.click()[1] == 2:
                        cur_scene = path2
                        ind.clear()
                        ind = [0]
    pygame.display.flip()
