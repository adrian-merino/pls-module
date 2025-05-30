# pls-module
Python package for IPLS using identified peak areas in the spectra

### Notes
 * Package can be used by creating a `PLSModeller` instance, which can be used to open `.csv` files, trim data, apply preprocessing, and create a PLR regression model.
  * The package also uses the `brukeropusreader` package for opening spectra files with `.0` file extension.

### Testing
  * Run `poetry run python main.py` on main directory.


### Dependencies
 * scipy
 * pandas
 * scikit-learn
 * brukeropusreader

 