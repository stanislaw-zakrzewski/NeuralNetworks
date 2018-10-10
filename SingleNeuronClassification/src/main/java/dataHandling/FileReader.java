package dataHandling;

import examples.Example;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class FileReader {
    public List<Example> readFile(String path) {
        List<Example> temp = new ArrayList<>();
        File file = new File("src/main/resources/dataset.txt");
        Scanner scanner;
        try {
            scanner = new Scanner(file);

            while (scanner.hasNextDouble()) {
                temp.add(new Example(scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble()));
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return temp;
    }
}
