
import com.opencsv.CSVWriter;
import sndlib.core.io.*;
import sndlib.core.model.LinkModel;
import sndlib.core.model.Model;
import sndlib.core.network.Link;
import sndlib.core.network.Node;
import sndlib.core.network.Network;
import sndlib.core.network.Demand;
import sndlib.core.network.AdmissiblePath;
import com.opencsv.CSVReader;

import java.util.*;

import sndlib.core.network.Node;
import sndlib.core.network.Link;
import sndlib.core.util.NetworkUtils;
import sndlib.core.solution.Solution;


import java.io.*;



class PolandData {
    public static void main(String[] args) throws IOException, SNDlibParseException {
        Reader networkReader = new FileReader("src\\somestuff\\germany50.txt");

        // get the appropriate parser, e.g. for the native format
        SNDlibParser parser = SNDlibIOFactory.newParser(SNDlibIOFormat.NATIVE);

        Network network = null;
        network = parser.parseNetwork(networkReader);
        Collection<Demand> demandList = network.demands(); //collectionOfDemands
        List<AdmissiblePath> pathes = new ArrayList<>();
        pathes =allpathes(demandList);
        System.out.println(pathes.size());

        writeDataLineByLine("C:/Users/User/Desktop/output2.csv",pathes);


    }



    public static List<AdmissiblePath> allpathes (Collection<Demand> demands){
        Iterator<Demand> iteratorDemand = demands.iterator();
        List<AdmissiblePath> pathes = new ArrayList<>();


        Collection<AdmissiblePath> pathIndemand;
        while(iteratorDemand.hasNext()){
            pathIndemand =  iteratorDemand.next().admissiblePaths();
            pathes.addAll(pathIndemand);
        }
    return pathes;
        }

    public static void writeDataLineByLine(String filePath,List<AdmissiblePath>allPathes)
    {

        File file = new File(filePath);
        try {
            // create FileWriter object with file as parameter
            FileWriter outputfile = new FileWriter(file);

            // create CSVWriter object filewriter object as parameter
            CSVWriter writer = new CSVWriter(outputfile);

            // adding header to csv
            String[] header = { "Id","Km", "Hopes" };
            writer.writeNext(header);


            for (int l = 0; l < allPathes.size(); l++)

            {
                List<Link> links = new ArrayList<>();
                links=allPathes.get(l).links();


                double summDist = 0;
                for (int i = 0; i < links.size(); i++) {
                    double distance = NetworkUtils.calculateDistanceInKms(links.get(i).getFirstNode(), links.get(i).getSecondNode());
                    summDist =summDist+distance;
                }
                String pathId =allPathes.get(l).getId();
                String km =  Double.toString(summDist);
                String hope = Integer.toString(links.size());

                String[] data = { pathId, km, hope };
                writer.writeNext(data);

            }

            writer.close();
        }
        catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
    }

