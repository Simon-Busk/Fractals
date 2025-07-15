import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms
from matplotlib.widgets import Slider, RadioButtons

length = 200
height = math.sqrt(length**2 -  (length/2)**2)
scale_factor = 0.5
offsets = [(0,0), (100, 0), (50, height/2)]

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2, left=0.3)

def draw_fractal(iterations, shape_type):
    #Clear the old fractal
    ax.clear()

    #Choose starting shape
    shapes = {
        'Triangle': [[0, 0], [length, 0], [length / 2, height]],
        'Square': [[0, 0], [length, 0], [length, height], [0, height]]
    }
    vertices = shapes[shape_type]

    transforms_list = [transforms.Affine2D()]

    for i in range(iterations):
        new_transforms = []
        for tform in transforms_list:
            for dx, dy in offsets:
                # Create new transform: scale and translate from current transform
                new_t = transforms.Affine2D().scale(scale_factor).translate(dx, dy)
                new_transforms.append(new_t + tform)

        transforms_list = new_transforms  # Update for next iteration

    for tform in transforms_list:
        triangle = patches.Polygon(vertices, closed=True, edgecolor='black', facecolor='skyblue', alpha=0.5)
        triangle.set_transform(tform + ax.transData)
        ax.add_patch(triangle)

    ax.set_xlim(0,210)
    ax.set_ylim(0,200)
    ax.axis('off')
    ax.set_aspect('equal')

    #Makes sure to redraw
    fig.canvas.draw_idle()

# Initial draw
draw_fractal(3, 'Triangle')

# Slider axis and slider
ax_slider = plt.axes((0.25, 0.05, 0.5, 0.03))
ax_radio = plt.axes((0.05, 0.5, 0.2, 0.15))
slider = Slider(ax_slider, 'Iterations', 0, 6, valinit=3, valstep=1)
radio = RadioButtons(ax_radio, ('Triangle', 'Square'))

# Update function
def update(_=None):
    iterations = int(slider.val)
    shape_type = radio.value_selected
    draw_fractal(iterations, shape_type)

slider.on_changed(update)
radio.on_clicked(update)

plt.show()
