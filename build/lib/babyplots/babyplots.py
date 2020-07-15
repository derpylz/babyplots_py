import os
from uuid import uuid4
import json
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

    def add_plot(self, coordinates, plot_type, color_by, color_var, options = {}):
        self.plots.append(
            {
                'coordinates': coordinates,
                'plot_type': plot_type,
                'color_by': color_by,
                'color_var': color_var,
                'options': options
            }
        )


    def _repr_html_(self):
        display_id = str(uuid4()).replace('-', '_')


        html = JENV.get_template('plot.html')
        output = html.render(baby=self, display_id=display_id)
        # print(output)
        return output
