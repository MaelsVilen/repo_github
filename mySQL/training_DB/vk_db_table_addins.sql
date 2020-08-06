USE vk;

DROP TABLE IF EXISTS user_video;
CREATE TABLE user_video(
	id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
	filename VARCHAR(255) DEFAULT NULL,
    user_id BIGINT UNSIGNED DEFAULT NULL,
	confirmed_at DATETIME ON UPDATE NOW(),
	
    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS videos;
CREATE TABLE videos (
	id SERIAL,
	video_id BIGINT unsigned NOT NULL,
	media_id BIGINT unsigned NOT NULL,

	FOREIGN KEY (video_id) REFERENCES user_video(id),
    FOREIGN KEY (media_id) REFERENCES media(id)
);

DROP TABLE IF EXISTS premium_account;
CREATE TABLE premium_account (
	user_id BIGINT UNSIGNED DEFAULT NULL,
	`status` ENUM ('basic', 'premium'),
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	expires_at DATETIME,
	
	FOREIGN KEY (user_id) REFERENCES users(id)
);