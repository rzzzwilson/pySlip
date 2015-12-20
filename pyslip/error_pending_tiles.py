#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Source of the 'error' and 'pending' tiles data.

The code here is generated from the:
    error_tile.png
    pending_tile.png
files in the pyslip/examples/graphics directory using:
    /usr/local/bin/img2py <file>
"""

import wx
from wx.lib.embeddedimage import PyEmbeddedImage


# the 'pending' tile data
def getPendingImage():
    """Generate 'pending' image from embedded data."""

    return PyEmbeddedImage(
    "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").GetImage()


def getErrorImage():
    """Generate 'pending' image from embedded data."""

    return PyEmbeddedImage(
    "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").GetImage()
