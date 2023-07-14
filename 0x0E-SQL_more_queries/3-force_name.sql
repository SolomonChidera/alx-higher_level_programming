-- a script that creates the table force_name on your MySQL server.
--	force_name description:
--		id INT
--		name VARCHAR(256) can’t be null
-- if the table force_name already exists, your script should not fail
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
	);
