DROP DATABASE brit_insurance;
CREATE DATABASE brit_insurance;
USE brit_insurance;

--
-- Table structure for table `user`
--
CREATE TABLE IF NOT EXISTS `user` (
  `id`         BIGINT(20)   UNSIGNED NOT NULL AUTO_INCREMENT,
  `username`   VARCHAR(100)  DEFAULT NULL,
  `password`   VARCHAR(50)   DEFAULT 0,
  `auth_token` VARCHAR(255)  DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=INNODB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

--
-- Table structure for table `item`
--
CREATE TABLE IF NOT EXISTS `item` (
  `id`            BIGINT(20)    UNSIGNED NOT NULL AUTO_INCREMENT,
  `item_name`     VARCHAR(255)  DEFAULT NULL,
  `default_price` BIGINT(20)    UNSIGNED NOT NULL   DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=INNODB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

--
-- Table structure for table `basket`
--
CREATE TABLE IF NOT EXISTS `basket` (
  `id`         BIGINT(20)   UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id`    BIGINT(20)   UNSIGNED NOT NULL,
  `item_name`  VARCHAR(255)  DEFAULT NULL,
  `price`      BIGINT(20)   DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=INNODB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;
