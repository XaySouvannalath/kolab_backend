# How to run the project:
uvicorn main:app --reload




# Create user for databas

CREATE USER 'kolab'@'0.0.0.0' IDENTIFIED BY 'Qazplm#123Qazplm';
CREATE USER 'kolab'@'0.0.0.0' IDENTIFIED WITH mysql_native_password BY 'Qazplm#123Qazplm';

ALTER USER 'kolab'@'0.0.0.0' IDENTIFIED WITH mysql_native_password BY 'Qazplm#123Qazplm';

GRANT PRIVILEGE ON database.table TO 'kolab'@'0.0.0.0';

GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'kolab'@'0.0.0.0' WITH GRANT OPTION;


GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'kolab'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

SHOW GRANTS FOR 'kolab'@'0.0.0.0';

DROP USER 'username'@'localhost';

mysql -u sammy -p

ref: https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql


# allow mysql user to remote from any ip
 GRANT ALL PRIVILEGES ON *.* TO 'kolab'@'%' IDENTIFIED BY 'Qazplm#123Qazplm' WITH GRANT OPTION;
 FLUSH PRIVILEGES;


 ALTER USER 'kolab'@'%' IDENTIFIED BY 'Qazplm_123Qazplm';



view-source:https://www.facebook.com/MrBeast6000


task:

get follower log by: influencer_id, from_date to_date