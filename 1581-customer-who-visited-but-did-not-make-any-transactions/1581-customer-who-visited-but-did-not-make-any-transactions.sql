# Write your MySQL query statement below
Select v.customer_id, count(v.customer_id) count_no_trans
from Visits v 
left JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id is NULL
Group By v.customer_id