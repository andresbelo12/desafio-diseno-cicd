import test
import demandPrediction

def main():
    model = demandPrediction.DemandPrediction()
    model.initialize()
    test.test(model)

main()
