#NOTE - Machine learning algorithm
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd
import numpy as np

#NOTE - K-means clustering without AI score
def kMeansClusteringFirst(dataset):
    df = pd.read_csv(dataset)
    features = ["goals", "assists", "saves", "shots"]
    # df[features] = (df[features] - df[features].mean()) / df[features].std()
    kmeans = KMeans(n_clusters=2).fit(df[features])
    labels = kmeans.labels_
    np.set_printoptions(threshold=len(labels))
    print('Labels: '+str(labels))

#NOTE - K-means clustering with AI score
def kMeansClusteringSecond(dataset):
    df = pd.read_csv(dataset)
    features = ["AI score"]
    # df[features] = (df[features] - df[features].mean()) / df[features].std()
    kmeans = KMeans(n_clusters=2, n_init=5).fit(df[features])
    labels = kmeans.labels_
    np.set_printoptions(threshold=len(labels))
    print(labels)

#NOTE - Algorithm
def machineLearningAlgorithm(dataset):
    # Load data
    df = pd.read_csv(dataset)

    # Prepare input features and target variable
    X = df[['game duration','score','goals','assists','saves','shots','shots conceded','goals conceded','goals conceded while last defender','shooting percentage','bpm','avg boost amount','amount collected','amount collected big pads','amount collected small pads','count collected big pads','count collected small pads','amount stolen','amount stolen big pads','amount stolen small pads','count stolen big pads','count stolen small pads','0 boost time','100 boost time','amount used while supersonic','amount overfill total','amount overfill stolen','avg speed','total distance','time slow speed','percentage slow speed','time boost speed','percentage boost speed','time supersonic speed','percentage supersonic speed','time on ground','percentage on ground','time low in air','percentage low in air','time high in air','percentage high in air','time powerslide','avg powerslide time','count powerslide','time most back','time most forward','avg distance to ball','avg distance to ball has possession','avg distance to ball no possession','time behind ball','percentage behind ball','time in front of ball','percentage in front of ball','time defensive half','percentage defensive half','time offensive half','percentage offensive half','time defensive third','percentage defensive third','time neutral third','percentage neutral third','time offensive third','percentage offensive third','demos inflicted','demos taken']]
    y = df['AI score']

    num_iterations = 100
    model_filename = 'model.pkl'

    for i in range(num_iterations):

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Choose a machine learning algorithm
        model = LogisticRegression()

        # Train the model
        model.fit(X_train, y_train)

        # Make predictions on the testing data
        y_pred = model.predict(X_test)

        # Evaluate the model's performance
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", accuracy)

        joblib.dump(model, model_filename)
