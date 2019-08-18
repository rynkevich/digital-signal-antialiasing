import matplotlib.pyplot as plt


def plot_signal_and_spectra(signal_values, spectra, window_title):
    fig, axes = plt.subplots(3)
    fig.canvas.set_window_title(window_title)

    amplitude_spectrum, phase_spectrum = spectra

    set_ax_title(axes[0], 'Signal')
    axes[0].plot(signal_values)

    set_ax_title(axes[1], 'Amplitude Spectrum')
    axes[1].stem(amplitude_spectrum, markerfmt=' ', use_line_collection=True)

    set_ax_title(axes[2], 'Phase Spectrum')
    axes[2].stem(phase_spectrum, markerfmt=' ', use_line_collection=True)

    plt.subplots_adjust(hspace=1)


def plot_signal_antialiasing_and_spectra(original_signal_values, antialiased_signal_values,
                                         antialiased_signal_spectra, window_title):
    fig, axes = plt.subplots(3)
    fig.canvas.set_window_title(window_title)

    amplitude_spectrum, phase_spectrum = antialiased_signal_spectra

    set_ax_title(axes[0], 'Signals')
    axes[0].plot(original_signal_values, label='Original')
    axes[0].plot(antialiased_signal_values, label='Antialiased')
    axes[0].legend(loc=3, prop={'size': 9})

    set_ax_title(axes[1], 'Amplitude Spectrum (antialiased)')
    axes[1].stem(amplitude_spectrum, markerfmt=' ', use_line_collection=True)

    set_ax_title(axes[2], 'Phase Spectrum (antialiased)')
    axes[2].stem(phase_spectrum, markerfmt=' ', use_line_collection=True)

    plt.subplots_adjust(hspace=1)


def set_ax_title(ax, title):
    ax.set_title(title, pad='15', fontsize='10')
