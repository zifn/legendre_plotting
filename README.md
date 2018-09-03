# point_to_line_representation

## Motivation
Any individual function can be represented in several different ways. The common way that these functions are visualized is as a collection of points where for every $x$ value a corresponding $y$ value is calculated and plotted where the tuples take the form $(x, y(x))$. However, this function can be represented as function of it's derivative using the Legendre transform. This new function ($\psi(P)$), takes as input the slope of a line and computes the y intercept of the line that will make that line tangent to the original function $y(x)$.  The existence of $\psi(P)$ allows functions to be visualized not as a collection of points but as a collection of lines tangent to the curve being represented. This has the effect of transforming the curve from a point geometric to a line geometric representation. This python script computes and plots this collection of tangent curves and compares it to the point geometric representation

This method of taking a function and looking at it's Legendre transform has been a valuable technique in physics. It acts as the glue between Lagrangian and Hamiltonian mechanics, and it's the link between the various representations of the equation of state in thermodynamics (ie. Energy $E$ and Enthalpy $H$ ).

## Quick Start
The legendre_plotter script requires the sympy, numpy, and matplotlib libraries. Please have these packages installed in your local environment prior to running the program. The script will plot three graphs per run, the traditional point representation, the line geometric representation, and a plot of both representations. To change the viewing window, the number of lines ploted, or the range of slopes plotted, the parameters on lines 13:19 of the main script can be adjusted. To change the function whose transform is computed and plotted, modify line number 29 `y = (1/10)*x**2 # Modify this line to plot your own function`. When modifing the function, because this script is only designed to handle 1D functions, please make your expression using the x sympy symbol and assign your created sympy expression to the parameter y.  

```python
YMIN = -20
YMAX = 20
XMIN = -15
XMAX = 15
NUMB_LINES = 20
SLOPE_MIN = -4
SLOPE_MAX = 4
```
global parameters that can be adjusted to change the window, number of lines, and range of slopes plotted 

## Sample Output

![Alt text](sample/xlnx_point.png?raw=true "xln(x) point representation")

![Alt text](sample/xlnx_line.png?raw=true "xln(x) line representation")

![Alt text](sample/xlnx_point_and_line.png?raw=true "xln(x) point and line representation")

## References
- Callen 1985 Thermodynamics and an Introduction to Thermostatistics
- [introduction to sympy](https://docs.sympy.org/latest/tutorial/intro.html)
- [legendre transformations](https://en.wikipedia.org/wiki/Legendre_transformation)
