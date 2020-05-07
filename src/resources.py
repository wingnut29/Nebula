
import nebula

PATH, ERRORS = nebula.check_permissions()



# Ui Files
MAIN_WINDOW = "{}{}".format(PATH, "/ui/main.ui")


# Image Files
BACKGROUND = "{}{}".format(PATH, "/imgs/space_nebula.jpg")
WINDOW_ICON = "{}{}".format(PATH, "/imgs/nebula.png")
BTN_START = "{}{}".format(PATH, "/imgs/rocket.png")

# Data Files
DATA = "{}{}".format(PATH, "/backend/app_data.json")
