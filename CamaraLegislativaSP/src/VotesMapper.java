import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;


public class VotesMapper extends Mapper<LongWritable, Text, Text, Text>
{
	@Override
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException
	{
		String line = value.toString(), party = "", vote = "";
		Pattern patternVote = Pattern.compile("Partido=\"([A-Za-z]{2,})\"[^>]+Voto=\"(Sim|Não|Não votou)\"");
		Matcher matcherVote = patternVote.matcher(line);
		
		if(matcherVote.find())
		{
			party = matcherVote.group(1);
			vote  = matcherVote.group(2);
			context.write(new Text(party), new Text(vote));
		}
	}
}
