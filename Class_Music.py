import simpleaudio as sa
class Music():
    def __init__(self):
        self.sound_type = 'bouncing ball'
    def play():
        filename = 'Ping-pong-ball-bounce-sound-effect (1).wav'
        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()
        #play_obj.wait_done()


