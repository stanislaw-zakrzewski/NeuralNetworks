import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.util.ArrayList;
import java.util.List;
import java.util.Vector;

public class DataForPlot {
    private List<List<Vector<Double>>> lines;
    private List<List<Vector<Double>>> points;

    public DataForPlot() {
        lines = new ArrayList<>();
        points = new ArrayList<>();
    }

    public void addLine(List<Vector<Double>> line) {
        lines.add(line);
    }

    public void addPointSet(List<Vector<Double>> point) {
        points.add(point);
    }

    public XYDataset getDatasetFromData() {
        XYSeriesCollection dataset = new XYSeriesCollection();
        for(int i = 0; i < lines.size(); i++) {
            XYSeries pom = new XYSeries("line_" + i);
            lines.get(i).forEach(v -> pom.add(v.get(0), v.get(1)));
            dataset.addSeries(pom);
        }
        for(int i = 0; i < points.size(); i++) {
            XYSeries pom = new XYSeries("point_" + i);
            points.get(i).forEach(v -> pom.add(v.get(0), v.get(1)));
            dataset.addSeries(pom);
        }
        return dataset;
    }

    public List<List<Vector<Double>>> getLines() {
        return lines;
    }

    public List<List<Vector<Double>>> getPoints() {
        return points;
    }
}
