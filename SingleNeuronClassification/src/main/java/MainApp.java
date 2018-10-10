import java.util.ArrayList;
import java.util.Vector;

public class MainApp {
    public static void main(String[] args) {
        DataForPlot dataForPlot = new DataForPlot();
        ArrayList<Vector<Double>> line = new ArrayList<>();
        line.add(new Vector<>());
        line.add(new Vector<>());
        line.get(0).add(1.0);
        line.get(0).add(1.0);
        line.get(1).add(3.0);
        line.get(1).add(3.0);
        dataForPlot.addPointSet(line);
        Plot plot = new Plot("oko", dataForPlot);
        plot.pack();
        plot.setVisible(true);
    }
}
