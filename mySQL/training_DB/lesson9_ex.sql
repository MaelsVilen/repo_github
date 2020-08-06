-- Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, 
-- catalogs и products в таблицу logs помещается время и дата создания записи, название таблицы, 
-- идентификатор первичного ключа и содержимое поля name. 
USE shop;
DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
	created_at DATETIME NOT NULL,
	table_name VARCHAR(255) NOT NULL,
	str_id BIGINT NOT NULL,
	name_value VARCHAR(255) NOT NULL
) ENGINE = ARCHIVE;

DROP TRIGGER IF EXISTS logging_users;
delimiter //
CREATE TRIGGER logging_users AFTER INSERT ON users
FOR EACH ROW
BEGIN
	INSERT INTO logs (created_at, table_name, str_id, name_value)
	VALUES (NOW(), 'users', NEW.id, NEW.name);
END //

DROP TRIGGER IF EXISTS logging_catalogs //
CREATE TRIGGER logging_catalogs AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN
	INSERT INTO logs (created_at, table_name, str_id, name_value)
	VALUES (NOW(), 'catalogs', NEW.id, NEW.name);
END //

DROP TRIGGER IF EXISTS logging_products //
CREATE TRIGGER logging_products AFTER INSERT ON products
FOR EACH ROW
BEGIN
	INSERT INTO logs (created_at, table_name, str_id, name_value)
	VALUES (NOW(), 'products', NEW.id, NEW.name);
END //
delimiter ;

SELECT * FROM users;
SELECT * FROM logs;

INSERT INTO users (name, birthday_at)
VALUES ('John Wick', '1962-09-02');

SELECT * FROM users;
SELECT * FROM logs;

-- insert into catalogs
SELECT * FROM catalogs;
SELECT * FROM logs;

INSERT INTO catalogs (name)
VALUES ('ACME'),
		('Umbrella'),
		('Shinra electric');

SELECT * FROM catalogs;
SELECT * FROM logs;



-- (по желанию) Создайте SQL-запрос, который помещает в таблицу users миллион записей. 

DROP TABLE IF EXISTS dummy_users; 
CREATE TABLE dummy_users_ (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	birthday_at DATE,
	`created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
 	`updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


DROP PROCEDURE IF EXISTS datafill_users ;
delimiter //
CREATE PROCEDURE datafill_users ()
BEGIN
	DECLARE i INT DEFAULT 1;
	WHILE i < 1000000 DO
		INSERT INTO dummy_users(name, birthday_at) VALUES (CONCAT('user_', i), NOW());
		SET i = i + 1;
	END WHILE;
END //
delimiter ;

SELECT * FROM dummy_users;
CALL datafill_users();
SELECT * FROM dummy_users LIMIT 5;
