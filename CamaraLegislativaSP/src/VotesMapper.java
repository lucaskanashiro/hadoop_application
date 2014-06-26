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
		String line = value.toString(), party = "", vote = "";
		
		Pattern patternParty = Pattern.compile("Partido=\"([A-Za-z]{2,})\"");
		Pattern patternVote = Pattern.compile("Voto=\"(Sim|Não|Não votou)\"");
		
		Matcher matcherParty = patternParty.matcher(line);
		
		if(matcherParty.find())
			party = matcherParty.group(1);
			
		Matcher matcherVote = patternVote.matcher(line);
		
		if(matcherVote.find())
			vote = matcherVote.group(1);
		
		context.write(new Text(party), new Text(vote));
	}
}
