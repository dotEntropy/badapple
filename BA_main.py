import sys, os
file_path = os.path.dirname(__file__)
pygame_path = os.path.join(file_path, 'pygame')
sys.path.insert(0, pygame_path)

import pygame


class Main:
    def __init__(self) -> None:
        self.FPS = 30
        self.FRAME_SKIP = 1 
        self.TOTAL_FRAMES = 6569
        self.OUTPUT_DETAILS = f"[client] fps:{self.FPS} skip:{self.FRAME_SKIP}"
        self.clock = pygame.time.Clock()
        self.initialize_music()

    @staticmethod
    def initialize_music() -> None:
        music_path = os.path.join(file_path, 'res', 'BA.wav')
        pygame.mixer.init()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.1)
    
    def load_frame(self, frame_index: int) -> str:
        frame_path = os.path.join(file_path, 'res', f'BA{frame_index}.txt')
        with open(frame_path) as file:
            return file.read()

    def run(self) -> None:
        pygame.mixer.music.play()
        for frame_index in range(1, self.TOTAL_FRAMES + 1, self.FRAME_SKIP):
            self.clock.tick(self.FPS)
            frame = self.load_frame(frame_index)
            print(f"{frame}{self.OUTPUT_DETAILS} frame:{frame_index}/{self.TOTAL_FRAMES}", end='')
    

if __name__ == '__main__':
    main = Main()
    input("[Press enter to start]\n")
    try:
        main.run()
    except KeyboardInterrupt:
        pass
    pygame.mixer.music.stop()
    pygame.quit()
