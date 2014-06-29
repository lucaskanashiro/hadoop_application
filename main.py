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
	html_content = ""
	for party in data:
		data_votes = party.split(" ")
		yes_votes = float(data_votes[1])
		no_votes = float(data_votes[2])
		without_votes = float(data_votes[3])

		total_votes = yes_votes + no_votes + without_votes

		percent_yes = "%.2f" % (yes_votes*100 / total_votes)
		percent_no = "%.2f" % (no_votes*100 / total_votes)
		percent_without = "%.2f" % (without_votes*100 / total_votes)

		html_content = html_content + data_votes[0] + ': [' + percent_yes + ', ' + percent_no + ', ' + percent_without + "],\n" 

	template = ''
	with open('html/graphic_template.html', 'r') as content_file:
		template = content_file.read()

	template = template.replace('%dataParties%', str(html_content).replace("'", ''))

	html_file = open("/var/www/graphic_data.html", 'w')
	html_file.write(template)
	html_file.close()

def run():
	compile()
	hadoop_application()
	analyze()

run()

