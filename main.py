import subprocess
import os
import re

def compile():
	subprocess.call("git pull", shell=True)
	os.chdir("CamaraLegislativaSP/src")
	subprocess.call("pwd", shell=True)
	subprocess.call("javac -cp ../../../share/hadoop/mapreduce/hadoop-mapreduce-client-core-2.4.0.jar:../../../share/hadoop/common/hadoop-common-2.4.0.jar *.java", shell=True)
	subprocess.call("jar cf camara.jar *.class", shell=True)
	subprocess.call("mv camara.jar ../../../camara.jar", shell=True)
	os.chdir("../../")

def hadoop_application():
	os.chdir("../")
	subprocess.call("rm -rf output", shell=True)
	subprocess.call("bin/hadoop jar camara.jar VotesSummarizer input output", shell=True)
	os.chdir("hadoop_application")

def analyze():
	data = ""
	with open('../output/part-r-00000', 'r') as content_file:
		data = content_file.read().replace("\t", " ")
	data = data.split("\n")
	data = data[:-1]
	result = {}
	for party in data:
		data_votes = party.split(" ")
		yes_votes = float(data_votes[1])
		no_votes = float(data_votes[2])
		without_votes = float(data_votes[3])

		total_votes = yes_votes + no_votes + without_votes

		percent_yes = "%.2f" % (yes_votes*100 / total_votes)
		percent_no = "%.2f" % (no_votes*100 / total_votes)
		percent_without = "%.2f" % (without_votes*100 / total_votes)

		result[data_votes[0]] = [percent_yes, percent_no, percent_without]

	html_content = ""
	with open('html/graphic_template.html', 'r') as content_file:
		html_content = content_file.read()
	pattern = re.compile(ur'([\w]+): \[(%s%)\]')	
	matches = re.findall(pattern, html_content)
	for grp1, grp2 in matches:
		html_content = html_content.replace(grp1 + ": [" + grp2 + "]", grp1 + ": " + str(result[grp1]).replace("'", ''))

	html_file = open("/var/www/graphic_data.html", 'w')
	html_file.write(html_content)
	html_file.close()


def run():
	compile()
	hadoop_application()
	analyze()

run()

