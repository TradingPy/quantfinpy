# quantfinpy

Quantitative finance in python.

## Context

This project is still in the early development phase and is mostly an educational experience for now.

## Credits

Most of the initial design and logic is derived from : Options, Futures, and Other Derivatives (10th Edition) by 
John C. Hull

## Testing

As the project is still in its early development phase, the testing doesn't cover most of the edge cases and 
some of the underlying interfaces.
As the project becomes more mature and the interfaces become more stable, more tests will be added.
Testing is done via tox and covers static checks + pytest testing.

## Documentation

The [documentation](https://quantfinpy.readthedocs.io/) is generated with sphinx and autodoc when running the tox action. 
If the sphinx command fails with an error mentioning missing modules and these missing modules have just been deleted, 
it means that you need to delete doc/source/_autosummary folder and rerun tox.

## Installation

**End user:**

$ pip install quantfinpy

**Developer**

Running the tox.ini with [tox](https://tox.wiki/en/latest/)

## Contributing 

Contributions are welcome. Please follow this [document](https://github.com/TradingPy/quantfinpy/blob/main/CONTRIBUTING.md) for more information.
