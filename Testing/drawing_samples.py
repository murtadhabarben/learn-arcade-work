import arcade

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Platformer"
SCREEN_COLOR = arcade.csscolor.AQUA


def draw_tree(position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), scale=1):
    x, y = position
    s = scale
    arcade.draw_rectangle_filled(x, y, 10 * s, 30 * s, arcade.csscolor.BROWN)

    arcade.draw_circle_filled(x, y + 30 * s, 20 * s, arcade.csscolor.FOREST_GREEN)


def draw_trees(number=5, camera_pos=(0, 0)):
    # d is distance between two trees in pixel
    d = 10
    for i in range(1, number):
        draw_tree((100 + d, 20 + d), 1)
    for i in range(1, 5):
        draw_tree((400 - d, 20 + d), 1)


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.set_background_color(SCREEN_COLOR)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 500, 150, 0, arcade.csscolor.GREEN)

draw_trees()

arcade.finish_render()

arcade.run()
