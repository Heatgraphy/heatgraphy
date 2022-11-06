from __future__ import annotations

from typing import Any, List, Callable

import numpy as np
from matplotlib.artist import Artist
from matplotlib.axes import Axes

from .._deform import Deformation


class RenderPlan:
    name: str
    data: Any
    size: float = 1.
    side: str = "top"
    # label if a render plan
    # can be used on split axes
    no_split: bool = False
    # label if a render plan need to calculate
    # canvas size before rendering
    canvas_size_unknown: bool = False

    render_data = None
    deform: Deformation = None
    deform_func = None

    def set(self, **kwargs):
        for k, v in kwargs.items():
            if k == "side":
                self.set_side(v)
            else:
                self.__setattr__(k, v)

    def set_side(self, side):
        self.side = side
        self._update_deform_func()

    def set_size(self, size):
        self.size = size

    def _update_deform_func(self):
        if self.is_deform:
            if self.h:
                trans = self.deform.transform_row
            elif self.v:
                trans = self.deform.transform_col
            else:
                trans = self.deform.transform
            self.deform_func = trans

    def set_deform(self, deform: Deformation):
        self.deform = deform
        self._update_deform_func()

    @property
    def is_deform(self):
        return self.deform is not None

    def get_render_data(self):
        if self.is_deform:
            return self.deform_func(self.data)
        else:
            return self.data

    @property
    def v(self):
        return self.side in ["top", "bottom"]

    @property
    def h(self):
        return self.side in ["right", "left"]

    def render_ax(self, ax: Axes, data):
        raise NotImplemented

    def render_axes(self, axes):
        for ax, data in zip(axes, self.get_render_data()):
            self.render_ax(ax, data)

    def render(self, axes):
        if self.is_split(axes):
            self.render_axes(axes)
        else:
            self.render_ax(axes, self.get_render_data())

    def get_canvas_size(self):
        raise NotImplemented

    def align_lim(self, axes):
        if self.v:
            is_inverted = False
            ylim_low = []
            ylim_up = []
            for ax in axes:
                low, up = ax.get_ylim()
                if ax.yaxis_inverted():
                    is_inverted = True
                    low, up = up, low
                ylim_up.append(up)
                ylim_low.append(low)
            ylims = [np.min(ylim_low), np.max(ylim_up)]
            if is_inverted:
                ylims = ylims[::-1]
            for ax in axes:
                ax.set_ylim(*ylims)
        else:
            is_inverted = False
            xlim_low = []
            xlim_up = []
            for ax in axes:
                low, up = ax.get_xlim()
                if ax.xaxis_inverted():
                    is_inverted = True
                    low, up = up, low
                xlim_up.append(up)
                xlim_low.append(low)
            xlims = [np.min(xlim_low), np.max(xlim_up)]
            if is_inverted:
                xlims = xlims[::-1]
            for ax in axes:
                ax.set_xlim(*xlims)

    @staticmethod
    def is_split(axes):
        return not isinstance(axes, Axes)

    def get_legends(self) -> List[Artist] | None:
        return None

    def set_legends(self, *args, **kwargs):
        raise NotImplemented
