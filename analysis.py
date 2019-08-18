from math import pi, cos, sin


def calculate_spectra(sampled_signal):
    amplitude_spectrum, phase_spectrum = [], []
    for harmonic_index in range(len(sampled_signal)):
        an, bn = fourier_coefficients(sampled_signal, harmonic_index)
        amplitude_spectrum.append(an)
        phase_spectrum.append(bn)
    return amplitude_spectrum, phase_spectrum


def fourier_coefficients(sampled_signal, harmonic_index):
    big_n = len(sampled_signal)
    an, bn = 0, 0
    for i, signal_value in enumerate(sampled_signal):
        angle = 2 * pi * i * harmonic_index / big_n
        an += signal_value * cos(angle)
        bn += signal_value * sin(angle)
    an *= 2 / big_n
    bn *= 2 / big_n
    return an, bn
