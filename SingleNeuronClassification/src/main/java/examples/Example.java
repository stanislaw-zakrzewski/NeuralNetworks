package examples;

import java.util.ArrayList;
import java.util.List;

public class Example {
    private List<Double> inputs;
    private double destiresResult;

    public Example(double x, double y, double desiredResult) {
        inputs = new ArrayList<>();
        inputs.add(x);
        inputs.add(y);
        this.destiresResult = desiredResult;
    }

    public List<Double> getInputs() {
        return inputs;
    }

    public double getDestiresResult() {
        return destiresResult;
    }
}
