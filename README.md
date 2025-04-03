# inst414_project

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Project Descriptions

A quantitative social science research project exploring the linear relationships between the amount of education an individual recieves and their income level.

## Dependencies

The following Python libraries and tools are required to run this project:

- `pandas`  #Data manipulation and analysis
- `numpy`  #Numerical operations
- `matplotlib`  #Data visualization
- `seaborn`  #Statistical data visualization
- `scikit-learn`  #Machine learning algorithms and tools
- `statsmodels`  #Statistical models
- `scipy`  #Statistical functions
- `flake8`  #Code linting
- `black`  #Code formatting
- `mkdocs`  #Documentation generation

**To install all dependencies, run:**
- pip install -r requirements.txt

## Setting up the environment

To set up your environment for this project, you can use a virtual environment. The following instructions assume you are using `pip` and `virtualenv`:

1. **Create a virtual environment:**

   ```bash
   python -m venv venv

2. **Activate the virtual environment:**

    On Windows:
    - venv\Scripts\activate

    On macOS/Linux:
    - source venv/bin/activate

3. **Install depdendencies**
    - pip install -r requirements.txt

## Running the data processing pipeline
    
The data processing pipeline is located in `testing_correlation/dataset.py` and includes scripts to download and process the dataset. To run the pipeline, follow these steps:

1. **Download and process the dataset:**

   If the dataset is not processed, you can run the following script to download and process the data:

   python testing_correlation/dataset.py

   Once the data has been processed, you can train and evaluate the model using the following steps:

## Training and evaluating the model:

1. **Model training**

   The training script is located in `testing_correlation/modeling/train.py`. To train the model, run:

   python testing_correlation/modeling/train.py

2. **Model evaluation:**

   After training the model, evaluation is performed using several diagnostic plots, which can be found in testing_correlation/plots.py. These include residual plots, Q-Q plots, and others. Run the following script to generate the plots:

   python testing_correlation/plots.py

   The results will be saved in the reports folder

## Reproducing results

To reproduce the results of this project, you can follow these steps:

1. **Clone the repository and set up the environment:**

   Follow the instructions under the "Setting Up the Environment" section to set up a virtual environment and install dependencies.

2. **Run the data processing pipeline:**

   Follow the "Running the Data Processing Pipeline" section to download and process the dataset.

3. **Train the model:**

   Use the instructions in the "Evaluating Models" section to train the model and evaluate it.

4. **Review Results:**

   All results, including plots and model evaluations, will be stored in the `reports` folder. You can view the generated plots to analyze the performance of the model.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         testing_correlation and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── testing_correlation   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes testing_correlation a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

