package networkComponents;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Neuron {
    private List<Double> weigths;
    private Random random;

    public Neuron(int weigthsCount) {
        weigths = new ArrayList<Double>();
        random = new Random();

        for(int i = 0; i < weigthsCount; i++) {
            weigths.add(random.nextDouble());
        }
    }

    public List<Double> getWeigths() {
        return weigths;
    }

    public void addToWeight(int weightNumber, double valueToAdd) {
        weigths.get(weightNumber);
    }
}
