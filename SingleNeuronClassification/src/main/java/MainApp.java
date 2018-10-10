import examples.Examples;
import networkComponents.Network;
import plotting.DataForPlot;
import plotting.Plot;

import java.util.ArrayList;
import java.util.List;

public class MainApp {
    public static void main(String[] args) {
        Examples examples = new Examples("");
        Network network = new Network(2);
        for (int i = 0; i < 1000; i++) {
            network.adapt(examples.getRandomExample());
        }
        DataForPlot dataForPlot = new DataForPlot();
        List<List<Double>> class1 = new ArrayList<>();
        List<List<Double>> class2 = new ArrayList<>();
        for (int i = 0; i < 100; i++) {
            if (network.work(examples.getSpecificExample(i).getInputs()) > 0.5) {
                class1.add(examples.getSpecificExample(i).getInputs());
            } else {
                class2.add(examples.getSpecificExample(i).getInputs());
            }
        }
        dataForPlot.addPointSet(class1);
        dataForPlot.addPointSet(class2);
        Plot plot = new Plot("oko", dataForPlot);
        plot.pack();
        plot.setVisible(true);
    }
}
