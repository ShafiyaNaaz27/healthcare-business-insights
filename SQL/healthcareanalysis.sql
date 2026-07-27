SELECT COUNT(*) AS Total_patients
FROM healthcare_cleaned;

SELECT ROUND(SUM("Billing Amount")::numeric, 2) AS total_revenue
FROM healthcare_cleaned;

SELECT ROUND(AVG("Billing Amount")::numeric, 2) AS average_billing
FROM healthcare_cleaned;

SELECT ROUND(AVG("Lenght_of_stay")::numeric, 2) AS average_stay_days
FROM healthcare_cleaned;

SELECT
    "Gender",
    COUNT(*) AS total_patients
FROM healthcare_cleaned
GROUP BY "Gender"
ORDER BY total_patients DESC;

SELECT
    "Age_Group",
    COUNT(*) AS total_patients
FROM healthcare_cleaned
GROUP BY "Age_Group"
ORDER BY total_patients DESC;

SELECT
    "Medical Condition",
    COUNT(*) AS total_patients
FROM healthcare_cleaned
GROUP BY "Medical Condition"
ORDER BY total_patients DESC;

SELECT
    "Admission Type",
    COUNT(*) AS total_patients
FROM healthcare_cleaned
GROUP BY "Admission Type"
ORDER BY total_patients DESC;

SELECT 
    "Hospital",
    ROUND(SUM("Billing Amount")::numeric, 2) AS revenue
FROM healthcare_cleaned
GROUP BY "Hospital"
ORDER BY revenue DESC
LIMIT 10;

SELECT
    "Insurance Provider",
    ROUND(SUM("Billing Amount")::numeric, 2) AS revenue
FROM healthcare_cleaned
GROUP BY "Insurance Provider"
ORDER BY revenue DESC;

SELECT
    "Medical Condition",
    ROUND(AVG("Billing Amount")::numeric, 2) AS average_billing
FROM healthcare_cleaned
GROUP BY "Medical Condition"
ORDER BY average_billing DESC;

SELECT
    "Admission_Month",
    COUNT(*) AS total_admissions
FROM healthcare_cleaned
GROUP BY "Admission_Month"
ORDER BY MIN("Date of Admission");

SELECT
    "Admission_Quarter",
    COUNT(*) AS total_admissions
FROM healthcare_cleaned
GROUP BY "Admission_Quarter"
ORDER BY "Admission_Quarter";

SELECT
    "Doctor",
    COUNT(*) AS total_patients
FROM healthcare_cleaned
GROUP BY "Doctor"
ORDER BY total_patients DESC
LIMIT 10;

SELECT
    "Hospital",
    COUNT(*) AS total_patients
FROM healthcare_cleaned
GROUP BY "Hospital"
ORDER BY total_patients DESC
LIMIT 10;


















