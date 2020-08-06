-- ii. Написать скрипт, возвращающий список имен (только firstname) 
-- пользователей без повторений в алфавитном порядке

USE vk;

SELECT DISTINCT firstname
FROM users
ORDER BY firstname;

-- iii. Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false).
-- Предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)
ALTER TABLE profiles ADD is_active BIT DEFAULT 1;

UPDATE profiles 
SET is_active = 0
WHERE (CURDATE() - birthday < 78840);


-- iv. Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней)

DELETE FROM messages
WHERE (NOW() - created_at < 0);


