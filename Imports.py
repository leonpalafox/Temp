# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:31:24 2016

@author: carlo
"""
import tkMessageBox
import Tkinter
import tkFileDialog
import openpyxl
import xlwt
import copy
import math
import numpy
import networkx as nx
from sklearn import manifold
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
from sklearn.cluster import DBSCAN

from tempfile        import TemporaryFile
from Tkinter         import Frame, LEFT, LabelFrame, W, E, Scrollbar, RIGHT
from Tkinter         import Listbox, BOTH, Y, Radiobutton, Label, GROOVE
from Tkinter         import HORIZONTAL, IntVar, RIDGE, OptionMenu, Scale
from Tkinter         import Checkbutton, mainloop, StringVar