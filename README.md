# babyplots - Easy, fast, interactive 3D visualizations

Babyplots is an easy to use library for creating interactive 3d graphs for exploring and presenting data. This is the python API that allows you to create babyplots visualizations in Jupyter notebooks.

**Find the full documentation [here](https://bp.bleb.li/documentation/python).**


## Install

You can install the babyplots package using pip:

```sh
pip install babyplots
```

## Usage

Once imported, you can create a babyplots visualization using the Babyplot class and adding plots to it. To display your visualization, simply call the object:

```python
from babyplots import Babyplot

bp = Babyplot()

bp.add_plot(coordinates, "pointCloud", "categories", clusters, {"colorScale": "Paired"})

bp
```

Below is a minimal example using the Iris data set:

```python
import numpy as np
from sklearn import decomposition
from sklearn import datasets
from babyplots import Babyplot
np.random.seed(5)

iris = datasets.load_iris()
X = iris.data
y = iris.target

iris = datasets.load_iris()
X = iris.data
y = iris.target

bp_iris = Babyplot(background_color="#262626ff")

bp_iris.add_plot(X, "shapeCloud", "categories", y, {"shape": "sphere", "colorScale": "Set2", "showAxes": [True, True, True], "axisLabels": ["PC 1", "PC 2", "PC 3"]})

bp_iris
```

You can see this example (and a few more) in a demo notebook [here](https://derpylz.github.io/babyplots_py/).

## Full Documentation

For the complete documentation of babyplots and its python API, please visit [https://bp.bleb.li/documentation/python](https://bp.bleb.li/documentation/python).

## Support, Questions, Feedback, ...

Join our [Discord server](https://discord.gg/bbWxP8q)!

## Support the work on babyplots

Using babyplots will always be free for everybody. But if you really like it and want to show your appreciation, you may buy us a coffee :)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/D1D45DB4K)

## Also see:

* [babyplots_lib](https://github.com/derpylz/babyplots), the underlying javascript library
* Babyplots as an [R package](https://bitbucket.org/derpylz/babyplots)

Libraries used in babyplots:

* [Babylon.js](https://www.babylonjs.com/), the rendering engine
* [Chroma.js](https://gka.github.io/chroma.js/), the color conversion library
* [CCapture.js](https://github.com/spite/ccapture.js/), for capturing gifs

## Author

Babyplots was created by [Nils Trost](https://github.com/derpylz)

## License

Released under the [Apache 2.0 License](LICENSE).

Find the licenses of the included libraries [here](babyplots/js/babyplots.js.LICENSE.txt). Make sure to include this file if you use babyplots in your project.


