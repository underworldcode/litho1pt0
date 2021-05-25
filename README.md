# Litho1pt0


`litho1pt0` is a python interface to the _crust 1.0_ dataset and the lithospheric part of the _litho 1.0_ dataset (Laske et al, 2013 and Pasyanos et al, 2014) which both requires and demonstrates the triangulation / searching and interpolation on the sphere that is provided by `stripy`.


## Navigation / Notebooks



```bash
   python -c 'import litho1pt0; litho1pt0.documentation.install_documentation(path="Notebooks")'
```

The first three notebooks are an introduction to `litho1pt0` 
the next two worked examples show how to search, interpolate and plot with the help of `stripy` routines.
`stripy is a dependency`

  - [Ex1-Litho1Layers.ipynb](litho1pt0-src/litho1pt0/Notebooks/litho1pt0/Ex1-Litho1Layers.ipynb)
  - [Ex2-Litho1Properties.ipynb](litho1pt0-src/litho1pt0/Notebooks/litho1pt0/Ex2-Litho1Properties.ipynb)
  - [Ex3-CrustalRegionalisation.ipynb](litho1pt0-src/litho1pt0/Notebooks/litho1pt0/Ex3-CrustalRegionalisation.ipynb)
  - [WorkEx1-CratonAverageProperties.ipynb](litho1pt0-src/litho1pt0/Notebooks/litho1pt0/WorkEx1-CratonAverageProperties.ipynb)
  - [WorkEx2-OceanDepthAge.ipynb](litho1pt0-src/litho1pt0/Notebooks/litho1pt0/WorkEx2-OceanDepthAge.ipynb)


## Installation

### Dependencies

You will need **Python 3.5 or greater**.
Also, the following packages are required:

 - [`stripy`]()
 - [`gfortran`](https://www.fatiando.org/verde/latest/install.html) (or any Fortran compiler)
 - [`numpy`](http://numpy.org)

### Installing using pip

You can install `litho1pt0` and the `stripy` dependency using the
[`pip package manager`](https://pypi.org/project/pip/):

```bash
pip install [--user] litho1pt0 stripy
```

The dependencies will be automatically installed by `pip`, except for `gfortran`
(or any Fortran compiler). It must be installed in your system before installing
`stripy` with `pip`.

### Documentation

Automatically populated to [underworldcode.github.io/litho1pt0](https://underworldcode.github.io/litho1pt0)




