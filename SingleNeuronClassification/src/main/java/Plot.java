import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.ui.ApplicationFrame;

public class Plot extends ApplicationFrame {

    public Plot(String plotTitle, DataForPlot dataForPlot) {
        super(plotTitle);
        JFreeChart chart = ChartFactory.createXYLineChart(
                plotTitle,
                "X",
                "Y",
                dataForPlot.getDatasetFromData(),
                PlotOrientation.VERTICAL,
                true, true, false);

        ChartPanel chartPanel = new ChartPanel(chart);
        final XYPlot plot = chart.getXYPlot();

        XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer();
        plot.setRenderer(renderer);
        for(int i = 0; i < dataForPlot.getPoints().size(); i ++) {
            renderer.setSeriesLinesVisible(i + dataForPlot.getLines().size(), false);
        }
        setContentPane(chartPanel);
    }
}
