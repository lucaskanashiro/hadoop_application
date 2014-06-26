import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;


public class VotesReducer extends Reducer<Text, Text, Text, Text>
{
	@Override
	public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException
	{
		int votosSim, votosNao, naoVotou;
		votosSim = votosNao = naoVotou = 0;
		Iterator<Text> it = values.iterator();
		String temp;
		while(it.hasNext())
		{
			temp = it.next().toString();
			if(temp.equals("Sim"))
				votosSim++;
			else if(temp.equals("Não"))
				votosNao++;
			else
				naoVotou++;
		}
		context.write(key, new Text("S" + votosSim + "N" + votosNao + "NV" + naoVotou));
	}
}
