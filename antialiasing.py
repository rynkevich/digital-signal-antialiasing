from statistics import mean

DEFAULT_ELEMENTS_TO_REMOVE = 1
DEFAULT_PARABOLA_COEFFS = (5, -30, 75, 131, 75, -30, 5)
DEFAULT_PARABOLA_OUTER_COEFF = 1 / 231


def moving_average_antialiasing(signal_values, window_size):
    m = (window_size - 1) // 2
    time_range = range(len(signal_values))
    return [mean(signal_values[j] for j in range(i - m, i + m) if j in time_range) for i in time_range]


def median_filter_antialiasing(signal_values, window_size, elements_to_remove=DEFAULT_ELEMENTS_TO_REMOVE):
    half_window_size = (window_size - 1) // 2

    def calculate_antialiased(i):
        window = (signal_values[m] for m in range(i - half_window_size, i + half_window_size) if m in range(len(signal_values)))
        selected_values = sorted(window)[elements_to_remove:-elements_to_remove]
        return mean(selected_values) if selected_values else 0

    return [calculate_antialiased(i) for i in range(len(signal_values))]


def parabolic_antialiasing(signal_values, coeffs=DEFAULT_PARABOLA_COEFFS, outer_coeff=DEFAULT_PARABOLA_OUTER_COEFF):
    half_coeffs_size = len(coeffs) // 2

    def calculate_antialiased(i):
        result = 0
        for coefficient_index, offset in enumerate(range(-half_coeffs_size, half_coeffs_size + 1)):
            value_index = i + offset
            result += (coeffs[coefficient_index] * signal_values[value_index]) if value_index in range(len(signal_values)) else 0
        return result * outer_coeff

    return [calculate_antialiased(i) for i in range(len(signal_values))]
