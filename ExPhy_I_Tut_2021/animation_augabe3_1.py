import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation

def x(t, epsilon, l) -> np.ndarray:
    """
    berechnet den herunterhängenden Teil des Seils zum Zeitpunkt t

    Args:
        t: Zeit in Sekunden
        epsilon: Anfangsbedingung, x(t=0)=espsilon in Metern
        l: Länge des Seils in Metern
    """
    g = 9.81 # m/s^2
    tau = math.sqrt(l/g)
    return epsilon * np.cosh(t/tau)

def init() -> [Line2D, Line2D]:
    """
    initialisert leere Linie

    Args:
        None
    Returns:
        [Line2D, Line2D]: list of lines to plot
    """
    line1.set_data([1-(l-epsilon), 1], [z0, z0])
    line2.set_data([1, 1], [z0-epsilon, z0])
    return line1, line2

def update_im(n: int) -> [Line2D, Line2D]:
    """
    Plottet das System im n. Zeitschritt,
    also zum Zeitpukt n * dt

    Args:
        n: Nummer des Zeitschritts
    Returns:
        [Line2D, Line2D]: list of lines to plot
    """

    # Zeit
    t = n * dt

    # Titel aktualisieren mit aktueller Zeit
    title.set_text(r'$t = %.*f$ s'%(2, t))

    # aktueller Wert x(t)
    x_t = x(t, epsilon, l)

    if x_t < l:
        # Falls x_t < l, plotte beide Linien

        # Länge auf Tisch:
        l_tisch = l - x_t
        line1.set_data([1-l_tisch, 1], [z0,z0])

        # Länge herunterhängend
        line2.set_data([1, 1], [z0-x_t, z0])
    else:
        # Wenn x_t >= l, ist das Seil vom Tisch heruntergerutscht
        # -> plotte nur senkrechte Linie
        line1.set_data([], [])
        line2.set_data([1, 1], [z0-x_t, z0-x_t+l])
    return line1, line2


if __name__ == '__main__':
    # Definition der Variablen
    epsilon = .01 #in m
    l = 1 # in m
    dt = 0.01 # in s, Zeit

    fig, ax = plt.subplots(figsize=(7,4))
    fig.suptitle("Magie der reibungsfreien Welt")

    # z-koordinate des auf dem Tisch liegenden Seils
    z_tisch = 1.5
    z0 = z_tisch + .03

    # Tisch plotten
    ax.plot([0, 0], [0, z_tisch], c='black', zorder=11, lw=5)
    ax.plot([2, 2], [0, z_tisch], c='black', zorder=11, lw=5)
    ax.plot([-.5, .95], [z_tisch, z_tisch], c='black', zorder=11, lw=5)
    ax.plot([1.05, 2.5], [z_tisch, z_tisch], c='black', zorder=11, lw=5)
    # label etc.
    ax.set_xlabel(r'$x$ [m]')
    ax.set_ylabel(r'$z$ [m]')
    ax.set_xlim(-.6, 2.6)
    ax.set_ylim(0, 1.6)
    title = ax.set_title('')

    line1, = ax.plot([], [], lw=5, c='red')
    line2, = ax.plot([], [], lw=5, c='red')

    anim = FuncAnimation(fig, update_im, blit=True, init_func=init,
                        frames=180, interval=10)

    anim.save('animation_aufgabe3-1.gif', writer='imagemagick')
