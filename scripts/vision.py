from PIL import ImageGrab


def take_screenshot(file_name):
    screenshot = ImageGrab.grab()
    screenshot.save(f"{file_name}.png", "PNG")
