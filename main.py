import matplotlib.pyplot as plt
import random
import keyboard
from bubble_sort import bubble_sort
from get_rand_numbers_list import get_rand_number_list


def main():
    y_values = get_rand_number_list(500)
    x_positions = list(range(len(y_values)))

    plt.ion()
    figure, axis = plt.subplots()

    bars = axis.bar(x_positions, y_values)
    axis.set_title('Simple Bar Chart')
    axis.set_xlabel('Categories')
    axis.set_ylabel('Values')

    while True:
        if keyboard.is_pressed('q'):
            plt.close(figure)
            break

        #random.shuffle(y_values)
        y_values = bubble_sort(y_values)

        for bar, new_height in zip(bars, y_values):
            bar.set_height(new_height)
            
        figure.canvas.draw_idle()
        plt.pause(.01)
    
    plt.ioff()
    
if __name__ == "__main__":
    main()


