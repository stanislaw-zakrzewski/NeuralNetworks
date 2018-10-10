package plotting;

import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.util.ArrayList;
import java.util.List;

public class DataForPlot {
    private List<List<List<Double>>> lines;
    private List<List<List<Double>>> points;

    public DataForPlot() {
        lines = new ArrayList<>();
        points = new ArrayList<>();
    }

    public void addLine(List<List<Double>> line) {
        lines.add(line);
    }

    public void addPointSet(List<List<Double>> point) {
        points.add(point);
    }

    public XYDataset getDatasetFromData() {
        XYSeriesCollection dataset = new XYSeriesCollection();
        for (int i = 0; i < lines.size(); i++) {
            XYSeries pom = new XYSeries("line_" + i);
            lines.get(i).forEach(v -> pom.add(v.get(0), v.get(1)));
            dataset.addSeries(pom);
        }
        for (int i = 0; i < points.size(); i++) {
            XYSeries pom = new XYSeries("point_" + i);
            points.get(i).forEach(v -> pom.add(v.get(0), v.get(1)));
            dataset.addSeries(pom);
        }
        return dataset;
    }

    public List<List<List<Double>>> getLines() {
        return lines;
    }

    public List<List<List<Double>>> getPoints() {
        return points;
    }
}
