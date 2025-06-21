# pls-module
Python package for IPLS using identified peak areas in the spectra

### Notes
  * Package can be used by creating a `IPLSModeler` instance, which can be used to open `.csv` files, trim data, apply preprocessing, and create a PLR regression model.
  * The package will also be used to open the `brukeropusreader` package for opening spectra files with `.0` file extension.
  * Package is for creating PLS models with all possible combinations of specified configurations, which is the full-factorial approach design of experiments. This is helpful if all possible approaches to model creation for spectral data are to be explored.

### Testing
  * Run the ff on main directory. It should give out the performance metrics, along with the settings, for each model created.
```
poetry run python src/main.py
```

### Installation
  * Run the ff to install the package:
  ```
  pip install dist/<file name of wheel file>
  ```
  * To test if installation was successful, you can try to create an `IPLSModeler` object in python
  ```
  a = IPLSModeler()
  ```

### Dependencies
 * scipy
 * pandas
 * scikit-learn
 * brukeropusreader
 * pybaselines

 