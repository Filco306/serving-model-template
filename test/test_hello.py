from src.model import Model


def test_model_prediction():
    model = Model()
    pred = model.predict(x=None)
    assert pred <= 1.0 and pred >= 0.0


def test_fit_function():
    assert isinstance(Model(), Model)
