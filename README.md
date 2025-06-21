# pls-module
Python package for IPLS using identified peak areas in the spectra

### Notes
 * Package can be used by creating a `PLSModeller` instance, which can be used to open `.csv` files, trim data, apply preprocessing, and create a PLR regression model.
  * The package also uses the `brukeropusreader` package for opening spectra files with `.0` file extension.

### Testing
  * Run the ff on main directory. It should give out the performance metrics, along with the settings, for each model created.
```
poetry run python main.py
```

### Dependencies
 * scipy
 * pandas
 * scikit-learn
 * brukeropusreader

 