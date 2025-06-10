import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像のsurface
    bg_img2 = pg.transform.flip(bg_img, True, False)
    # bg_img = pg.transform.scale(bg_img, (1600, 600))#バグる
    kk_img = pg.image.load("fig/3.png") #こうかとんのsurface
    kk_img = pg.transform.flip(kk_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200
        screen.blit(bg_img, [-x, 0])  #screenは10で作られる。blitしないと真っ黒になる。右の0をtmrにすると昇天する。
        screen.blit(bg_img2, [-x+1600, 0])  #2枚目
        screen.blit(bg_img, [-x+3200, 0]) #3枚目
        screen.blit(kk_img, [300, 200])  #screenのところをbg=imgにしても良い。
        pg.display.update()
        # print(tmr,x)
        tmr += 1        
        clock.tick(20000000) #FPS(?)の変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()