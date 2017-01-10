from django.template import RequestContext
from django.shortcuts import render_to_response

from templateApp.models import *
from templateApp.templateAppObjs import *
import pandas as pd
#from pandas import DataFrame

from seaborn import color_palette, diverging_palette

from bokeh.embed import components
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool, Circle, Panel, Tabs

import os as _os
import re as _re
import json as _json
import argparse as _ap
import calendar as _cal
import datetime as _datetime
import urllib.request as _request

import seaborn as sns
import matplotlib.pyplot as _plt
from pandas import DataFrame as DataFrame

from jsonspec.validators import load as _load
from jsonspec.validators import ValidationError as _ValidationError

from django.conf import settings

from lola.render.server_side import render

# Plot values
_WIDTH = 1000  # pixels
_HEIGHT = 700  # pixels
_PLOT_TOOLS = 'pan,box_zoom,resize,wheel_zoom,save,reset'

heatmap_data = {'score': ['CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'CADD_raw_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'SIFT_converted_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_rankscore'], 'x': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73'], 'value': [0.00951, 0.09921, 0.16201, 0.08792, 0.15128, 0.44901, 0.92674, 0.64382, 0.26193, 0.268, 0.95434, 0.37322, 0.50156, 0.95654, 0.1683, 0.08205, 0.05597, 0.36136, 0.43997, 0.30856, 0.72671, 0.8541, 0.77383, 0.71343, 0.85229, 0.68575, 0.52824, 0.93296, 0.95453, 0.89763, 0.57923, 0.27556, 0.92961, 0.85589, 0.80245, 0.76719, 0.84376, 0.74234, 0.94302, 0.88102, 0.85307, 0.92787, 0.90711, 0.76713, 0.8429, 0.62647, 0.67453, 0.71305, 0.60239, 0.89587, 0.70264, 0.88187, 0.91415, 0.92933, 0.94665, 0.88988, 0.94359, 0.95212, 0.95225, 0.95292, 0.45473, 0.86627, 0.46986, 0.7768, 0.87426, 0.22364, 0.74004, 0.91244, 0.48009, 0.83918, 0.57571, 0.95262, 0.91161, 0.91619, 0.13722, 0.03977, 0.03055, 0.17853, 0.36066, 0.25018, 0.56404, 0.72092, 0.08393, 0.06491, 0.63171, 0.14572, 0.04113, 0.44307, 0.46462, 0.09879, 0.42437, 0.6818, 0.23326, 0.1954, 0.91219, 0.91219, 0.91219, 0.91219, 0.91219, 0.91219, 0.07732, 0.78421, 0.49561, 0.91219, 0.32098, 0.27744, 0.91219, 0.91219, 0.91219, 0.91219, 0.78421, 0.91219, 0.91219, 0.57428, 0.91219, 0.91219, 0.44988, 0.63171, 0.37918, 0.91219, 0.91219, 0.36662, 0.91219, 0.91219, 0.41314, 0.63171, 0.91219, 0.91219, 0.78421, 0.91219, 0.78421, 0.91219, 0.63171, 0.5008, 0.78421, 0.91219, 0.36865, 0.91219, 0.91219, 0.24148, 0.91219, 0.63171, 0.31046, 0.72092, 0.32098, 0.91219, 0.91219, 0.91219, 0.10235, 0.06737, 0.12561, 0.23271, 0.23484, 0.49209, 0.76378, 0.89865, 0.02634, 0.02634, 0.89865, 0.10235, 0.22952, 0.76378, 0.31257, 0.06737, 0.42374, 0.47865, 0.54244, 0.06737, 0.89865, 0.89865, 0.89865, 0.89865, 0.89865, 0.71542, 0.76378, 0.89865, 0.89865, 0.89865, 0.64686, 0.45424, 0.89865, 0.89865, 0.89865, 0.89865, 0.89865, 0.89865, 0.89865, 0.89865, 0.71542, 0.89865, 0.71542, 0.89865, 0.89865, 0.89865, 0.89865, 0.71542, 0.89865, 0.89865, 0.68941, 0.89865, 0.89865, 0.76378, 0.89865, 0.89865, 0.89865, 0.89865, 0.89865, 0.89865, 0.45811, 0.89865, 0.60931, 0.89865, 0.89865, 0.32566, 0.89865, 0.76378, 0.60931, 0.89865, 0.71542, 0.89865, 0.89865, 0.89865]}

roc_data = [{'coords': ((1.0, 1.0), (0.9, 1.0), (0.75, 1.0), (0.65, 1.0), (0.6, 1.0), (0.55, 1.0), (0.5, 1.0), (0.44999999999999996, 1.0), (0.4, 1.0), (0.4, 0.9814814814814815), (0.35, 0.9814814814814815), (0.35, 0.9629629629629629), (0.35, 0.9444444444444444), (0.30000000000000004, 0.9444444444444444), (0.25, 0.9444444444444444), (0.19999999999999996, 0.9444444444444444), (0.19999999999999996, 0.9074074074074074), (0.19999999999999996, 0.8888888888888888), (0.19999999999999996, 0.8703703703703703), (0.19999999999999996, 0.7777777777777778), (0.09999999999999998, 0.7222222222222222), (0.0, 0.0)), 'thresholds': ['inf', 0.046855, 0.08485999999999999, 0.11398, 0.177565, 0.23111500000000001, 0.233775, 0.273705, 0.31911500000000004, 0.37470000000000003, 0.43899, 0.456175, 0.46838, 0.48537, 0.5172650000000001, 0.575875, 0.628085, 0.6681349999999999, 0.702415, 0.7396, 0.831215, 'inf'], 'algorithm': 'Polyphen2_HDIV_rankscore', 'auc': [0.8112108693595568, 0.9018518518518519, 0.992492834344147]}, {'coords': ((1.0, 1.0), (0.95, 1.0), (0.9, 1.0), (0.85, 1.0), (0.8, 1.0), (0.8, 0.9814814814814815), (0.75, 0.9814814814814815), (0.7, 0.9814814814814815), (0.65, 0.9814814814814815), (0.6, 0.9814814814814815), (0.55, 0.9814814814814815), (0.5, 0.9814814814814815), (0.44999999999999996, 0.9814814814814815), (0.44999999999999996, 0.9629629629629629), (0.4, 0.9629629629629629), (0.4, 0.9444444444444444), (0.4, 0.9259259259259259), (0.4, 0.8888888888888888), (0.35, 0.8888888888888888), (0.35, 0.8703703703703703), (0.35, 0.8518518518518519), (0.35, 0.8333333333333334), (0.35, 0.8148148148148148), (0.30000000000000004, 0.8148148148148148), (0.25, 0.8148148148148148), (0.25, 0.7962962962962963), (0.19999999999999996, 0.7962962962962963), (0.19999999999999996, 0.7777777777777778), (0.19999999999999996, 0.7592592592592593), (0.15000000000000002, 0.7592592592592593), (0.15000000000000002, 0.7407407407407407), (0.09999999999999998, 0.6666666666666666), (0.050000000000000044, 0.6666666666666666), (0.0, 0.6481481481481481), (0.0, 0.5555555555555556), (0.0, 0.0)), 'thresholds': ['inf', 0.03516, 0.04045, 0.05302, 0.071115, 0.080625, 0.09136, 0.118005, 0.14146999999999998, 0.162125, 0.186965, 0.21433, 0.23737, 0.24583, 0.26381, 0.29395000000000004, 0.31572, 0.34082, 0.36363999999999996, 0.367635, 0.373915, 0.39616, 0.418755, 0.43372, 0.446475, 0.45725, 0.48011499999999996, 0.498205, 0.53242, 0.56916, 0.602995, 0.656755, 0.70136, 0.7525649999999999, 0.8482, 'inf'], 'algorithm': 'SIFT_converted_rankscore', 'auc': [0.8254493983031341, 0.8967592592592594, 0.9680691202153846]}, {'coords': ((1.0, 1.0), (0.95, 1.0), (0.9, 1.0), (0.85, 1.0), (0.8, 1.0), (0.75, 1.0), (0.7, 1.0), (0.65, 1.0), (0.6, 1.0), (0.6, 0.9814814814814815), (0.55, 0.9814814814814815), (0.5, 0.9814814814814815), (0.5, 0.9629629629629629), (0.44999999999999996, 0.9629629629629629), (0.4, 0.9629629629629629), (0.35, 0.9629629629629629), (0.30000000000000004, 0.9629629629629629), (0.25, 0.9629629629629629), (0.25, 0.9444444444444444), (0.25, 0.9259259259259259), (0.25, 0.9074074074074074), (0.19999999999999996, 0.9074074074074074), (0.19999999999999996, 0.8888888888888888), (0.19999999999999996, 0.8703703703703703), (0.19999999999999996, 0.8518518518518519), (0.19999999999999996, 0.8333333333333334), (0.19999999999999996, 0.8148148148148148), (0.15000000000000002, 0.8148148148148148), (0.15000000000000002, 0.7962962962962963), (0.15000000000000002, 0.7777777777777778), (0.15000000000000002, 0.7592592592592593), (0.15000000000000002, 0.7407407407407407), (0.15000000000000002, 0.7222222222222222), (0.15000000000000002, 0.7037037037037037), (0.15000000000000002, 0.6851851851851852), (0.15000000000000002, 0.6666666666666666), (0.15000000000000002, 0.6481481481481481), (0.15000000000000002, 0.6296296296296297), (0.15000000000000002, 0.6111111111111112), (0.15000000000000002, 0.5925925925925926), (0.15000000000000002, 0.5740740740740741), (0.15000000000000002, 0.5555555555555556), (0.15000000000000002, 0.5370370370370371), (0.15000000000000002, 0.5185185185185185), (0.15000000000000002, 0.5), (0.15000000000000002, 0.48148148148148145), (0.15000000000000002, 0.46296296296296297), (0.15000000000000002, 0.4444444444444444), (0.15000000000000002, 0.42592592592592593), (0.15000000000000002, 0.4074074074074074), (0.15000000000000002, 0.3888888888888889), (0.15000000000000002, 0.37037037037037035), (0.15000000000000002, 0.35185185185185186), (0.15000000000000002, 0.3333333333333333), (0.15000000000000002, 0.3148148148148148), (0.15000000000000002, 0.2962962962962963), (0.15000000000000002, 0.2777777777777778), (0.15000000000000002, 0.25925925925925924), (0.15000000000000002, 0.24074074074074073), (0.15000000000000002, 0.2222222222222222), (0.09999999999999998, 0.2222222222222222), (0.09999999999999998, 0.2037037037037037), (0.09999999999999998, 0.18518518518518517), (0.09999999999999998, 0.16666666666666666), (0.09999999999999998, 0.14814814814814814), (0.09999999999999998, 0.12962962962962962), (0.09999999999999998, 0.1111111111111111), (0.09999999999999998, 0.09259259259259259), (0.09999999999999998, 0.07407407407407407), (0.09999999999999998, 0.05555555555555555), (0.09999999999999998, 0.037037037037037035), (0.09999999999999998, 0.018518518518518517), (0.050000000000000044, 0.018518518518518517), (0.050000000000000044, 0.0), (0.0, 0.0)), 'thresholds': ['inf', 0.03274, 0.06901, 0.084985, 0.09356500000000001, 0.125245, 0.15664499999999998, 0.165155, 0.19597, 0.242785, 0.264965, 0.27178, 0.29206, 0.33496000000000004, 0.36729, 0.40659500000000004, 0.44449000000000005, 0.45187, 0.462295, 0.47497500000000004, 0.490825, 0.5149, 0.5519750000000001, 0.57747, 0.5908100000000001, 0.61443, 0.635145, 0.659175, 0.68014, 0.694195, 0.7078450000000001, 0.71324, 0.72007, 0.733375, 0.74119, 0.7547349999999999, 0.7671600000000001, 0.77051, 0.775315, 0.789625, 0.8208150000000001, 0.84104, 0.8433299999999999, 0.848025, 0.85268, 0.853585, 0.854995, 0.8610800000000001, 0.8702650000000001, 0.87764, 0.881445, 0.885875, 0.8928750000000001, 0.89675, 0.90237, 0.90936, 0.9120250000000001, 0.913295, 0.91517, 0.921465, 0.927305, 0.9286, 0.92947, 0.931285, 0.93799, 0.9433050000000001, 0.94512, 0.9493849999999999, 0.9521850000000001, 0.952435, 0.95277, 0.95363, 0.9544349999999999, 0.955535, 'inf'], 'algorithm': 'CADD_raw_rankscore', 'auc': [0.6899508470778891, 0.837037037037037, 0.9841232269961849]}]

boxplot_data = {'Polyphen2_HDIV_rankscore': {'value': [0.89865, 0.10235, 0.89865, 0.06737, 0.12561, 0.89865, 0.89865, 0.89865, 0.71542, 0.23271, 0.23484, 0.49209, 0.76378, 0.89865, 0.76378, 0.89865, 0.89865, 0.64686, 0.45424, 0.89865, 0.89865, 0.89865, 0.02634, 0.89865, 0.89865, 0.89865, 0.89865, 0.89865, 0.02634, 0.89865, 0.89865, 0.10235, 0.22952, 0.76378, 0.71542, 0.89865, 0.71542, 0.31257, 0.06737, 0.42374, 0.47865, 0.54244, 0.06737, 0.89865, 0.89865, 0.89865, 0.89865, 0.71542, 0.89865, 0.89865, 0.68941, 0.89865, 0.89865, 0.76378, 0.89865, 0.89865, 0.89865, 0.89865, 0.89865, 0.89865, 0.45811, 0.89865, 0.60931, 0.89865, 0.89865, 0.32566, 0.89865, 0.76378, 0.60931, 0.89865, 0.71542, 0.89865, 0.89865, 0.89865], 'effect': ['deleterious', 'benign', 'deleterious', 'benign', 'benign', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'benign', 'benign', 'benign', 'deleterious', 'deleterious', 'benign', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'benign', 'benign', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'benign', 'deleterious', 'benign', 'benign', 'benign', 'benign', 'deleterious', 'deleterious', 'deleterious', 'benign', 'benign', 'benign', 'benign', 'benign', 'benign', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious']}, 'SIFT_converted_rankscore': {'value': [0.91219, 0.13722, 0.91219, 0.03977, 0.03055, 0.91219, 0.91219, 0.91219, 0.91219, 0.17853, 0.36066, 0.25018, 0.07732, 0.78421, 0.56404, 0.49561, 0.91219, 0.32098, 0.27744, 0.91219, 0.91219, 0.72092, 0.08393, 0.91219, 0.91219, 0.78421, 0.91219, 0.91219, 0.06491, 0.57428, 0.63171, 0.14572, 0.04113, 0.44307, 0.91219, 0.91219, 0.44988, 0.46462, 0.09879, 0.42437, 0.6818, 0.23326, 0.1954, 0.63171, 0.37918, 0.91219, 0.91219, 0.36662, 0.91219, 0.91219, 0.41314, 0.63171, 0.91219, 0.91219, 0.78421, 0.91219, 0.78421, 0.91219, 0.63171, 0.5008, 0.78421, 0.91219, 0.36865, 0.91219, 0.91219, 0.24148, 0.91219, 0.63171, 0.31046, 0.72092, 0.32098, 0.91219, 0.91219, 0.91219], 'effect': ['deleterious', 'benign', 'deleterious', 'benign', 'benign', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'benign', 'benign', 'benign', 'deleterious', 'deleterious', 'benign', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'benign', 'benign', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'benign', 'deleterious', 'benign', 'benign', 'benign', 'benign', 'deleterious', 'deleterious', 'deleterious', 'benign', 'benign', 'benign', 'benign', 'benign', 'benign', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious']}, 'CADD_raw_rankscore': {'value': [0.72671, 0.00951, 0.8541, 0.09921, 0.16201, 0.77383, 0.71343, 0.85229, 0.68575, 0.08792, 0.15128, 0.44901, 0.52824, 0.93296, 0.92674, 0.95453, 0.89763, 0.57923, 0.27556, 0.92961, 0.85589, 0.64382, 0.26193, 0.80245, 0.76719, 0.84376, 0.74234, 0.94302, 0.268, 0.88102, 0.95434, 0.37322, 0.50156, 0.95654, 0.85307, 0.92787, 0.90711, 0.1683, 0.08205, 0.05597, 0.36136, 0.43997, 0.30856, 0.76713, 0.8429, 0.62647, 0.67453, 0.71305, 0.60239, 0.89587, 0.70264, 0.88187, 0.91415, 0.92933, 0.94665, 0.88988, 0.94359, 0.95212, 0.95225, 0.95292, 0.45473, 0.86627, 0.46986, 0.7768, 0.87426, 0.22364, 0.74004, 0.91244, 0.48009, 0.83918, 0.57571, 0.95262, 0.91161, 0.91619], 'effect': ['deleterious', 'benign', 'deleterious', 'benign', 'benign', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'benign', 'benign', 'benign', 'deleterious', 'deleterious', 'benign', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'benign', 'benign', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'benign', 'deleterious', 'benign', 'benign', 'benign', 'benign', 'deleterious', 'deleterious', 'deleterious', 'benign', 'benign', 'benign', 'benign', 'benign', 'benign', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious', 'deleterious']}}

scatter_plot_data = {
  "description": "A scatterplot showing horsepower and miles per gallons for various cars.",
  "data": {
  "values":
    [
      {
          "x": 3.007088910408773,
          "y": -0.5767486883101697
      },
      {
          "x": -0.3715147717513474,
          "y": -0.45655775867899306
      },
      {
          "x": 1.013465756577963,
          "y": -0.9917248443846479
      },
      {
          "x": 2.2104159257344307,
          "y": 0.6226417882091236
      },
      {
          "x": 1.3677522196434437,
          "y": 1.493193428246762
      },
      {
          "x": 1.1941633047120335,
          "y": -1.0456542199615089
      },
      {
          "x": -1.488021859840008,
          "y": 1.736696131803707
      },
      {
          "x": -1.954388466537492,
          "y": 1.2115142674655741
      },
      {
          "x": 0.9633728872400767,
          "y": -0.7658893522221107
      },
      {
          "x": 3.1621865079188507,
          "y": -2.1570137156089357
      },
      {
          "x": -1.3274719768197967,
          "y": 0.30233483483337686
      },
      {
          "x": 0.7674649442182615,
          "y": -0.7550003063113175
      },
      {
          "x": 1.6919485996080377,
          "y": -0.7215202040070503
      },
      {
          "x": -0.8099157907986564,
          "y": 0.930681949406044
      },
      {
          "x": 1.17685436823612,
          "y": 2.373712486875515
      },
      {
          "x": 0.9202788923852231,
          "y": -1.1929625780898914
      },
      {
          "x": 0.31253418762596397,
          "y": 0.7792442534403811
      },
      {
          "x": -1.1322827500223775,
          "y": -0.343555606892329
      },
      {
          "x": 1.6258059183074645,
          "y": -0.5801457938240323
      },
      {
          "x": 0.5665960097342454,
          "y": 0.671313570658484
      },
      {
          "x": 1.4235362037149164,
          "y": -0.8503088749418612
      },
      {
          "x": -0.4501147264463176,
          "y": -0.3015538451597721
      },
      {
          "x": 0.19564880970837514,
          "y": 0.7163439493394218
      },
      {
          "x": 0.5412313516755161,
          "y": 0.3372610870524152
      },
      {
          "x": 1.291909525435338,
          "y": -1.3210104277338053
      },
      {
          "x": 2.0599738861731796,
          "y": 1.1189651779939556
      },
      {
          "x": -0.8829162386056493,
          "y": 0.5809792541452514
      },
      {
          "x": 0.06359143165035028,
          "y": 0.12488806194295811
      },
      {
          "x": 1.8586018975447363,
          "y": -2.9982416638580873
      },
      {
          "x": -0.3112474011912661,
          "y": 1.0030604839121295
      },
      {
          "x": 0.5816192995919195,
          "y": -2.0136132498656267
      },
      {
          "x": -0.5065755767418036,
          "y": 1.0838305800093748
      },
      {
          "x": 0.04938407863907232,
          "y": -0.00755622034389306
      },
      {
          "x": 1.014333703859286,
          "y": -1.8205897559735649
      },
      {
          "x": -1.3157865654461502,
          "y": 0.5444623245977386
      },
      {
          "x": 0.28338720124712313,
          "y": -0.6774339816381
      },
      {
          "x": -1.4627164692544423,
          "y": -1.3448248533196985
      },
      {
          "x": 1.3156837952801457,
          "y": 2.6841593248028452
      },
      {
          "x": -0.8609085673777807,
          "y": 1.7741824447480103
      },
      {
          "x": -1.6534177579868157,
          "y": -0.4923794627606267
      },
      {
          "x": -1.8569864260373032,
          "y": 0.020226606217648224
      },
      {
          "x": 0.9687242204642484,
          "y": -1.228267633923647
      },
      {
          "x": -2.0876094976942983,
          "y": -1.4157259320937825
      },
      {
          "x": -0.6428369809744184,
          "y": -0.5466970703588849
      },
      {
          "x": -2.2175352608412897,
          "y": -0.042286084096438796
      },
      {
          "x": -0.5472368414334602,
          "y": -0.7539624835410048
      },
      {
          "x": -1.642620371752907,
          "y": 2.3950907787869076
      },
      {
          "x": -1.6233312098592725,
          "y": 0.7003356625883874
      },
      {
          "x": -0.07608983502249152,
          "y": 1.2205121683177402
      },
      {
          "x": -1.9755658041034967,
          "y": -0.6617801064785921
      },
      {
          "x": 0.5095011435433441,
          "y": -0.07020722538842813
      },
      {
          "x": 0.019691264736789272,
          "y": 0.35952599280914904
      },
      {
          "x": -0.21840990506862712,
          "y": 0.9151217562808761
      },
      {
          "x": 1.461083657923508,
          "y": 1.5200721899989125
      },
      {
          "x": 0.5031477179665955,
          "y": -1.083561253118263
      },
      {
          "x": 1.7055807290758622,
          "y": 0.08015503713634267
      },
      {
          "x": -0.06215037626405552,
          "y": -0.6904030700180733
      },
      {
          "x": -1.0657025788145984,
          "y": -0.25019771938378516
      },
      {
          "x": 0.948385573171175,
          "y": 1.5436566576535435
      },
      {
          "x": 0.8310150816505648,
          "y": 0.9558014465296636
      },
      {
          "x": 0.7368349108659572,
          "y": -0.06793603284603575
      },
      {
          "x": 1.4279113237398442,
          "y": 0.857821556532648
      },
      {
          "x": -2.4219510843896597,
          "y": -1.0741203064795402
      },
      {
          "x": 0.7596775462970807,
          "y": -1.00901715703128
      },
      {
          "x": -0.30167740255902603,
          "y": 0.09382441253731351
      },
      {
          "x": 1.2417313091331807,
          "y": 0.1461772058726318
      },
      {
          "x": 0.7118791820401059,
          "y": -0.9686983691360636
      },
      {
          "x": 3.1991953947468676,
          "y": 0.5556682172894349
      },
      {
          "x": -2.9855732879827723,
          "y": 1.116343683741117
      },
      {
          "x": -3.013592643015049,
          "y": 0.6516230039747214
      },
      {
          "x": 1.181716476844661,
          "y": -0.6679309779291568
      },
      {
          "x": 0.7503534639920022,
          "y": 0.5673752912817204
      },
      {
          "x": 0.11058343361250651,
          "y": 1.2558188364337992
      },
      {
          "x": 1.9493048268777513,
          "y": 0.1915967556848491
      },
      {
          "x": 3.9236595572019195,
          "y": 0.4017329754463508
      },
      {
          "x": 1.3539061139490955,
          "y": -0.9797867377026666
      },
      {
          "x": -0.8689395644019952,
          "y": 2.4122727558944623
      },
      {
          "x": -0.40389069998498184,
          "y": 0.8977036804832341
      },
      {
          "x": 0.8427252923470038,
          "y": -0.22853201556066743
      },
      {
          "x": -0.39961435730496864,
          "y": -0.8616836740284981
      },
      {
          "x": 0.01644542751426915,
          "y": 0.10277570373760317
      },
      {
          "x": -0.3402985976921514,
          "y": 2.1077553195204577
      },
      {
          "x": 1.086569237353543,
          "y": -0.933268582820222
      },
      {
          "x": -1.1482259990260482,
          "y": -0.7785168957675552
      },
      {
          "x": -0.2907439127307038,
          "y": -0.34020192140389854
      },
      {
          "x": -0.24764074086473406,
          "y": -0.36234152694508615
      },
      {
          "x": 1.1634326717224972,
          "y": -0.1433574093273791
      },
      {
          "x": -3.4089630035588323,
          "y": -0.5202517725447173
      },
      {
          "x": 1.4848212711940993,
          "y": -0.9089577913295793
      },
      {
          "x": 3.3778162094199122,
          "y": 0.06185943721098133
      },
      {
          "x": -0.48922335373226117,
          "y": -1.5961893945221648
      },
      {
          "x": -2.3208927340102563,
          "y": -0.682327237293137
      },
      {
          "x": -2.552882629481847,
          "y": 0.6297661397678685
      },
      {
          "x": -0.021535342051250794,
          "y": 0.8108536727387018
      },
      {
          "x": -0.13945040827466507,
          "y": -0.807856948090543
      },
      {
          "x": -0.2433424391748636,
          "y": -0.9202477946436375
      },
      {
          "x": -0.46135279938131996,
          "y": 1.5073316827149563
      },
      {
          "x": 0.7511108199691489,
          "y": -0.9833728783230232
      },
      {
          "x": -2.629138292058999,
          "y": -0.6155441242989111
      },
      {
          "x": 2.0388350577423413,
          "y": -1.365099885604345
      }
    ]
  },
  "mark": "point",
  "encoding": {
    "x": {"field": "x", "type": "quantitative"},
    "y": {"field": "y", "type": "quantitative"}
  }
}

#@login_required
def landing(request):
    '''Landing'''
    return render_to_response("templateApp/landing.html", {

    },  RequestContext(request))

#@login_required
def handleUpload(request):
    ''' Processes landing'''

    columns = []
    rows = []
    
    plot_script = ''
    plot_div = ''
    
    listPlotObjs = []
    xyList = []    
    
    plotTypeId = request.POST.get("plotTypeId","" )
    
    jsonFile = request.FILES['uploadFilePath']

    jsonData = jsonFile.read().decode('utf-8-sig')    
    
    print (str(plotTypeId)) 
    plt = render(jsonData)
    
    plotName = "outputFig.png" 
    plotPath = settings.IMAGE_OUTPUT_FOLDER + plotName   

    if _os.path.isfile(plotPath):
        _os.remove(plotPath)    
    
    if plotTypeId == "0":
        plotType = "Line_Plot"
        plt = render(jsonData)   
        
        plt.savefig(plotPath)         

    elif plotTypeId == "1":
        plotType = "Scatter_Plot"
        
        plt.savefig(plotPath)         
        
    elif plotTypeId == "2":

        plotType = "Box_Plot"
        
        print (" in box plot " )
        
        plt.figure.savefig(plotPath)         
        
    elif plotTypeId == "3":
        plotType = "HeatMap_Plot"
        
        plt.savefig(plotPath)         

    return render_to_response('templateApp/displayPlot.html', {

        "plotType":plotType,
        "plot_div":plot_div,
        "plot_script":plot_script,
        "columns":columns,        
        "rows":rows,   
        "listPlotObjs":listPlotObjs,
        "xyList":xyList,
        "plotPath":plotPath,
        "plotName":plotName,
        
    },  RequestContext(request))        

#@login_required
def processLanding(request):
    ''' Processes landing'''
    templateHomeButton = request.POST.get("templateHomeButton","0" )
    
    columns = []
    rows = []
    
    plot_script = ''
    plot_div = ''
    
    listPlotObjs = []
    xyList = []

    plot_path = ''
    
    plotName = "outputFig.png" 
    plotPath = settings.IMAGE_OUTPUT_FOLDER + plotName 

    if _os.path.isfile(plotPath):
        _os.remove(plotPath)

    if templateHomeButton == "0":
        
        plotType = "Line_Plot"
        
        jsonFile = open(settings.PROJECT_BASE_PATH + "plots/line.json","r")
        jsonData = jsonFile.read() 
        # seaborn plot
        plt = render(jsonData)        
        
        plt.savefig(plotPath)            

        # create the data for display
        listPlotObjs = _make_roc_plot_data_table (roc_data)
        # bokeh plots
        plot_script, plot_div = _roc_plot(roc_data)
 
    elif templateHomeButton == "1":
        plotType = "Scatter_Plot"
        
        jsonFile = open(settings.PROJECT_BASE_PATH + "plots/scatter.json","r")
        jsonData = jsonFile.read() 
        # seaborn plot
        plt = render(jsonData)   
        
        # create the data for display
        xyList = _make_scatter_plot_data_table (scatter_plot_data)
        # bokeh plots
        plot_script, plot_div = _scatterplot(scatter_plot_data)   
        
        plotName = "outputFig.png" 
        plotPath = settings.IMAGE_OUTPUT_FOLDER + plotName   

        if _os.path.isfile(plotPath):
            _os.remove(plotPath)
        
        plt.savefig(plotPath)         
        
    elif templateHomeButton == "2":

        plotType = "Box_Plot"
        
        jsonFile = open(settings.PROJECT_BASE_PATH + "plots/boxplot.json","r")
        jsonData = jsonFile.read() 
        # seaborn plot
        plt = render(jsonData)
        
        # create the data for display
        listPlotObjs = _make_box_plot_data_table (boxplot_data)
        # bokeh plots
        plot_script, plot_div = _box_plot(boxplot_data) 
        
        plt.figure.savefig(plotPath)            
        
    elif templateHomeButton == "3":
        plotType = "HeatMap_Plot"
        
        jsonFile = open(settings.PROJECT_BASE_PATH + "plots/heatmap.json","r")
        jsonData = jsonFile.read() 
        # seaborn plot
        plt = render(jsonData)         
        # bokeh plots
        plot_script, plot_div = _heatmap_plot(heatmap_data)        
        # create the data for display
        columns, rows = _make_heat_map_data_table (heatmap_data)
            
        plt.savefig(plotPath)             
        
    elif templateHomeButton == "4":
        
        plotType = "Bar_Chart"
        
        jsonFile = open(settings.PROJECT_BASE_PATH + "plots/barchart.json","r")
        jsonData = jsonFile.read() 
        # seaborn plot
        render(jsonData)         
            
        _sns.plt.savefig(plotPath)  
        
    return render_to_response('templateApp/displayPlot.html', {

        "plotType":plotType,
        "plot_div":plot_div,
        "plot_script":plot_script,
        "columns":columns,        
        "rows":rows,   
        "listPlotObjs":listPlotObjs,
        "xyList":xyList,
        "plotPath":plotPath,
        "plotName":plotName,
        "plotTypeId": templateHomeButton
        
    },  RequestContext(request))        

def _make_bar_chart_data_table(data):
    '''Creates data table from JSON data for bar chart data''' 
    df = pd.DataFrame(data)
    columns = list(df.columns)
    
    columns.remove("color")
    
    print ( " ^^^^^^^^ columns = " + str(columns) )
    rows = []
    for index, row in df.iterrows():
        #print " row = " + str(row)
        rows.append([row["score"], row["value"], row["x"]])
    return columns, rows

def _make_heat_map_data_table(data):
    '''Creates data table from JSON data for heat map data''' 
    df = pd.DataFrame(data)
    columns = list(df.columns)
    
    columns.remove("color")
    
    print ( " ^^^^^^^^ columns = " + str(columns) )
    rows = []
    for index, row in df.iterrows():
        #print " row = " + str(row)
        rows.append([row["score"], row["value"], row["x"]])
    return columns, rows

def _make_box_plot_data_table(data):

    '''Creates data table from JSON data for box plot data'''

    listPlotObjs = []    
    
    index = 0

    for k,v in data.items():
        
        df = pd.DataFrame(v, index=None)
        
        listPlotObj = ListPlotObj()

        listPlotObj.title = k
        
        listPlotObj.index = index
        
        listPlotObj.columns = df.columns
        
        print (df.columns)
        
        for i, row in df.iterrows():
            
            #print (str(row))
            
            listPlotObj.rows.append([row["effect"], row["value"]])
            
        index = index + 1
        
        listPlotObjs.append(listPlotObj)

    return listPlotObjs

def _make_roc_plot_data_table(data):
    
    '''Creates data table from JSON data for roc plot data'''

    listPlotObjs = []    
    
    for index,v in enumerate(data):
        
        listPlotObj = ListPlotObj()

        listPlotObj.algorithm = v["algorithm"]
        listPlotObj.aucs = v["auc"]

        listPlotObj.title = v["algorithm"]
        listPlotObj.index = index
        
        df = pd.DataFrame(columns=["coords", "thresholds"], index = None)
        
        df["coords"] = v["coords"]
        df["thresholds"] = v["thresholds"]
        
        listPlotObj.columns = ["coords", "thresholds"]
        
        for i, row in df.iterrows():
            
            print (str(row))
            
            listPlotObj.rows.append([row["coords"], row["thresholds"]])  
            
        listPlotObjs.append(listPlotObj)
    
    return listPlotObjs

def _make_scatter_plot_data_table(scatterData):
    
    '''Creates data table from JSON data for scatter plot data'''
    encoding = scatterData["encoding"]

    x_field = encoding["x"]["field"]
    y_field = encoding["y"]["field"]

    data = scatterData["data"]

    if "values" in data:
        values = data["values"]
    elif "url" in data:
        url = data["url"]
        data_type = data.get("type")

        values = _get_values(url, data_type)
    else:
        _error(x, ValueError)

    xyList = [(record[x_field], record[y_field]) for record in values]

    return xyList

def _heatmap_plot(data):
    '''Returns a (JS script, div) tuple for plot generation, both in UTF-8.'''
    colors = diverging_palette(220, 20, n=10).as_hex()
    data['color'] = [colors[min(int(x * 10), 9)] for x in data['value']]

    source = ColumnDataSource(data=data)

    heatmap = figure(
        title='Heatmap',
        y_range=list(set(data['score'])),
        plot_width=_WIDTH,
        plot_height=_HEIGHT,
        tools=_PLOT_TOOLS,
    )

    rect = heatmap.rect(
        x='x',
        y='score',
        width=1,
        height=1,
        source=source,
        color='color',
        line_color=None,
    )

    hover = HoverTool(
        renderers=[rect],
        tooltips=[('algorithm', '@score'), ('score', '@value')],
    )

    heatmap.add_tools(hover)

    heatmap.grid.grid_line_color = None
    heatmap.axis.axis_line_color = None
    heatmap.axis.major_tick_line_color = None
    heatmap.axis.major_label_text_font_size = '10pt'
    heatmap.axis.major_label_standoff = 1
    heatmap.xaxis.visible = None

    return components(heatmap)

def _box_plot(data):
    '''Returns a (JS script, div) tuple for plot generation, both in UTF-8.'''
    tabs = []

    for k in data:
        df = DataFrame(data[k])

        groups = df.groupby('effect', sort=True)
        categories = [x[0] for x in list(groups)]

        hex_cols = color_palette(n_colors=len(categories)+1).as_hex()

        boxplot_cols = hex_cols[:-1]
        point_col = hex_cols[-1]

        q1 = groups.quantile(q=0.25)
        q2 = groups.quantile(q=0.5)
        q3 = groups.quantile(q=0.75)
        qmin = groups.quantile(q=0.00)
        qmax = groups.quantile(q=1.00)

        iqr = q3 - q1
        upper = q3 + 1.5*iqr
        lower = q1 - 1.5*iqr

        upper.value = [
            min([x, y]) for (x, y) in zip(list(qmax.iloc[:, 0]), upper.value)
        ]

        lower.value = [
            max([x, y]) for (x, y) in zip(list(qmin.iloc[:, 0]), lower.value)
        ]

        boxplot = figure(
            x_range=categories,
            title=k,
            tools=_PLOT_TOOLS,
            width=_WIDTH,
            height=_HEIGHT,
        )

        # Stems
        boxplot.segment(
            categories,
            upper.value,
            categories,
            q3.value,
            line_width=2,
            line_color='black'
        )

        boxplot.segment(
            categories,
            lower.value,
            categories,
            q1.value,
            line_width=2,
            line_color='black'
        )

        width = _WIDTH // len(categories) // 3

        # Boxes
        boxplot.rect(
            x=categories,
            y=(q3.value+q2.value)/2,
            width=width,
            height=q3.value-q2.value,
            fill_color=hex_cols[:-1],
            line_width=1,
            line_color='black',
            width_units='screen',
        )

        boxplot.rect(
            x=categories,
            y=(q2.value+q1.value)/2,
            width=width,
            height=q2.value-q1.value,
            fill_color=boxplot_cols,
            line_width=1,
            line_color='black',
            width_units='screen',
        )

        # Whiskers (almost-0 height rects; simpler than segments)
        whisker_height = 1
        whisker_width = width//2

        boxplot.rect(
            x=categories,
            y=lower.value,
            width=whisker_width,
            height=whisker_height,
            line_color='black',
            width_units='screen',
            height_units='screen',
        )

        boxplot.rect(
            x=categories,
            y=upper.value,
            width=whisker_width,
            height=whisker_height,
            line_color='black',
            width_units='screen',
            height_units='screen',
        )

        # Data points
        boxplot.add_glyph(
            ColumnDataSource(data[k]),
            Circle(
                x='effect',
                y='value',
                fill_color=point_col,
                fill_alpha=0.3,
                line_alpha=0.3,
                size=8,
            )
        )

        boxplot.xgrid.grid_line_color = None
        boxplot.ygrid.grid_line_color = None
        boxplot.xaxis.major_label_text_font_size = '12pt'

        tabs.append(Panel(child=boxplot, title=k))

    return components(Tabs(tabs=tabs))

def _roc_plot(data):
    '''Returns a (JS script, div) tuple for plot generation, both in UTF-8.'''
    roc_curve = figure(
        plot_width=_WIDTH,
        plot_height=_HEIGHT,
        x_axis_label='1 - Specificity',
        y_axis_label='Sensitivity',
        tools=_PLOT_TOOLS,
    )

    hex_cols = color_palette(n_colors=len(data)).as_hex()

    circ_glyphs = []
    leg_txt = '{algo} (AUC: {auc:4.2f}, 95% CI ({lower:4.2f}, {upper:4.2f}))'

    for col, line in zip(hex_cols, data):
        fpr_tpr = line['coords']
        fpr, tpr = zip(*fpr_tpr)

        thres = line['thresholds']

        col_src = ColumnDataSource({
            'fpr': fpr,
            'tpr': tpr,
            'thres': thres,
            'specificity': [1-x for x in fpr]
        })

        lower, auc, upper = line['auc']

        legend = leg_txt.format(
            algo=line['algorithm'],
            auc=auc,
            lower=lower,
            upper=upper,
        )

        roc_curve.line(
            x='fpr',
            y='tpr',
            source=col_src,
            color=col,
            legend=legend,
            line_width=1.5,
        )

        circ_glyphs.append(roc_curve.circle(
            x='fpr',
            y='tpr',
            source=col_src,
            color=col,
            size=6,
            alpha=0.5,
        ))

    # Hover tool display

    tooltips = [
        ('Threshold', '@thres'),
        ('(Specificity, Sensitivity)', '(@specificity, @tpr)'),
    ]

    roc_curve.add_tools(HoverTool(
        tooltips=tooltips,
        renderers=circ_glyphs,
        mode='mouse',
    ))

    # The y = x reference line

    x = [0.03, 0.97]
    roc_curve.line(x, x, color='grey', line_width=0.75, line_dash=[4, 4])

    # High sens/spec region lines

    x, y = [0.225, 0.225], [0, 1]
    roc_curve.line(x, y, color='grey', line_width=0.75, line_dash=[2, 2])

    x, y = [0, 1], [0.775, 0.775]
    roc_curve.line(x, y, color='grey', line_width=0.75, line_dash=[2, 2])

    # Plot annotation

    roc_curve.title = 'ROC Curve'
    roc_curve.grid.grid_line_color = None
    roc_curve.legend.orientation = 'bottom_right'

    return components(roc_curve)

def _scatterplot(x):
    encoding = x["encoding"]

    x_field = encoding["x"]["field"]
    y_field = encoding["y"]["field"]

    data = x["data"]

    if "values" in data:
        values = data["values"]
    elif "url" in data:
        url = data["url"]
        data_type = data.get("type")

        values = _get_values(url, data_type)
    else:
        _error(x, ValueError)

    xy = [(record[x_field], record[y_field]) for record in values]
    x, y = zip(*xy)
    
    #radii = np.random.random(size=N) * 1.5
    #colors = ["#%02x%02x%02x" % (r, g, 150) for r, g in zip(np.floor(50+2*x), np.floor(30+2*y))]
    
    scatter_plot = figure(tools=_PLOT_TOOLS, plot_width=_WIDTH, plot_height=_HEIGHT)
    
    #p.scatter(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

    scatter_plot.scatter(x, y, fill_alpha=0.6, line_color=None)

    #return sns.lmplot(x=x_field, y=y_field, data=data_f, fit_reg=False)

    return components(scatter_plot)

def render(json_str):
    '''Renders a graphic according to the given JSON string through matplotlib.

    Args:
        json_str : A valid graphics specification JSON string.
    '''
    schema_file = _os.path.join(
        _os.path.dirname(__file__),
        '..',
        'graphics_schema.json',
    )

    with open(schema_file) as f:
        json_schema = _json.load(f)

    validator = _load(json_schema)

    graphics_spec = _json.loads(json_str)

    try:
        validator.validate(graphics_spec)
    except _ValidationError:
        raise ValueError('Given JSON graphics specification invalid.')

    mark = graphics_spec['mark']
    encoding = graphics_spec['encoding']
    data = graphics_spec['data']

    xfield, yfield = _extract_xyfields(encoding)
    xtype, ytype = _extract_xytypes(encoding)

    col_field, col_type, col_map = None, None, None
    if 'color' in encoding:
        color = encoding['color']

        col_field = _extract_col_field(color)
        col_type = _extract_col_type(color)

        if 'scale' in color:
            col_map = _extract_color_mapping(color['scale'])

    col_vals = None
    if col_field:
        x, y, col_vals = _extract_field_vals(data, xfield, yfield, col_field)
        x, y, col_vals = _convert_types(x, xtype, y, ytype, col_vals, col_type)
    else:
        x, y = _extract_field_vals(data, xfield, yfield)
        x, y = _convert_types(x, xtype, y, ytype)

    if _is_match('bar', mark):
        return _barchart(x, y)
    elif _is_match('point', mark):
        return _scatter_plot(x, xfield, y, yfield)
    elif _is_match('line', mark):

        if col_field is None:
            return _line_plot(x, y)
        else:
            if col_vals is None:
                raise ValueError('Color values must be specified.')

            return _multiline_plot(x, xfield, y, yfield, col_vals, col_field, col_map)

    elif _is_match('heatmap', mark):
        return _heatmap(x, xfield, y, yfield, col_vals, col_field)
    elif _is_match('boxplot', mark):
        return _boxplot(x, xfield, y, yfield)
    else:
        raise ValueError('Not a valid mark: {}.'.format(mark))
    
    return ''

def _barchart(x, y):
    '''Renders a barchart.

    Args:
        x : A list of categorical data.
        y : A list of numerical data (the heights of the bars).
    '''
    _plt.bar(range(len(x)), y, align='center')
    _plt.xticks(range(len(x)), x)
    
    return _plt


#def _scatter_plot(x, xfield, y, yfield):
    #'''Renders a scatter plot.

    #Args:
        #x : A list of numerical data.
        #xfield : A string containing the name of the given x list.
        #y : A list of numerical data.
        #yfield : A string containing the name of the given y list.
    #'''
    #data_f = DataFrame({xfield: x, yfield: y})
    #sns.lmplot(x=xfield, y=yfield, data=data_f, fit_reg=False)

    #return sns.plt

#def _boxplot(x, xfield, y, yfield):
    #'''Renders a boxplot.

    #Args:
        #x : A list of categorical data.
        #xfield : A string containing the name of the given x list.
        #y : A list of numerical data for boxplot stats calculation.
        #yfield : A string containing the name of the given y list.
    #'''
    #data_f = DataFrame({xfield: x, yfield: y})
    #sns.boxplot(x=xfield, y=yfield, data=data_f)

    #return sns.plt

def _line_plot(x, y, color=None):
    '''Renders a line plot.

    Args:
        x : A list of numerical data.
        y : A list of numerical data.
        color (optional) : The color of the line.
    '''
    if color is None:
        _plt.plot(x, y)
    else:
        _plt.plot(x, y, color=color)
    
    return _plt

def _multiline_plot(x, xfield, y, yfield, col_vals, col_field,
                    col_mapping=None):
    '''Renders a multiline plot.

    Args:
        x : A list of numerical data.
        xfield : A string containing the name of the given x list.
        y : A list of numerical data.
        yfield : A string containing the name of the given y list.
        col_vals : Categorical values for color specifiction.
        col_field : A string containing the name of the col_vals list.
        col_mapping (optional) : A dict mapping the col_vals categories to
                                 colors.
    '''
    data_f = DataFrame({xfield: x, yfield: y, col_field: col_vals})
    groups = data_f.groupby(col_field)

    col_field_names = []
    for name, group in groups:
        col_field_names.append(name)

        if col_mapping is not None:
            _plt.plot(
                group.get(xfield),
                group.get(yfield),
                col_mapping[name],
            )
        else:
            _plt.plot(group.get(xfield), group.get(yfield))

    _plt.legend(col_field_names)
    
    return _plt    

def _heatmap(x, xfield, y, yfield, col_vals, col_field):
    '''Renders a multiline plot.

    Args:
        x : A list of categorical data.
        xfield : A string containing the name of the given x list.
        y : A list of categorical data.
        yfield : A string containing the name of the given y list.
        col_vals : Numerical values for the cell color generation.
        col_field : A string containing the name of the col_vals list.
    '''

    data_f = DataFrame({xfield: x, yfield: y, col_field: col_vals})

    ax = sns.heatmap(data_f.pivot(xfield, yfield, col_field))

    if len(x) > 20:
        ax.xaxis.set_visible(False)
    elif len(y) > 20:
        ax.yaxis.set_visible(False)
        
    return sns.plt

def _is_match(pattern, string):
    '''Returns true iff string is a full case insensitive match of pattern.'''
    return _re.fullmatch(pattern, string, _re.IGNORECASE) is not None


def _get_data_from_uri(uri, data_type):
    req = _request.urlopen(uri)

    content_charset = req.headers.get_content_charset()
    content_subtype = req.headers.get_content_subtype()

    if data_type != content_subtype:
        raise TypeError('Content uri type must match that requested.')

    if data_type is None or data_type == 'json':
        if content_charset is None:
            content_charset = 'utf-8'

        content = str(req.read(), content_charset)
        values = _json.loads(content)
    elif data_type == 'csv':
        content = str(req.read(), content_charset)
        values = _process_sep_content(content, ',')
    elif data_type == 'tsv':
        content = str(req.read(), content_charset)
        values = _process_sep_content(content, '\t')

    return values


def _process_sep_content(content, sep):
    '''Gets a list of dicts, with the header of content as keys.'''
    header, lines = _get_header_lines(content)
    header = header.split(sep)
    return [dict(zip(header, line.split(sep))) for line in lines]


def _get_header_lines(content):
    '''Gets a tuple of (header, lines) from content.'''
    data = content.split(_os.linesep)
    return data[0], data[1:]


def _convert_types(x, xtype, y, ytype, z=None, ztype=None):
    x = [_type_conversion(i, xtype) for i in x]
    y = [_type_conversion(i, ytype) for i in y]

    if z:
        z = [_type_conversion(i, ztype) for i in z]
        return x, y, z
    else:
        return x, y


def _type_conversion(z, ztype):
    if _is_match('quantitative', ztype) or _is_match('q', ztype):
        z = float(z)
    elif _is_match('temporal', ztype) or _is_match('t', ztype):
        year, mon, day = _extract_date_info(z)
        z = _datetime.date(year, mon, day)
    elif _is_match('ordinal', ztype) or _is_match('o', ztype):
        z = str(z)
    elif _is_match('nominal', ztype) or _is_match('n', ztype):
        z = str(z)
    else:
        raise ValueError('Not a valid type: {}.'.format(ztype))

    return z


def _extract_color_mapping(scale):
    '''Processes info from the color scale attribute.

    Returns a dict mapping the value of the coloring field (keys) to the
    display color (values).
    '''
    domain = scale['domain']
    col_scale = scale['range']

    col_mapping = {k: v for k, v in zip(domain, col_scale)}

    return col_mapping


def _extract_date_info(z):
    '''Extracts the date info (Y, M, D) from a string temporal data point.'''
    year = _re.search('\d\d\d\d', z).group()
    mon = _re.search('[a-zA-Z]+', z).group()

    mon_abbr = {k.lower(): v for v, k in enumerate(_cal.month_abbr)}
    mon_name = {k.lower(): v for v, k in enumerate(_cal.month_name)}

    if mon.lower() in mon_abbr:
        mon_numeric = mon_abbr[mon.lower()]
    elif mon.lower() in mon_name:
        mon_numeric = mon_abbr[mon.lower()]
    else:
        raise ValueError('Not a valid month: {}.'.format(mon))

    z = z.replace(year, '')
    z = z.replace(mon, '')

    day = z.strip(' ,')

    return int(year), int(mon_numeric), int(day)


def _extract_xytypes(encoding):
    xtype = encoding['x']['type']
    ytype = encoding['y']['type']

    return xtype, ytype


def _extract_xyfields(encoding):
    xfield = encoding['x']['field']
    yfield = encoding['y']['field']

    return xfield, yfield


def _extract_col_type(color):
    return color['type']


def _extract_col_field(color):
    return color['field']


def _extract_field_vals(data, xfield, yfield, cfield=None):
    if 'values' in data:
        values = data['values']
    elif 'url' in data:
        url = data['url']
        data_type = data.get('formatType') if data.get('formatType') else \
            'json'

        values = _get_data_from_uri(url, data_type)
    else:
        raise ValueError('Not a valid data source.')

    if cfield:
        xyc = [
            (rec[xfield], rec[yfield], rec[cfield]) for rec in values
            if rec[xfield] is not None and rec[yfield] is not None and
            rec[cfield] is not None
        ]
        zipped = zip(*xyc)
    else:
        xy = [
            (rec[xfield], rec[yfield]) for rec in values
            if rec[xfield] is not None and rec[yfield] is not None
        ]
        zipped = zip(*xy)

    return zipped

def _boxplot(x, xfield, y, yfield):
    '''Renders a boxplot.

    Args:
        x : A list of categorical data.
        xfield : A string containing the name of the given x list.
        y : A list of numerical data for boxplot stats calculation.
        yfield : A string containing the name of the given y list.
    '''
    data_f = pd.DataFrame({xfield: x, yfield: y})
    return sns.boxplot(x=xfield, y=yfield, data=data_f)

def _scatter_plot(x, xfield, y, yfield):
    '''Renders a scatter plot.

    Args:
        x : A list of numerical data.
        xfield : A string containing the name of the given x list.
        y : A list of numerical data.
        yfield : A string containing the name of the given y list.
    '''
    data_f = pd.DataFrame({xfield: x, yfield: y})
    return sns.lmplot(x=xfield, y=yfield, data=data_f, fit_reg=False)