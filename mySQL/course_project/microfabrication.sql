DROP DATABASE IF EXISTS microfabrication;
CREATE DATABASE microfabrication;
USE microfabrication;

DROP TABLE IF EXISTS shifts_schedule;
CREATE TABLE shifts_schedule (
  operator_id int UNSIGNED NOT NULL,
  operator_firstname varchar(20),
  operator_lastname varchar(20),
  working_day date,
  status enum ('1st shift', '2nd shift', 'sick', 'vacation'),

  PRIMARY KEY (operator_id, working_day)
  );

DROP TABLE IF EXISTS runlog;
CREATE TABLE runlog (
   foup_id varchar(10) NOT NULL,
   slot tinyint UNSIGNED NOT NULL,
   operation enum ('deposition', 'etch', 'anneal', 'polishing'),
   module enum ('M1', 'V1', 'M2', 'monitor'),
   process_time datetime DEFAULT NOW(),
   operator_id int UNSIGNED NOT NULL,

  PRIMARY KEY (foup_id, slot, operation, module),
  FOREIGN KEY (operator_id) REFERENCES shifts_schedule(operator_id)
  );

DROP TABLE IF EXISTS material_type;
CREATE TABLE material_type (
  film_material enum ('metal', 'oxide', 'nitride'),
  multiplier float UNSIGNED
  );

DROP TABLE IF EXISTS measurement_site;
CREATE TABLE measurement_site (
  measurement_map enum ('polar', 'cross', 'diagonal', 'sqare'),
  site tinyint UNSIGNED NOT NULL,
  coordinate_x float NOT NULL,
  coordinate_y float NOT NULL,

  PRIMARY KEY (measurement_map, site)
  );

DROP TABLE IF EXISTS metrology_pre;
CREATE TABLE metrology_pre (
  foup_id varchar(10) NOT NULL,
  slot tinyint UNSIGNED NOT NULL,
  site tinyint UNSIGNED NOT NULL,
  measurement_map enum ('polar', 'cross', 'diagonal', 'sqare'),
  raw_value float UNSIGNED,
  film_material enum ('metal', 'oxide', 'nitride'), 
  processed_value float UNSIGNED,
  module enum ('M1', 'V1', 'M2', 'monitor'),
  operation enum ('deposition', 'etch', 'anneal', 'polishing'),
  process_time datetime DEFAULT NOW(),
  
  PRIMARY KEY (foup_id, slot, operation, module, measurement_map, site),
  FOREIGN KEY (foup_id, slot, operation, module) REFERENCES runlog(foup_id, slot, operation, module)
);

DROP TABLE IF EXISTS metrology_post;
CREATE TABLE metrology_post (
  foup_id varchar(10) NOT NULL,
  slot tinyint UNSIGNED NOT NULL,
  site tinyint UNSIGNED NOT NULL,
  measurement_map enum ('polar', 'cross', 'diagonal', 'sqare'),
  raw_value float UNSIGNED,
  film_material enum ('metal', 'oxide', 'nitride'), 
  processed_value float UNSIGNED,
  module enum ('M1', 'V1', 'M2', 'monitor'),
  operation enum ('deposition', 'etch', 'anneal', 'polishing'),
  process_time datetime DEFAULT NOW(),

  PRIMARY KEY (foup_id, slot, operation, module, measurement_map, site),
  FOREIGN KEY (foup_id, slot, operation, module) REFERENCES runlog(foup_id, slot, operation, module)
);

DROP TABLE IF EXISTS deposition_metrics;
CREATE TABLE deposition_metrics (
  foup_id varchar(10) NOT NULL,
  slot tinyint UNSIGNED NOT NULL,
  module enum ('M1', 'V1', 'M2', 'monitor'),
  measurement_map enum ('polar', 'cross', 'diagonal', 'sqare'),
  mean_deposition_rate float UNSIGNED, 
 
  PRIMARY KEY (foup_id, slot, module, measurement_map), 
  FOREIGN KEY (foup_id, slot) REFERENCES runlog(foup_id, slot),
  FOREIGN KEY (measurement_map) REFERENCES measurement_site(measurement_map)
  );

DROP TABLE IF EXISTS polishing_metrics;
CREATE TABLE polishing_metrics (
  foup_id varchar(10) NOT NULL,
  slot tinyint UNSIGNED NOT NULL,
  module enum ('M1', 'V1', 'M2', 'monitor'),
  measurement_map enum ('polar', 'cross', 'diagonal', 'sqare'),
  mean_removal_rate float UNSIGNED, 

  PRIMARY KEY (foup_id, slot, module, measurement_map),
  FOREIGN KEY (foup_id, slot) REFERENCES runlog(foup_id, slot),
  FOREIGN KEY (measurement_map) REFERENCES measurement_site(measurement_map)
 );

DROP TABLE IF EXISTS etch_metrics;
CREATE TABLE etch_metrics (
  foup_id varchar(10) NOT NULL,
  slot tinyint UNSIGNED NOT NULL,
  module enum ('M1', 'V1', 'M2', 'monitor'),
  measurement_map enum ('polar', 'cross', 'diagonal', 'sqare'),
  mean_etch_rate float UNSIGNED, 

  PRIMARY KEY (foup_id, slot, module, measurement_map),
  FOREIGN KEY (foup_id, slot) REFERENCES runlog(foup_id, slot),
  FOREIGN KEY (measurement_map) REFERENCES measurement_site(measurement_map)
  );

DROP TABLE IF EXISTS anneal_metrics;
CREATE TABLE anneal_metrics (
  foup_id varchar(10) NOT NULL,
  slot tinyint UNSIGNED NOT NULL,
  module enum ('M1', 'V1', 'M2', 'monitor'),
  measurement_map enum ('polar', 'cross', 'diagonal', 'sqare'),
  mean_Rs float UNSIGNED, 

  PRIMARY KEY (foup_id, slot, module, measurement_map),
  FOREIGN KEY (foup_id, slot) REFERENCES runlog(foup_id, slot),
  FOREIGN KEY (measurement_map) REFERENCES measurement_site(measurement_map)
  );
