import pygame
from pygame.locals import *

# ゲームの初期化
pygame.init()

# 画面の大きさを設定
screen = pygame.display.set_mode((800, 600))

# 主人公のキャラクターを作成
character = pygame.Rect(400, 300, 30, 60)

# ゲームのループ
while True:
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    # キー入力の取得
    keys = pygame.key.get_pressed()
    # if keys[K_w]:
    #     character.y -= 1  # 上に移動
    # if keys[K_s]:
    #     character.y += 1  # 下に移動
    if keys[K_a]:
        character.x -= 1  # 左に移動
    if keys[K_d]:
        character.x += 1  # 右に移動

    # マウス入力の取得
    if pygame.mouse.get_pressed()[0]:
        pygame.draw.line(screen, (255, 255, 0), (character.x + character.width, character.y + character.height // 2), (800, character.y + character.height // 2), 2)

    # 画面を白で塗りつぶす
    screen.fill((255, 255, 255))

    # 主人公のキャラクターを描画
    pygame.draw.rect(screen, (255, 0, 0), character)

    # 画面の更新
    pygame.display.update()
