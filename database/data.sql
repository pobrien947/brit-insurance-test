
--
-- Add items
--
INSERT INTO `item` (`id`, `item_name`, `default_price`) VALUES
  (1, "Apples", 5),
  (2, "Book", 100),
  (3, "Car", 20000);

--
-- Add a demo test user
--
INSERT INTO `user` (`id`, `username`, `password`, `auth_token`) VALUES (1, "demouser", "demopassword", "");
