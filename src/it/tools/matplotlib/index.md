# Matplotlib



Representation of `cos(x)` and `sin(x)` in `[-1;5]` with a step of `0.1`.

```python
from matplotlib import pyplot as plt
import numpy as np

x = [i for i in np.arange(-1,5.1,0.1)]
cos = [np.cos(i) for i in x]
sin = [np.sin(i) for i in x]
plt.plot(x, cos)
plt.plot(x, sin)
plt.show()
```

Modify the axis terminals

```python
plt.axis((Xmin, Xmax, Ymin, Ymax))
# or
plt.xlim(min,max)
plt.ylim(min,max)
```

Change labels

```python
plt.xticks(position, labels, rotation, horizontal_alignment) # x-axis
plt.yticks(position, labels, rotation, vertical_alignment) # y-axes
```

Adapt the size of the image according to the content

```python
plt.tight_layout()
```

Change Titles

```python
plt.title() # graphic
plt.x_label() # x-axes
plt.y_label() # y-axes
```

Everything that is text can be changed

```python
color
fontname
fontsize # size in points
fontweight # bold/normal
style # normal/italic/oblique
Latex # '$...$'
```

Draw a curve

```python
plot([x-axis...], [ordonnees...])
# optional parameters, if None, then [0, 1, 2, ...]
```

Display legends. Must be called after all calls to `plot()`

```python
plt.legend()
```



Interactive mode (no need to call `show()`). Display a curve, do other tasks, question the user and update the curve.

Some `plot()` parameters

```python
color
linestyle (solid, dashed, dashdot, ...)
linewidth
marker
markersize
```



Change the title of the window (default: 'Figure 1')

```python
plt.gcf().canvas_manager.set_windows.title("New title")
```



Some examples on [Matplotlib](https://matplotlib.org/stable/gallery/index.html)