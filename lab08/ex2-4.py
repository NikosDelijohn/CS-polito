# Define constant variables.
INITIAL_DISPLACEMENT = 0.5  # m
INITIAL_VELOCITY = 0  # m/s
MASS = 1  # kg
K = 10  # N/m
TIMESTEP = 0.01  # s

# Set up initial values for the draw position in the window, the spring
# displacement and the velocity.
def main():

    x = INITIAL_DISPLACEMENT
    v = INITIAL_VELOCITY
    t = 0  # time

    while t < 10.0:
        a = -K * x / MASS
        v = v + a * TIMESTEP
        x = x + v * TIMESTEP
        print(f'Time = {t:5.2f} s    Position = {x:8.3f} m')
        t = t + TIMESTEP

if __name__ == "__main__":
    main()