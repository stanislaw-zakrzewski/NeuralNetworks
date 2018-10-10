import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class DatasetGenerator {
    private static final double a = 1;
    private static final double b = 0;
    private static final int datasetCount = 100;

    private static List<List<Double>> dataset;
    private static Random random;

    private static double linearFunction(double x) {
        return a * x + b;
    }

    public static void main(String[] args) {
        dataset = new ArrayList<>();
        random = new Random();

        for (int i = 0; i < datasetCount; i++) {
            dataset.add(new ArrayList<>());
            dataset.get(i).add(random.nextDouble() * 10);
            dataset.get(i).add(random.nextDouble() * 10);
            dataset.get(i).add((linearFunction(dataset.get(i).get(0)) < dataset.get(i).get(1)) ? 1.0 : 0.0);
        }

        writeToFile();
    }

    private static void writeToFile() {
        try {
            final PrintWriter writer = new PrintWriter("src/main/resources/dataset.txt", StandardCharsets.UTF_8);
            dataset.forEach(d -> writer.println(d.get(0) + " " + d.get(1) + " " + d.get(2)));
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
