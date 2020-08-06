import os
from functools import reduce
from uuid import uuid4
import json
import numpy as np
from skimage import io
from skimage.util import img_as_float
from IPython.display import HTML, Javascript, display
import jinja2


dirname = os.path.dirname(
    os.path.realpath(__file__)
)

t_loader = jinja2.FileSystemLoader(os.path.join(dirname, 'templates'))
JENV = jinja2.Environment(loader=t_loader)


class Babyplot(object):
    def __init__(self, width=640, height=480, background_color="#ffffffff", turntable=False, rotation_rate=0.01):
        self.plots = []
        self.turntable = turntable
        self.rotation_rate = rotation_rate
        self.width = width
        self.height = height
        self.background_color = background_color
        bpjs_file = os.path.join(
            dirname,
            'js/babyplots.js'
        )
        with open(bpjs_file, 'r', encoding="utf8") as infile:
            bpjs = infile.read()
        display(Javascript(bpjs))

    @staticmethod
    def format_json(prop):
        return json.dumps(prop)

    def add_plot(self, coordinates, plot_type, color_by, color_var, options={}):
        self.plots.append(
            {
                'coordinates': coordinates,
                'plot_type': plot_type,
                'color_by': color_by,
                'color_var': color_var,
                'options': options
            }
        )

    def add_img_stack(self, values, indices, attributes, options={}):
        self.plots.append(
            {
                'values': values,
                'indices': indices,
                'attributes': attributes,
                'options': options
            }
        )

    def add_tiff(self, image_path, threshold=0.1, channel_thresholds=None, options={}):
        im = img_as_float(io.imread(image_path)) # im shape: z, x, y, c
        # if image has no color channels, adjust dimensions
        if len(im.shape) == 3:
            im = np.expand_dims(im, axis=-1)
        # set shape attribute
        attributes = {
            "dim": [im.shape[1], im.shape[2], im.shape[3], im.shape[0]]
        }
        # apply channel-wise thresholds if given.
        if channel_thresholds is not None:
            for i, thres in enumerate(channel_thresholds):
                mask = im[:, :, :, i] < thres
                im[:, :, :, i][mask] = 0
        # reorder dimensions to that flatten gives the same order as R equivalent
        im = np.transpose(im, (0, 3, 2, 1)) # im shape becomes z, c, y, x
        # flatten
        n_vals = reduce(lambda x, y: x*y, im.shape)
        im = np.reshape(im, n_vals)
        # find indices of values larger than threshold
        # single threshold is ignored when per channel thresholds are given
        if channel_thresholds is None:
            idcs = np.argwhere(im > threshold).squeeze()
        else:
            idcs = np.argwhere(im > 0).squeeze()
        # only keep non-zero values
        im = im[idcs].tolist()
        idcs = idcs.tolist()

        self.add_img_stack(im, idcs, attributes, options)

    def _repr_html_(self):
        display_id = str(uuid4()).replace('-', '_')

        is_plot = "plot_type" in self.plots[0]
        html = JENV.get_template('plot.html')
        output = html.render(baby=self, display_id=display_id, is_plot=is_plot)
        return output
