from IPython.display import HTML, Javascript, display
from uuid import uuid4


class Babyplot(object):
    def __init__(self, width="100%", height="100%", background_color="#ffffffff"):
        self.plots = []
        self.turntable = False
        self.rotation_rate = 0.01
        self.width = width
        self.height = height
        self.background_color = background_color

    def addPlot(self, coordinates, plot_type, color_by, color_var, options):
        self.plots.append(
            {
                'coordinates': coordinates,
                'plot_type': plot_type,
                'color_by': color_by,
                'options': options
            }
        )

    def _repr_html_(self):
        id = uuid4()
        return """<style>
                    canvas#plot {{
                        width: {bp.width};
                        height: {bp.height};
                        background-color: {bp.background_color};
                    }}
                    </style>
                    <canvas id="plot_{id}"></canvas>
                    <script>
                    function display() {{
                        var cnvs = document.getElementById("plot_{id}");
                        var ctx = cnvs.getContext("2d");
                        setInterval(function () {{
                            ctx.clearRect(0, 0, 100, 100);
                            ctx.fillStyle = "red";
                            ctx.fillRect(Math.random() * 10, Math.random() * 10, Math.random() * 50, Math.random() * 50);
                        }}, 100)
                    }}
                    display();
                    </script>""".format(bp=self, id=id)
