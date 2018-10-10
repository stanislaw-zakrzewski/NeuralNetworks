import java.util.List;
import java.util.Random;

public class Examples {
    private List<Example> examples;
    private Random random = new Random();
    public Examples(String path) {
        FileReader fileReader = new FileReader();
        examples = fileReader.readFile(path);
    }

    public Example getRandomExample() {
        return examples.get(random.nextInt(examples.size()));
    }

    public Example getSpecificExample(int index) {
        return examples.get(index);
    }
}
