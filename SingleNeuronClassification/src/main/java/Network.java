import java.util.List;

public class Network {
    private Neuron neuron;
    private int inputCount;
    private double learningRate;

    public Network(int inputCount) {
        neuron = new Neuron(inputCount);
        this.inputCount = inputCount;
        learningRate = 0.01;
    }

    public double work(List<Double> inputs) {
        double result = 0;
        for (int i = 0; i < inputCount; i++) {
            result += neuron.getWeigths().get(i) * inputs.get(i);
        }
        return result;
    }

    public void adapt(List<Double> inputs, double desiredResult) {
        double result = work(inputs);
        double resultOffset = desiredResult - result;

        for (int i = 0; i < inputCount; i++) {
            double weightChange = resultOffset * -inputs.get(i);
            neuron.getWeigths().set(i, neuron.getWeigths().get(i) - learningRate * weightChange);
        }
    }
}
