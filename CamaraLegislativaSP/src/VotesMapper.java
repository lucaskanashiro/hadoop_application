import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;


public class VotesMapper extends Mapper<Text, Text, Text, Text>
{
	@Override
	public void map(Text key, Text value, Context context) throws IOException, InterruptedException
	{
		String line = value.toString(), party;
		Pattern pattern = Pattern.compile("Partido=\"([A-Za-z]{2,})\"");
		Matcher matcher = pattern.matcher(line);
		if(matcher.find())
		{
			party = matcher.group(1);
			context.write(new Text(party), new Text("1"));
		}
	}
}
