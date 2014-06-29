<?php
	error_reporting(E_ALL);
	ini_set("display_errors", 1);
	putenv("JAVA_HOME=/opt/java/jdk1.7.0_60");
	apc_clear_cache();
	if(isset($_GET['year']))
	{
		$year = $_GET['year'];
		if(in_array($year, array(2010, 2011, 2012, 2013, 2014)))
		{
			$cmd = "python main.py $year";
		} 
	}
	else
	{
		$cmd = 'python main.py';
	}
	chdir('/opt/hadoop/hadoop-2.4.0/hadoop_application');
	shell_exec($cmd);
	echo file_get_contents('/opt/hadoop/hadoop-2.4.0/hadoop_application/graphic_data.html');
?>
