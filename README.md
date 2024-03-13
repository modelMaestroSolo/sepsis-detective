# sepsis-detective 

## Overview
A project focused on building a classification model to predict sepsis using machine learning techniques. The project also includes developing an API for seamless interaction with the model, aiding in early detection and intervention for sepsis.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

List key features or functionalities of your project.

## Installation

git clone https://github.com/modelMaestroSolo/sepsis-detective
cd your-project
pip install -r requirements.txt

## Usage
Explain how to use your project. Include code examples or screenshots if necessary

# Example usage command
python main.py --input data/input.csv --output results/output.csv

## Data Description
The provided data is a modified version of a publicly available data source, and is subject to copyright.

### Donor of database: 
                          The Johns Hopkins University
                          Johns Hopkins Road
                          Laurel, MD 20707
                          (301) 953-6231

### Licence agreement: 

The dataset can only be used for the purpose of this assignment. Sharing or distributing this data or using this data for any other commercial or non-commercial purposes is prohibited.


### Data Fields

| Column   Name                | Attribute/Target | Description                                                                                                                                                                                                  |
|------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID                           | N/A              | Unique number to represent patient ID                                                                                                                                                                        |
| PRG           | Attribute1       |  Plasma glucose|
| PL               | Attribute 2     |   Blood Work Result-1 (mu U/ml)                                                                                                                                                |
| PR              | Attribute 3      | Blood Pressure (mm Hg)|
| SK              | Attribute 4      | Blood Work Result-2 (mm)|
| TS             | Attribute 5      |     Blood Work Result-3 (mu U/ml)|                                                                                  
| M11     | Attribute 6    |  Body mass index (weight in kg/(height in m)^2|
| BD2             | Attribute 7     |   Blood Work Result-4 (mu U/ml)|
| Age              | Attribute 8      |    patients age  (years)|
| Insurance | N/A     | If a patient holds a valid insurance card|
| Sepssis                 | Target           | Positive: if a patient in ICU will develop a sepsis , and Negative: otherwise |

### Missing Attribute Values: Yes

## Technologies Used
List the main technologies, frameworks, and libraries used in your project.
- Python
- Pandas
- Scikit-learn

## Contributing
If you would like others to contribute to your project, provide guidelines on how to do so. Include information on how to report bugs, suggest improvements, or submit pull requests.

## License
Specify the license under which your project is distributed. For example:

This project is licensed under the MIT License.




