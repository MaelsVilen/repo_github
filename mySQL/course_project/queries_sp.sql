-- проверка расписани€ смен на текущий день;
select * from shifts_schedule where working_day=current_date;
-- сверка среднего значени€, полученного расчЄтами из сырых данных, с итоговой таблицей;2
SET @thickness_post := (SELECT avg(processed_value) FROM metrology_post WHERE foup_id = 'AL21' AND operation = 'deposition');
SET @thickness_pre := (SELECT avg(processed_value) FROM metrology_pre WHERE foup_id = 'AL21' AND operation = 'deposition');
SELECT avg(mean_deposition_rate) FROM deposition_metrics WHERE foup_id = 'AL21'
UNION
SELECT @thickness_post - @thickness_pre; -- разница обусловлена приближЄнными расчЄтами дл€ таблицы итоговых значений;
-- выборка значений по координатам;
SELECT 
	mp.foup_id,
	mp.slot,
	mp.module,
	mp.site,
	mp.raw_value,
	mp.measurement_map,
	ms.coordinate_x,
	ms.coordinate_y
FROM
	metrology_pre AS mp
JOIN
	measurement_site AS ms 
ON 
	mp.measurement_map = ms.measurement_map
AND
	mp.site = ms.site;
-- предварительные сырые данные мониторинга нанесени€ металлических слоЄв;
CREATE OR REPLACE VIEW metal_deposition_monitoring_pre AS 
SELECT 
	slot,
	raw_value,
	measurement_map,
	process_time
FROM 
	metrology_pre
WHERE 
	operation='deposition'
AND 
	film_material='metal'
AND 
	module='monitor'
ORDER BY 
	process_time;

SELECT * FROM metal_deposition_monitoring_pre;

-- расчЄт стандартного отклонени€ результатов мониторинга;
CREATE OR REPLACE VIEW deposition_std AS 
SELECT 
	slot,
	avg(mean_deposition_rate) AS mean_deposition_rate,
	(SELECT 
		sqrt(power((avg(raw_value)-raw_value),2)) 
	FROM
		metrology_post 
	WHERE 
		operation='deposition' 
	AND
		film_material='metal'
	AND
		module='monitor') AS raw_std
FROM 
	deposition_metrics
WHERE 
	module='monitor';
	
SELECT * FROM deposition_std;

-- процедура нахождени€ неравномерности по образцу (в процентном выражении);
DROP FUNCTION IF EXISTS microfabrication.sf_monitor_nu;

DELIMITER // 

CREATE FUNCTION microfabrication.sf_monitor_nu(id VARCHAR(10), slot_n TINYINT)
RETURNS FLOAT READS SQL DATA
BEGIN
	DECLARE std FLOAT;
	DECLARE mean_dep FLOAT;
	
	SET std = (SELECT 
		sqrt(power((avg(raw_value)-raw_value),2)) 
		FROM
			metrology_post 
		WHERE 
			operation='deposition' 
		AND
			film_material='metal'
		AND
			module='monitor'
		AND 
			foup_id=id
		AND
			slot=slot_n);
		
	SET mean_dep = (
		SELECT 
			avg(raw_value) 
		FROM 
			metrology_post 
		WHERE 
			operation='deposition' 
		AND 
			film_material='metal' 
		AND 
			module='monitor'
		AND 
			foup_id=id
		AND
			slot=slot_n); 
	RETURN std * 100 / mean_dep;
END; //
DELIMITER ;

SELECT microfabrication.sf_monitor_nu('AL21', 1);