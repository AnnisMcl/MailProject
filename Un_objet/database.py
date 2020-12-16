import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS email_address (
  email_id int(11) PRIMARY KEY,
  address varchar(55) NOT NULL)''')

c.execute('''CREATE TABLE IF NOT EXISTS `server` (
  `server_id` int(11) PRIMARY KEY,
  `name` varchar(55) NOT NULL,
  `smtp` varchar(55) NOT NULL,
  `imap` varchar(55) NOT NULL,
  `port` int(11) DEFAULT NULL
)''')


c.execute('''CREATE TABLE IF NOT EXISTS `server_domain` (
  `domain_id` int(11) PRIMARY KEY,
  `domain` varchar(55) NOT NULL,
  `server_id` int(11) DEFAULT NULL,
  FOREIGN KEY(server_id) REFERENCES server(server_id)
)''')

c.execute('''INSERT INTO server VALUES(1, 'google','smtp.gmail.com',465)''')
