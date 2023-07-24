# Write your MySQL query statement below
SELECT author_id AS id
FROM Views 
WHERE viewer_id LIKE author_id
GROUP by author_id
ORDER BY author_id ASC