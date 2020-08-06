-- Пусть задан некоторый пользователь. Из всех пользователей соц. сети 
-- найдите человека, который больше всех общался с выбранным пользователем.
SELECT 
	COUNT(*),
	to_user_id,
	(SELECT CONCAT(firstname, ' ',  lastname) FROM users WHERE id = messages.from_user_id) AS BFF
FROM 
	messages
WHERE
	to_user_id = 1 -- ищем лучшего друга первого пользователя
GROUP BY
	from_user_id
LIMIT 1
;

-- Подсчитать общее количество лайков, которые получили пользователи младше 10 лет.
SELECT
	COUNT(*) AS 'likes from under 10'		
FROM
	likes
WHERE
	user_id IN 
	(SELECT user_id FROM profiles WHERE TIMESTAMPDIFF(YEAR, birthday, NOW()) <= 10)
;
	
-- Определить кто больше поставил лайков (всего): мужчины или женщины.
SELECT 
	COUNT(*), 
	gender 
FROM 
	profiles 
WHERE 
	user_id IN (SELECT user_id FROM likes WHERE user_id IN (SELECT id FROM users))
GROUP BY
	gender
;












