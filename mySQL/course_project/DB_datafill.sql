USE microfabrication;

INSERT INTO shifts_schedule (operator_id, operator_firstname, operator_lastname, working_day, status)
  VALUES (102, 'Vladislav', 'Donthurtme', '2020-01-17', '1st shift'),
  (103, 'Charlie', 'Brown', '2020-01-17', '1st shift'),
  (104, 'Betty', 'Boop', '2020-01-17', '2nd shift'),
  (105, 'John', 'Bravo', '2020-01-17', 'vacation'),
  (106, 'Olive', 'Oyl', '2020-01-17', '1st shift'),
  (102, 'Vladislav', 'Donthurtme', '2020-01-18', '1st shift'),
  (103, 'Charlie', 'Brown', '2020-01-18', '2nd shift'),
  (104, 'Betty', 'Boop', '2020-01-18', '1st shift'),
  (105, 'John', 'Bravo', '2020-01-18', 'vacation'),
  (106, 'Olive', 'Oyl', '2020-01-18', '1st shift');

INSERT INTO runlog(
  foup_id, slot, operation, module, process_time, operator_id)
  VALUES ('AL21', 1, 'deposition', 'monitor', '2020-01-17 11:05:00', 102),
  ('AF35', 5, 'etch', 'monitor', '2020-01-17 11:30:00', 106),
  ('LM11', 7,  'polishing', 'monitor', '2020-01-17 11:45:00', 103),
  ('AL21', 1, 'anneal', 'monitor', '2020-01-17 12:01:00', 102),
  ('ABC20120', 1, 'deposition', 'M1', '2020-01-17 13:15:00', 102),
  ('ABC20120', 2, 'deposition', 'M1', '2020-01-17 13:22:00', 102),
  ('ABC20120', 3, 'deposition', 'M1', '2020-01-17 13:29:00', 102),
  ('DEF20110', 4, 'etch', 'M2', '2020-01-17 13:29:00', 106),
  ('ABC20120', 4, 'deposition', 'M1', '2020-01-17 13:36:00', 102),
  ('DEF20110', 5, 'etch', 'M2', '2020-01-17 13:38:00', 106),
  ('ABC20120', 5, 'deposition', 'M1', '2020-01-17 13:43:00', 102),
  ('ABC20120', 1, 'anneal', 'M1', '2020-01-17 14:10:00', 103),
  ('ABC20120', 2, 'anneal', 'M1', '2020-01-17 14:10:00', 103),
  ('ABC20120', 3, 'anneal', 'M1', '2020-01-17 14:10:00', 103),
  ('ABC20120', 1, 'polishing', 'M1', '2020-01-17 14:17:00', 103),
  ('ABC20120', 2, 'polishing', 'M1', '2020-01-17 14:24:00', 103);

INSERT INTO material_type (film_material, multiplier)
  VALUES ('metal', 33.57),
  ('oxide', 1.0),
  ('nitride', 24.21);

INSERT INTO measurement_site (measurement_map, site, coordinate_x, coordinate_y)
  VALUES ('polar', 1, 0, 0),
  ('polar', 2, -20.5, 20.5),
  ('polar', 3, -51.5, 22.3),
  ('polar', 4, 58, 0.03),
  ('polar', 5, 41.1, 41.1),
  ('cross', 1, 7.25, 0),
  ('cross', 2, 3.62, 0),
  ('cross', 3, 0, 0),
  ('cross', 4, -3.62, 0),
  ('cross', 5, -7.25, 0),
  ('cross', 6, -10.88, 0);

INSERT INTO metrology_pre (foup_id, slot, site, measurement_map, raw_value, film_material, processed_value, module, operation, process_time)
  VALUES ('AL21', 1, 1, 'polar', 2.58, 'metal', 86.61, 'monitor', 'deposition', '2020-01-17 11:00:00'),
  ('AL21', 1, 2, 'polar', 2.56, 'metal', 85.94, 'monitor', 'deposition', '2020-01-17 11:00:00'),
  ('AL21', 1, 3, 'polar', 2.57, 'metal', 86.27, 'monitor', 'deposition', '2020-01-17 11:00:00'),
  ('AL21', 1, 4, 'polar', 2.63, 'metal', 88.29, 'monitor', 'deposition', '2020-01-17 11:00:00'),
  ('AL21', 1, 5, 'polar', 2.41, 'metal', 80.9, 'monitor', 'deposition', '2020-01-17 11:00:00'),
  ('AL21', 1, 1, 'cross', 2.55, 'metal', 85.6, 'monitor', 'deposition', '2020-01-17 11:02:00'),
  ('AL21', 1, 2, 'cross', 2.52, 'metal', 84.6, 'monitor', 'deposition', '2020-01-17 11:02:00'),
  ('AL21', 1, 3, 'cross', 2.55, 'metal', 85.6, 'monitor', 'deposition', '2020-01-17 11:02:00'),
  ('AL21', 1, 4, 'cross', 2.58, 'metal', 86.61, 'monitor', 'deposition', '2020-01-17 11:02:00'),
  ('AL21', 1, 5, 'cross', 2.61, 'metal', 87.61, 'monitor', 'deposition', '2020-01-17 11:02:00'),
  ('AL21', 1, 6, 'cross', 2.53, 'metal', 84.9, 'monitor', 'deposition', '2020-01-17 11:02:00');

