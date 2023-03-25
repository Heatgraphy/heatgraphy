How to customize your visualization?
====================================

Retrieve main axes
------------------

Easily access the main axes by invoking the :meth:`get_main_ax() <heatgraphy.WhiteBoard.get_main_ax>` method after rendering your plot.
Remember to retrieve the axes **after**
you render the plot. If not render, the axes will not be created.

Check out the example below to learn how to create a beautiful heatmap with a custom border:

.. code-block:: python
    :emphasize-lines: 7

    >>> import heatgraphy as hg
    >>> from matplotlib.patches import Rectangle
    >>> data = np.random.rand(10, 10)
    >>> h = hg.Heatmap(data)
    >>> h.render()
    >>> # Get the ax after render()
    >>> hax = h.get_main_ax()
    >>> border = Rectangle((0, 0), 1, 1, fill=False, ec=".1", lw=5, transform=hax.transAxes)
    >>> hax.add_artist(border)


.. plot::
    :context: close-figs
    :include-source: False

    >>> import heatgraphy as hg
    >>> from matplotlib.patches import Rectangle
    >>> data = np.random.rand(10, 10)
    >>> h = hg.Heatmap(data)
    >>> h.render()
    >>> # Get the ax after render()
    >>> hax = h.get_main_ax()
    >>> border = Rectangle((0, 0), 1, 1, fill=False, ec=".1", lw=5, transform=hax.transAxes)
    >>> hax.add_artist(border)

When working with split heatmaps, you'll receive multiple axes in return, ordered from the upper left to the lower right:

.. plot::
    :context: close-figs

    >>> h = hg.Heatmap(data, cmap="binary")
    >>> h.hsplit(cut=[5])
    >>> h.vsplit(cut=[5])
    >>> h.render()
    >>> # Get the ax after render()
    >>> hax = h.get_main_ax()
    >>> print(hax)
        [<AxesSubplot: > <AxesSubplot: > <AxesSubplot: > <AxesSubplot: >]
    >>> colors = ["#9a60b4", "#73c0de", "#3ba272", "#fc8452"]
    >>> # purple, blue, green, orange
    >>> for ax, c in zip(hax, colors):
    ...     border = Rectangle((0, 0), 1, 1, fill=False, ec=c, lw=5, transform=ax.transAxes)
    ...     ax.add_artist(border)


Retrieve side axes
------------------

To retrieve side axes, use the :meth:`get_ax() <heatgraphy.WhiteBoard.get_ax>`
method and provide the name of your target plot. Remember to assign a name to your plot first:


.. code-block:: python
    :emphasize-lines: 5, 8

    >>> h = hg.Heatmap(data)
    >>> h.split_row(cut=[5])
    >>> bar = hg.plotter.Numbers(np.arange(10))
    >>> h.add_right(bar, name="My Bar")
    >>> h.render()
    >>> # Get the ax after render()
    >>> bar_axes = h.get_ax("My Bar")
    >>> colors = ["#9a60b4", "#73c0de"]
    >>> # purple, blue
    >>> for ax, c in zip(bar_axes, colors):
    ...     bg = Rectangle((0, 0), 1, 1, fc=c, zorder=-1, transform=ax.transAxes)
    ...     ax.add_artist(bg)


.. plot::
    :context: close-figs
    :include-source: False

    >>> h = hg.Heatmap(data)
    >>> h.hsplit(cut=[5])
    >>> bar = hg.plotter.Numbers(np.arange(10))
    >>> h.add_right(bar, name="My Bar")
    >>> h.render()
    >>> # Get the ax after render()
    >>> bar_axes = h.get_ax("My Bar")
    >>> colors = ["#9a60b4", "#73c0de"]
    >>> # purple, blue
    >>> for ax, c in zip(bar_axes, colors):
    ...     bg = Rectangle((0, 0), 1, 1, fc=c, zorder=-1, transform=ax.transAxes)
    ...     ax.add_artist(bg)