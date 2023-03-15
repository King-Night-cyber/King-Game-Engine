import ctypes
user32 = ctypes.windll.user32

WIDTH, HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

FPS = 140