def color_convertation(wave):

    if wave < 440 * 1e-9:
        red = -(wave - 440 * 1e-9) / (440 * 1e-9 - 380 * 1e-9)
        green, blue = 0, 1
    elif wave < 490 * 1e-9:
        red = 0
        green = (wave - 440 * 1e-9) / (490 * 1e-9 - 440 * 1e-9)
        blue = 1
    elif wave < 510 * 1e-9:
        red, green = 0, 1
        blue = -(wave - 510 * 1e-9) / (510 * 1e-9 - 490 * 1e-9)
    elif wave < 580 * 1e-9:
        red = (wave - 510 * 1e-9) / (580 * 1e-9 - 510 * 1e-9)
        green, blue = 1, 0
    elif wave < 645 * 1e-9:
        red = 1
        green = -(wave - 645 * 1e-9) / (645 * 1e-9 - 580 * 1e-9)
        blue = 0
    elif wave <= 780 * 1e-9:
        red, green, blue = 1, 0, 0

    return red, green, blue