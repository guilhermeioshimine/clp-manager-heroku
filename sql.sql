CREATE TABLE `report` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `recipe_cod` varchar(20) NOT NULL,
  `recipe_name` varchar(20) NOT NULL,
  `solid` float NOT NULL,
  `liquid1` float NOT NULL,
  `liquid2` float NOT NULL,
  `powder` float NOT NULL,
  `blend_time` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=199 DEFAULT CHARSET=latin1;

CREATE TABLE `recipe` (
  `id` int NOT NULL AUTO_INCREMENT,
  `recipe_cod` varchar(20) COLLATE utf8_bin NOT NULL,
  `recipe_name` varchar(20) COLLATE utf8_bin NOT NULL,
  `solid` float NOT NULL,
  `liquid1` float NOT NULL,
  `liquid2` float NOT NULL,
  `powder` float NOT NULL,
  `blend_time` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
