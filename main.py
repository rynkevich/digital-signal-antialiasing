import json
import sys
import matplotlib.pyplot as plt

from analysis import calculate_spectra
from antialiasing import moving_average_antialiasing, median_filter_antialiasing, parabolic_antialiasing
from plotter import plot_signal_and_spectra, plot_signal_antialiasing_and_spectra
from signal import N, test_signal


def main():
    data_path = sys.argv[1]
    variant = int(sys.argv[2])
    with open(data_path, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    data = data[variant - 1]
    moving_average_window_size = data['movingAverageWindowSize']
    median_filter_window_size = data['medianFilterWindowSize']

    signal_values = tuple(test_signal(i) for i in range(N))
    moving_average_antialiased_signal_values = moving_average_antialiasing(signal_values, moving_average_window_size)
    median_filter_antialiased_signal_values = median_filter_antialiasing(signal_values, median_filter_window_size)
    parabolic_antialised_signal_values = parabolic_antialiasing(signal_values)

    antialising_demo_data = [
        (parabolic_antialised_signal_values, '4', 'Fourth Degree Parabola'),
        (moving_average_antialiased_signal_values, '3', 'Median Filter'),
        (median_filter_antialiased_signal_values, '2', 'Moving Average')
    ]
    for data in antialising_demo_data:
        demonstrate_antialiased_signal(signal_values, *data)

    demonstrate_signal(signal_values)

    plt.show()


def demonstrate_signal(signal_values):
    plot_signal_and_spectra(signal_values, calculate_spectra(signal_values),
                            'Digital Signal Antialiasing (#1) - Original Signal')


def demonstrate_antialiased_signal(original_signal_values, antialiased_signal_values, figure_number, algorithm_name):
    spectra = calculate_spectra(antialiased_signal_values)
    plot_signal_antialiasing_and_spectra(original_signal_values, antialiased_signal_values, spectra,
                                         f'Digital Signal Antialiasing (#{figure_number}) - {algorithm_name}')


if __name__ == '__main__':
    main()
