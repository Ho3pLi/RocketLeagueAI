
# Are you good at RL or not?

**Italian**

Questo progetto utilizza il machine learning per creare un modello di predizione della bravura di un giocatore in Rocket League. Il modello è creato utilizzando il framework TensorFlow in Python e viene addestrato su un dataset che contiene i dati dei giocatori, come il punteggio, il tempo di gioco, i goal, gli assist e le salvate. In particolare, il modello utilizza come target la colonna "AI score" del dataset, dove 1 indica che un giocatore è bravo mentre 0 indica che un giocatore non è bravo.

Il dataset utilizzato è stato fornito dall'utente che ha creato il progetto e consiste in un file CSV.

**English**

This project is a machine learning model that (should) predicts whether a player is good or not at the video game Rocket League based on their game statistics. The model is built using Python and TensorFlow.

The dataset used for this project is a CSV file containing various statistics for Rocket League matches. The AI score column is used as the target variable, with 1 indicating a good player and 0 indicating a bad player.

The model is built using TensorFlow, an open-source machine learning framework. It consists of a neural network with several hidden layers and is trained using the Adam optimization algorithm. The model achieves an accuracy of around 80%.




## Badges


[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

![GitHub last commit](https://img.shields.io/github/last-commit/Ho3pLi/RocketLeagueAI)

![GitHub repo size](https://img.shields.io/github/repo-size/Ho3pLi/RocketLeagueAI)
## Requirements

- Python 3.x
- Tensorflow
- Pandas


## Installation & Usage

**Italian**

Per usare il modello, lanciare il file 'main.py' nella cartella AI e inserire nella variabile 'dataset' il nome del file csv che contiene le statistiche di un giocatore di Rocket League. Il modello ritornerà una predizione dicendo se il giocatore è bravo oppure no.

**English**

To use the model, simply run the main.py script and provide the statistics for a Rocket League player. The script will output a prediction of whether the player is good or not.


## Support

For support, email daniele.barile.lavoro@gmail.com or just open an issue.


## License

[GPL v3](https://choosealicense.com/licenses/gpl-3.0/)

## Authors

- [@Ho3pLi](https://www.github.com/Ho3pLi)

