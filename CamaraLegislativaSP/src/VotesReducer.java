import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;


public class VotesReducer extends Reducer<Text, Text, Text, Text>
{
	@Override
	public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException
	{
		String total = "1";
		Iterator<Text> it = values.iterator();
		while(it.hasNext())
		{
			total += it.next().toString();
		}
		context.write(key, new Text(total));
	}
}
