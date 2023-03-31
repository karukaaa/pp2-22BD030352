import pygame

pygame.init()
running = True

number_song = 0
music_playing = True
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

playlist = ['budapest.mp3', 'morning.mp3']

song_end = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(song_end)


def play_song(number):
    pygame.mixer.music.load(playlist[number])
    pygame.mixer.music.play()


play_song(number_song)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == song_end:
            if number_song == len(playlist)-1:
                number_song = 0
            else:
                number_song += 1
            play_song(number_song)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if number_song == len(playlist) - 1:
                    number_song = 0
                else:
                    number_song += 1
                play_song(number_song)

            elif event.key == pygame.K_LEFT:
                if number_song == 0:
                    number_song = len(playlist) - 1
                else:
                    number_song -= 1
                play_song(number_song)

            if event.key == pygame.K_SPACE:
                if music_playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                music_playing = not music_playing

clock.tick(10)
pygame.display.flip()
