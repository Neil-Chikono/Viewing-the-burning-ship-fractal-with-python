#viewing a mandelbrot fractal through a python program


#z_{n+1}=z_n^2+c
import matplotlib
matplotlib.use("MacOSX")


import numpy as np 
import matplotlib.pyplot as plt 

#image parameters 


width = 2400
height = 2400 
max_iterations = 200

#zoom parameters 

zoom = 1.0 
center_x = -0.5
center_y = 0.0

def mandelbrot(width, height, zoom, center_x, center_y, max_iterations ):
    
#calaulate the visible region 
    scale = 1.5 / zoom 

    x_min = center_x - scale 
    x_max = center_x + scale 

    y_min = center_y - scale 
    y_max = center_y + scale 

    # create corordinates 

    x = np.linspace(x_min, x_max,  width)
    y = np.linspace(y_min, y_max, height)

    #create a grid of complex numbers 
    c = x[np.newaxis, :] + 1j * y[:, np.newaxis]

    # initalaize Z 

    Z = np.zeros_like(c)

    #store sthe escape iteration for each pixel 
    result = np.full(c.shape, max_iterations)

    #track points that have not escaped 
    active = np.ones(c.shape, dtype=bool)

    for i in range(max_iterations):

    #mandelbot equation 



        Z[active] = (
            np.abs(Z[active].real) 
            + 1j * np.abs(Z[active].imag)
        ) ** 2 + c[active]
        
      


        #find points that have escaped 
        escaped = active & (np.abs(Z) > 2)

        #recodr thier iteration 
        result[escaped] = i 

        #calculating escaped points 
        active[escaped] = False

    return result


# Generate the fractal

fig, ax = plt.subplots()

image = mandelbrot(
    width, height, zoom,
    center_x, center_y, max_iterations
)

display = ax.imshow(
    image,
    cmap="inferno",
    origin="lower"
)

ax.axis("off")


def update():

    image = mandelbrot(
        width, height, zoom,
        center_x, center_y, max_iterations
    )

    display.set_data(image)

    ax.set_title(f"Zoom: {zoom:.2f}x")

    fig.canvas.draw_idle()


def on_scroll(event):

    global zoom

    if event.button == "up":
        zoom *= 1.5

    elif event.button == "down":
        zoom /= 1.5

    update()


fig.canvas.mpl_connect("scroll_event", on_scroll)

plt.show()


