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
	for vote in data:
		print vote
	#print data
def run():
	#compile()
	#hadoop_application()
	analyze()

run()

