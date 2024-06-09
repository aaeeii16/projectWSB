from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
import pandas as pd

def testPredictFunc():
    # Use data from dashboard
    df = pd.read_csv('out.csv', index_col=0)

    # remove unnecessary columns
    del df["Dividends"]
    del df["Stock Splits"]

    # add Tomorrow column for predictions
    df["Tomorrow"] = df["Close"].shift(-1)
    # Add Target Column to check if tomorrow price is greater than today's close
    df["Target"] = (df["Tomorrow"] > df["Close"]).astype(int)

    # model - Random Forest
    model = RandomForestClassifier(n_estimators=100, min_samples_split=50, random_state=1)

    # Divide Data into train and test
    train = df.iloc[:-50]
    test = df.iloc[-50:]

    predictors = ["Open","High","Low","Close","Volume"]
    model.fit(train[predictors], train["Target"])

    horizons= [5,10,20,50]
    new_predictors = []

    for horizon in horizons:
        rolling_averages = df.rolling(horizon).mean()

        ratio_column = f"Close_ratio_{horizon}"
        df[ratio_column] = df["Close"] / rolling_averages["Close"]

        trend_column = f"Trend_{horizon}"
        df[trend_column] = df.shift(1).rolling(horizon).sum()["Target"]

        new_predictors += [ratio_column, trend_column]

    df = df.dropna()

    preds = model.predict(test[predictors])
    preds = pd.Series(preds, index = test.index)

    precision_score(test["Target"], preds)

    combined = pd.concat([test["Target"], preds], axis=1)



    def predict(train, test, predictors, model):
        model.fit(train[predictors], train["Target"])
        preds = model.predict_proba(test[predictors])[:,1]
        preds[preds >= .6] = 1
        preds[preds < .6] = 0
        preds = pd.Series(preds, index = test.index, name="Predictions")
        combined = pd.concat([test["Target"], preds], axis=1)
        return combined

    def backtest(data, model, predictors, start=100, step=50):
        all_predictions = []

        for i in range(start, data.shape[0], step):
            train = data.iloc[0:i].copy()
            test = data.iloc[i:(i + step)].copy()
            predictions = predict(train, test, predictors, model)
            all_predictions.append(predictions)
        return pd.concat(all_predictions)

    predictions = backtest(df, model, predictors)

# return precision score
    return precision_score(predictions["Target"], predictions["Predictions"])



