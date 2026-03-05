import matplotlib.pyplot as plt
import keyboard
from bubble_sort import bubble_sort
from get_rand_numbers_list import get_rand_number_list

ANIMATION_STEPS = 10


def main():
    y_values = get_rand_number_list(500)
    x_positions = list(range(len(y_values)))

    plt.ion()
    figure, axis = plt.subplots()

    bars = axis.bar(x_positions, y_values)
    axis.set_title('Simple Bar Chart')
    axis.set_xlabel('Categories')
    axis.set_ylabel('Values')

    for state, idx1, idx2 in bubble_sort(y_values):
        if keyboard.is_pressed('q'):
            plt.close(figure)
            break

        old_h1 = bars[idx1].get_height()
        old_h2 = bars[idx2].get_height()
        new_h1 = state[idx1]
        new_h2 = state[idx2]

        for step in range(1, ANIMATION_STEPS + 1):
            t = step / ANIMATION_STEPS
            bars[idx1].set_height(old_h1 + t * (new_h1 - old_h1))
            bars[idx2].set_height(old_h2 + t * (new_h2 - old_h2))
            figure.canvas.draw_idle()
            plt.pause(0.001)

    plt.ioff()


if __name__ == "__main__":
    main()
