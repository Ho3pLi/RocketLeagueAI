import pandas as pd
from tensorflow import keras
from sklearn.model_selection import train_test_split

def tensorFlowModel(dataset):
    data = pd.read_csv(dataset)

    X = data.drop(['AI score'], axis=1)
    y = data['AI score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # X_train = pd.get_dummies(X_train, columns=['color', 'platform', 'car name'])
    # X_test = pd.get_dummies(X_test, columns=['color', 'platform', 'car name'])

    numerical_cols = ['game duration', 'score', 'goals', 'assists', 'saves', 'shots', 'shots conceded', 
                      'goals conceded', 'goals conceded while last defender', 'shooting percentage', 'bpm', 
                      'avg boost amount', 'amount collected', 'amount collected big pads', 'amount collected small pads', 
                      'count collected big pads', 'count collected small pads', 'amount stolen', 'amount stolen big pads', 
                      'amount stolen small pads', 'count stolen big pads', 'count stolen small pads', '0 boost time', 
                      '100 boost time', 'amount used while supersonic', 'amount overfill total', 'amount overfill stolen', 
                      'avg speed', 'total distance', 'time slow speed', 'percentage slow speed', 'time boost speed', 
                      'percentage boost speed', 'time supersonic speed', 'percentage supersonic speed', 'time on ground', 
                      'percentage on ground', 'time low in air', 'percentage low in air', 'time high in air', 
                      'percentage high in air', 'time powerslide', 'avg powerslide time', 'count powerslide', 
                      'time most back', 'time most forward', 'avg distance to ball', 'avg distance to ball has possession', 
                      'avg distance to ball no possession', 'time behind ball', 'percentage behind ball', 
                      'time in front of ball', 'percentage in front of ball', 'time defensive half', 
                      'percentage defensive half', 'time offensive half', 'percentage offensive half', 'time defensive third', 
                      'percentage defensive third', 'time neutral third', 'percentage neutral third', 'time offensive third', 
                      'percentage offensive third', 'demos inflicted', 'demos taken']
    mean = X_train[numerical_cols].mean()
    std = X_train[numerical_cols].std()
    X_train[numerical_cols] = (X_train[numerical_cols] - mean) / std
    X_test[numerical_cols] = (X_test[numerical_cols] - mean) / std

    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=[X_train.shape[1]]),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=1000, batch_size=32)

    score, accuracy = model.evaluate(X_test, y_test)
    print('Test score:', score)
    print('Test accuracy:', accuracy)
