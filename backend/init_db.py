import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'Sharpeyecoder373!',
  'host': '127.0.0.1',
}

DB_NAME = 'csa_db'

TABLES = {}
TABLES['customers'] = (
    "CREATE TABLE `customers` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(255) NOT NULL,"
    "  `email` varchar(255) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['orders'] = (
    "CREATE TABLE `orders` ("
    "  `order_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `customer_id` int(11) NOT NULL,"
    "  `status` varchar(50) NOT NULL,"
    "  `current_location` varchar(255),"
    "  `last_updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`order_id`),"
    "  FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)"
    ") ENGINE=InnoDB")

TABLES['products'] = (
    "CREATE TABLE `products` ("
    "  `product_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(255) NOT NULL,"
    "  `category` varchar(100),"
    "  `price` decimal(10, 2) NOT NULL,"
    "  PRIMARY KEY (`product_id`)"
    ") ENGINE=InnoDB")

TABLES['sales'] = (
    "CREATE TABLE `sales` ("
    "  `sale_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `product_id` int(11) NOT NULL,"
    "  `quantity` int(11) NOT NULL,"
    "  `sale_date` datetime DEFAULT CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`sale_id`),"
    "  FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)"
    ") ENGINE=InnoDB")

TABLES['customer_feedback'] = (
    "CREATE TABLE `customer_feedback` ("
    "  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `customer_id` int(11) NOT NULL,"
    "  `text` text NOT NULL,"
    "  `sentiment` varchar(50),"
    "  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`feedback_id`),"
    "  FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)"
    ") ENGINE=InnoDB")

TABLES['agent_logs'] = (
    "CREATE TABLE `agent_logs` ("
    "  `log_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `agent_name` varchar(100) NOT NULL,"
    "  `action_taken` text NOT NULL,"
    "  `result` text,"
    "  `timestamp` datetime DEFAULT CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`log_id`)"
    ") ENGINE=InnoDB")

TABLES['agent_memory'] = (
    "CREATE TABLE `agent_memory` ("
    "  `memory_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `issue_type` varchar(100) NOT NULL,"
    "  `frequency` int(11) DEFAULT 1,"
    "  `trend` varchar(100),"
    "  `last_updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`memory_id`)"
    ") ENGINE=InnoDB")

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exist.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
