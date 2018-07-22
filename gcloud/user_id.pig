A = LOAD 'hdfs://hadoop-m/user/kolisachint/resources/passwd' using PigStorage(':');
B = FOREACH A GENERATE $0 as username;
STORE B INTO 'gs://kolisachint/pig_output/user_id_out';
