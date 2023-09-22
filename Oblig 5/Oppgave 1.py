import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Define points
x = np.array([1, 4, 6, 8, 10, 12])
y = np.array([3, -6, -3, -4, -2, -4])

# Clamped Cubic Spline
cs_clamped = CubicSpline(x, y, bc_type=((2, 0), (2, 0)))

# Curvature Adjusted Cubic Spline (Not-a-knot)
cs_curvature_adjusted = CubicSpline(x, y, bc_type='not-a-knot')

# Natural Cubic Spline
cs_natural = CubicSpline(x, y, bc_type='natural')

# Parabolically Terminated Cubic Spline
cs_parabolically_terminated = CubicSpline(x, y, bc_type='clamped')

# x-values for smooth plotting
x_smooth = np.linspace(1, 12, 100)

# Evaluate spline functions
y_clamped = cs_clamped(x_smooth)
y_curvature_adjusted = cs_curvature_adjusted(x_smooth)
y_natural = cs_natural(x_smooth)
y_parabolically_terminated = cs_parabolically_terminated(x_smooth)

# Plot the results
plt.plot(x_smooth, y_clamped, label='Clamped Cubic Spline')
plt.plot(x_smooth, y_curvature_adjusted, label='Curvature Adjusted Spline')
plt.plot(x_smooth, y_natural, label='Natural Cubic Spline')
plt.plot(x_smooth, y_parabolically_terminated, label='Parabolically Terminated Spline')
plt.scatter(x, y, c='red', label='Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Different Types of Cubic Splines')
plt.grid()
plt.show()