INSERT INTO metrology_post (foup_id, slot, site, measurement_map, raw_value, film_material, processed_value, module, operation, process_time)
  VALUES ('AL21', 1, 1, 'polar', 6.43, 'metal', 215.86, 'monitor', 'deposition', '2020-01-17 11:15:00'),
  ('AL21', 1, 2, 'polar', 6.52, 'metal', 218.88, 'monitor', 'deposition', '2020-01-17 11:15:00'),
  ('AL21', 1, 3, 'polar', 6.29, 'metal', 211.15, 'monitor', 'deposition', '2020-01-17 11:15:00'),
  ('AL21', 1, 4, 'polar', 6.34, 'metal', 212.83, 'monitor', 'deposition', '2020-01-17 11:15:00'),
  ('AL21', 1, 5, 'polar', 6.3, 'metal', 211.49, 'monitor', 'deposition', '2020-01-17 11:15:00'),
  ('AL21', 1, 1, 'cross', 6.42, 'metal', 215.52, 'monitor', 'deposition', '2020-01-17 11:17:00'),
  ('AL21', 1, 2, 'cross', 6.39, 'metal', 214.51, 'monitor', 'deposition', '2020-01-17 11:17:00'),
  ('AL21', 1, 3, 'cross', 6.5, 'metal', 218.2, 'monitor', 'deposition', '2020-01-17 11:17:00'),
  ('AL21', 1, 4, 'cross', 6.44, 'metal', 216.19, 'monitor', 'deposition', '2020-01-17 11:17:00'),
  ('AL21', 1, 5, 'cross', 6.38, 'metal', 214.18, 'monitor', 'deposition', '2020-01-17 11:17:00'),
  ('AL21', 1, 6, 'cross', 6.5, 'metal', 218.2, 'monitor', 'deposition', '2020-01-17 11:17:00');

INSERT INTO deposition_metrics (foup_id, slot, module, measurement_map, mean_deposition_rate)
  VALUES ('AL21', 1, 'monitor', 'polar', 128.44),
  ('AL21', 1, 'monitor', 'cross', 130.31),
  ('ABC20120', 1, 'M1', 'polar', 120.11),
  ('ABC20120', 1, 'M1', 'cross', 124.15),
  ('ABC20120', 2, 'M1', 'polar', 122.32),
  ('ABC20120', 2, 'M1', 'cross', 123.4),
  ('ABC20120', 3, 'M1', 'polar', 122.56),
  ('ABC20120', 3, 'M1', 'cross', 118.5),
  ('ABC20120', 4, 'M1', 'polar', 120.33),
  ('ABC20120', 4, 'M1', 'cross', 121.89);

INSERT INTO polishing_metrics (foup_id, slot, module, measurement_map, mean_removal_rate)
  VALUES ('LM11', 7,  'monitor', 'polar', 51.4),
  ('LM11', 7,  'monitor', 'cross', 58.6),
  ('ABC20120', 1, 'M1', 'polar', 56.91),
  ('ABC20120', 1, 'M1', 'cross', 54.23),
  ('ABC20120', 2, 'M1', 'polar', 55.5),
  ('ABC20120', 2, 'M1', 'cross', 55.64);

INSERT INTO etch_metrics (foup_id, slot, module, measurement_map, mean_etch_rate)
  VALUES ('AF35', 5, 'monitor', 'polar', 22.1),
  ('AF35', 5, 'monitor', 'cross', 15.72),
  ('DEF20110', 4, 'M2', 'polar', 17.92),
  ('DEF20110', 4, 'M2', 'cross', 19.34),
  ('DEF20110', 5, 'M2', 'polar', 14.81),
  ('DEF20110', 5, 'M2', 'cross', 16.48);

INSERT INTO anneal_metrics (foup_id, slot, module, measurement_map, mean_Rs)
  VALUES ('AL21', 1, 'monitor', 'polar', 2.35),
  ('AL21', 1, 'monitor', 'cross', 2.22),
  ('ABC20120', 1, 'M1', 'polar', 2.34),
  ('ABC20120', 1, 'M1', 'cross', 2.42),
  ('ABC20120', 2, 'M1', 'polar', 2.14),
  ('ABC20120', 2, 'M1', 'cross', 2.36),
  ('ABC20120', 3, 'M1', 'polar', 2.16),
  ('ABC20120', 3, 'M1', 'cross', 2.08);
  