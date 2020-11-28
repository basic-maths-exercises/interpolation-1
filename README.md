# Linear interpolation

In `main.py`, I have set up two NumPy arrays to hold a table of function values.  The NumPy array called `xv` holds the x coordinates of two points on the function and the NumPy array called `yv` holds the corresponding y-coordinates.  __Your task is to linearly interpolate the value of this function for 6 points between these two coordinates and to draw a graph of the interpolated function.__

I have started you off by writing a loop to generate the x-coordinates at which I would like the function to be interpolated.  These x-coordinates are stored in the NumPy array called `lxv` and have been generated using the following loop:

````
 for i in range(6) : 
  lxv[i] = xv[0] + i*(xv[1]-xv[0]) / 5
````

If you think about what this code is doing you quickly realise that `lxv[0]=xv[0`] and `lxv[5]=xv[1]`.  The remaining 4 values in `lxv` are then equally spaced between these two endpoints.

Your task is to evaluate the y-coordinates at each of these x-coordinates in `lxv`.   These y-coordinates should be stored in the NumPy array called `lyv`. Remember that the formula for linear interpolation is:

![](https://render.githubusercontent.com/render/math?math=f(x)=f(x_1)%2B\frac{f(x_2)-f(x_1)}{x_2-x_1}(x-x_1))

Once your code is complete a graph of the linearly interpolated datapoints is generated.
