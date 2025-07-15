import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms

def get_iterations():
    while True:
        try:
            iterations = int(input("Number of iterations: "))
            if iterations < 0:
                print("Please enter a number greater than or equal to 0.")
            else:
                return iterations
        except ValueError:
            print("Please input a whole number.")

def get_shape_type():
    while True:
        shape = input("Enter starting shape, 'S' for Square and 'T' for triangle: ").lower()
        if shape in ('s', 't'):
            return shape
        print("Please enter a valid shape ('S' or 'T').")


def draw_fractal(ax, iteration, shape_type):
    length = 200
    height = math.sqrt(length ** 2 - (length / 2) ** 2)
    scale_factor = 0.5
    offsets = [(0, 0), (100, 0), (50, height / 2)]

    shapes = {
        't': [[0, 0], [length, 0], [length / 2, height]],
        's': [[0, 0], [length, 0], [length, height], [0, height]]
    }

    vertices = shapes[shape_type]
    all_transforms = [transforms.Affine2D()]
    current_transforms = [transforms.Affine2D()]


    for i in range(iteration):
        new_transforms = []
        for tform in current_transforms:
            for dx, dy in offsets:
                # Create new transform: scale and translate from current transform
                new_t  = transforms.Affine2D().scale(scale_factor).translate(dx, dy) + tform
                # Move the transform so it gets pictured next to the old one
                moved  = new_t + transforms.Affine2D().translate(200 , 0)
                new_transforms.append(moved)

        current_transforms = new_transforms  # Update for next iteration
        all_transforms.extend(new_transforms)

    for tform in all_transforms:
        triangle = patches.Polygon(vertices, closed=True, edgecolor='black', facecolor='black')
        triangle.set_transform(tform + ax.transData)
        ax.add_patch(triangle)

    ax.set_xlim(0,200 * (iteration + 1))
    ax.set_ylim(0,200)
    ax.axis('off')
    ax.set_aspect('equal')

def main():
    iterations = get_iterations()
    shape = get_shape_type()

    fig, ax = plt.subplots()
    draw_fractal(ax, iterations, shape)
    plt.show()

main()