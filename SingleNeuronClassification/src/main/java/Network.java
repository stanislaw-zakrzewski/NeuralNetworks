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
        if(result > 0.5) result = 1;
        else  result  = 0;
        return result;
    }

    public void adapt(Example example) {
        double result = work(example.getInputs());
        double resultOffset = example.getDestiresResult() - result;

        for (int i = 0; i < inputCount; i++) {
            double weightChange = resultOffset * -example.getInputs().get(i);
            neuron.getWeigths().set(i, neuron.getWeigths().get(i) - learningRate * weightChange);
        }
    }
}
