# Rocket League Player Skill Predictor

This project is a machine learning model that (should) predicts whether a player is good or not at the video game Rocket League based on their game statistics. The model is built using Python and TensorFlow.

## Dataset

The dataset used for this project is a CSV file containing various statistics for Rocket League matches. The `AI score` column is used as the target variable, with 1 indicating a good player and 0 indicating a bad player.

## Model

The model is built using TensorFlow, an open-source machine learning framework. It consists of a neural network with several hidden layers and is trained using the Adam optimization algorithm. The model achieves an accuracy of around 80%.

## Usage

To use the model, simply run the `main.py` script and provide the statistics for a Rocket League player. The script will output a prediction of whether the player is good or not.

## Requirements

- Python 3.x
- TensorFlow
- Pandas

## Credits

This project was created by [Ho3pLi]. The dataset used for this project was obtained from https://ballchasing.com and formatted with my scripts.

## License

This project is licensed under the GPLv3 License - see the LICENSE file for details.
