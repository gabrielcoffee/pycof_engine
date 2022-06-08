from pygame import Surface, Rect, Vector2

class AnimatedSprite():
    def __init__(self,
                 spritesheet : Surface,
                 start_rect : Rect,
                 total_frames,
                 frames_persec,
                 is_loop = True,
                 is_back_and_forth = False,
                 cur_frame = 0,
                 running = True
                 ):

        self.images = []
        self.dim = Vector2(start_rect.width, start_rect.height)
        for frame in range(total_frames):
            self.images.append(spritesheet.subsurface(
                start_rect.x + (start_rect.width * frame),
                start_rect.y,
                start_rect.width,
                start_rect.height))

        self.total_frames = total_frames
        self.frames_persec = frames_persec
        self.is_loop = is_loop
        self.is_back_and_forth = is_back_and_forth
        self.cur_frame = cur_frame
        self.running = running

        self.frame_add = 1
        self.timer = 0

    def update(self):
        if self.running == False:
            return

        self.timer += 1
        if self.timer >= 60 / self.frames_persec:
            self.timer = 0
            self.cur_frame += self.frame_add

            if self.cur_frame >= self.total_frames or self.cur_frame < 0:
                if self.is_loop and not self.is_back_and_forth:
                    self.cur_frame = 0
                elif self.is_back_and_forth:
                    self.frame_add *= -1
                    self.cur_frame += self.frame_add*2
                else:
                    self.cur_frame = self.total_frames-1
                    self.running = False

    def draw(self, x, y, screen, cam_offset):

        # draw current frame animation with source width and height
        screen.blit(
            self.images[self.cur_frame],
            Vector2(x, y) - cam_offset)