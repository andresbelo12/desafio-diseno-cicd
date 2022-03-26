import demandPrediction
import numpy as np

def unitTest(model):
    spected_sales = np.array([[3,4,4,4,3,5,3,6]], int)
    spected_sales = np.rot90(spected_sales, 3)

    spected_demand = np.array([[3,4,4,4,3,5,3,6]], int)
    spected_demand = np.rot90(spected_demand, 3)

    real_sales = model.sales[:8]
    real_demand = model.demand[:8]
    assert np.array_equal(real_sales, spected_sales) and np.array_equal(real_demand, spected_demand)

def scoreTest(model):
    score = model.test
    assert score > 0.95

def test(model):
    unitTest(model)
    print('unit test passed')
    scoreTest(model)
    print('score model test passed')

    


