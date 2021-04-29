--Creates a stored procedure avg
DELIMITER //
CREATE PROCEDURE ComputeOverallScoreForUser
(IN user_id INT)
BEGIN UPDATE users SET overall_score =
   (SELECT AVG(score) FROM corrections WHERE corrections.user_id=user_id GROUP BY corrections.user_id )
   WHERE id=user_id;
END//
DELIMITER ;