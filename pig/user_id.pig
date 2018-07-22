A = LOAD '/user/kolisachint/resources/passwd' using PigStorage(':');
B = FOREACH A GENERATE $0 as username;
STORE B INTO '/user/kolisachint/resources/pig/user_id.out';
