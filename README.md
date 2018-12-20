# FIFA_Rating

Given all details like personal attributes, playing/performance attributes, rating at each position etc about all the players in FIFA 18, predict how good a player is overall and how efficient he is at each role.

Dataset Used (Publicly avaliable): [kevinmh/fifa-18-more-complete-player-dataset](https://www.kaggle.com/kevinmh/fifa-18-more-complete-player-dataset)

## Repo details

- [Pickle_models](Pickle_models): Contains all the pickled models.
- [Visualisations](Visualisations): All the visualisations done in the code are saved here.
- [FIFA_Rating.ipynb](FIFA_Rating.ipynb): Jupyter notebook containing main code with all the feature engineering, visualisations and model building.
- [complete.csv](complete.csv): Main dataset that is being used here.
- [FIFA_Rating.py](FIFA_Rating.py): Python file for the same Jupyter notebook.
- [Testing.ipynb](Testing.ipynb): Jupyter notebook containing model testing code.
- [test.csv](test.csv): Testing dataset produced for the testing code.
- [Testing.py](Testing.py): Python file for the same Jupyter notebook.
- [FIFA_Rating.pdf](FIFA_Rating.pdf): Actual report of our findings and approach to this problem with different results.

### Main code
```
$ python3 FIFA_Rating.py
```
OR <br>
```
$ jupyter notebook
```
and then run the `FIFA_Rating.ipynb` notebook.

### Test models
```
$ python3 Testing.py
```
OR <br>
```
$ jupyter notebook
```
and then run the `Testing.ipynb` notebook.

**Note:** Make necessary changes in both `.py` or `.ipynb` files regarding what models to build or to test.
