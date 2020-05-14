import nebula

PATH, ERRORS = nebula.check_permissions()

# Ui Files
MAIN_WINDOW = "{}{}".format(PATH, "/ui/main.ui")
SPLASH = "{}{}".format(PATH, "/ui/splash.ui")

# Image Files
BACKGROUND = "{}{}".format(PATH, "/imgs/space_nebula.jpg")
WINDOW_ICON = "{}{}".format(PATH, "/imgs/nebula.png")
BTN_START = "{}{}".format(PATH, "/imgs/rocket.png")
RIGHT_ARROW = "{}{}".format(PATH, "/imgs/right_arrow.png")
LEFT_ARROW = "{}{}".format(PATH, "/imgs/left_arrow.png")
ROCKET = "{}{}".format(PATH, "/imgs/color_rocket.png")
EARTH = "{}{}".format(PATH, "/imgs/earth.png")

# Data Files
DATA = "{}{}".format(PATH, "/backend/app_data.json")
