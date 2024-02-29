CREATE DATABASE student_management_system;

USE student_management_system;

-- DROP DATABASE student_management_system;

# CREATE TABLE FOR LOGIN DETAILS
CREATE TABLE login_details(
    id VARCHAR(12) PRIMARY KEY NOT NULL,
    uname VARCHAR(45) NOT NULL,
    password VARCHAR(255) NOT NULL,
    typeofuser VARCHAR(45) NOT NULL
);

# ENTER THE SUPER ADMIN DETAILS
INSERT INTO login_details VALUES ("", "", MD5(""), "");

# CREATE THE ADMIN TABLE
CREATE TABLE admin(
    id VARCHAR(8) PRIMARY KEY NOT NULL,
    name VARCHAR(45) NOT NULL UNIQUE,
    address TEXT NOT NULL,
    phoneno BIGINT NOT NULL,
    age INT NOT NULL,
    sex VARCHAR(10) NOT NULL
);

# CREATING THE STORED PROCEDURE TO ADD THE ADMIN ID AUTOMATICALLY
DELIMITER &&
CREATE PROCEDURE addadmin(IN name VARCHAR(255), IN address TEXT, IN phoneno BIGINT, IN age INT, IN sex VARCHAR(10))
BEGIN
    DECLARE countad INT DEFAULT 0;
    DECLARE i INT DEFAULT 1000;
    DECLARE idreturn VARCHAR(8);
    DECLARE getid VARCHAR(8);
    SELECT COUNT(*) INTO countad FROM admin;
    SET i = countad + i;
    SET idreturn = CONCAT("AD", i);
    INSERT INTO admin VALUES (get_correct_fid(idreturn), name, address, phoneno, age, sex);
END &&
DELIMITER ;

# TRIGGER FOR DELETING THE RECORD FROM ADMIN AND AUTOMATICALLY FROM LOGIN DETAILS
DELIMITER &&
CREATE TRIGGER auto_delete_login AFTER DELETE ON admin 
FOR EACH ROW
BEGIN
    DELETE FROM login_details WHERE id = old.id;
END &&
DELIMITER ;

# CREATE TABLE FOR FACULTY
CREATE TABLE faculty (
    id VARCHAR(8) PRIMARY KEY NOT NULL,
    first_name VARCHAR(45) NOT NULL,
    middle_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    experience INT NOT NULL,
    doj DATE NOT NULL,
    dob DATE NOT NULL,
    email VARCHAR(255) NOT NULL,
    sub VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    qualification TEXT NOT NULL,
    age INT NOT NULL,
    sex VARCHAR(8) NOT NULL,
    phoneno BIGINT NOT NULL
);

# STORED PROCEDURE TO ADD THE FACULTY ID AUTOMATICALLY
DELIMITER &&
CREATE PROCEDURE addfaculty(IN fn VARCHAR(45), IN mn VARCHAR(45), IN ln VARCHAR(45), IN exp INT, IN doj DATE, IN dob DATE, IN email VARCHAR(255), IN sub VARCHAR(255), IN address TEXT, IN quali TEXT, IN age INT, IN sex VARCHAR(8), IN phone BIGINT)
BEGIN
    DECLARE countad INT DEFAULT 0;
    DECLARE i INT DEFAULT 10000;
    DECLARE idreturn VARCHAR(8);
    DECLARE getid VARCHAR(8);
    SELECT id INTO getid FROM faculty ORDER BY id DESC LIMIT 1;
    SELECT COUNT(*) INTO countad FROM faculty;
    SET i = countad + i;
    SET idreturn = CONCAT("FT", i);
    INSERT INTO faculty VALUES (get_correct_aid(idreturn), fn, mn, ln, exp, doj, dob, email, sub, address, quali, age, sex, phone);
END &&
DELIMITER ;

# TRIGGER FOR DELETING THE RECORD FROM FACULTY AND AUTOMATICALLY FROM LOGIN DETAILS
DELIMITER &&
CREATE TRIGGER auto_delete_login_faculty AFTER DELETE ON faculty 
FOR EACH ROW
BEGIN
    DELETE FROM login_details WHERE id = old.id;
    DELETE FROM div_details WHERE faculty_id = old.id;
END &&
DELIMITER ;

# CREATE TABLE FOR KEEPING THE STUDENT RECORD
CREATE TABLE student(
    id VARCHAR(8) NOT NULL PRIMARY KEY,
    first_name VARCHAR(45) NOT NULL,
    middle_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    roll_no INT NOT NULL,
    division CHAR(1) NOT NULL,
    address TEXT NOT NULL,
    father_name VARCHAR(100) NOT NULL,
    mother_name VARCHAR(100) NOT NULL,
    std INT NOT NULL,
    dob DATE NOT NULL,
    bloodgroup CHAR(4),
    doa DATE NOT NULL,
    father_occ VARCHAR(100),
    mother_occ VARCHAR(100),
    phoneno BIGINT NOT NULL,
    sex VARCHAR(10) NOT NULL
);

# CREATE TABLE FOR ASSIGNING THE CLASS TEACHER
CREATE TABLE div_details(
    std INT,
    divison CHAR(1),
    faculty_id VARCHAR(8),
    FOREIGN KEY (faculty_id) REFERENCES faculty(id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

# CREATING A TRIGGER TO DELETE THE DIV DETAILS 
DELIMITER &&
CREATE TRIGGER delete_from_div BEFORE DELETE ON faculty 
FOR EACH ROW
BEGIN
    DELETE FROM div_details WHERE faculty_id = old.id;
END &&
DELIMITER ;

# TO ADD THE CORRECT ADMIN ID
DELIMITER &&
CREATE FUNCTION get_correct_fid(idi VARCHAR(8))
RETURNS VARCHAR(8)
DETERMINISTIC
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE rore VARCHAR(8);
    DECLARE noofro INT;
    DECLARE ex_id INT;
    DECLARE returnid VARCHAR(8);
    SELECT COUNT(*) INTO noofro FROM admin; 
    id_label:LOOP
        SELECT id INTO rore FROM admin ORDER BY id LIMIT 1 OFFSET i;
        SELECT SUBSTRING(rore, 3, 5) INTO ex_id;
        IF i >= noofro THEN RETURN idi;
        ELSEIF rore = idi THEN 
            SET ex_id = ex_id + 1;
            SET idi = CONCAT("AD", ex_id);
            SET i = i + 1;
        ELSE SET i = i + 1;
        END IF;
    END LOOP;
END &&
DELIMITER ;

# FOR ADDING THE CORRECT FACULTY ID 
DELIMITER &&
CREATE FUNCTION get_correct_aid(idi VARCHAR(8))
RETURNS VARCHAR(8)
DETERMINISTIC
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE rore VARCHAR(8);
    DECLARE noofro INT;
    DECLARE ex_id INT;
    SELECT COUNT(*) INTO noofro FROM faculty; 
    id_label:LOOP
        SELECT id INTO rore FROM faculty ORDER BY id LIMIT 1 OFFSET i;
        SELECT SUBSTRING(rore, 3, 5) INTO ex_id;
        IF i >= noofro THEN RETURN idi;
        ELSEIF rore = idi THEN 
            SET ex_id = ex_id + 1;
            SET idi = CONCAT("FT", ex_id);
            SET i = i + 1;
        ELSE SET i = i + 1;
        END IF;
    END LOOP;
END &&
DELIMITER ;

DESCRIBE student;

# CREATE A PROCEDURE TO ADD THE STUDENT ID
DELIMITER &&
CREATE PROCEDURE addstudent(
    IN f_name VARCHAR(45), IN m_name VARCHAR(45), IN l_name VARCHAR(45), 
    IN rolno INT, IN divi CHAR(1), IN addr TEXT,
    IN father_n VARCHAR(100), IN mother_n VARCHAR(100), IN std INT, 
    IN dob DATE, IN bg CHAR(4), IN doa DATE, IN father_occ VARCHAR(100), 
    IN mother_occ VARCHAR(100),  IN phone BIGINT,  IN sex VARCHAR(10))
BEGIN
    DECLARE countad INT DEFAULT 0;
    DECLARE i INT DEFAULT 10000;
    DECLARE idreturn VARCHAR(8);
    DECLARE getid VARCHAR(8);
    SELECT COUNT(*) INTO countad FROM admin;
    SET i = countad + i;
    SET idreturn = CONCAT("ST", i);
    INSERT INTO student VALUES (get_correct_sid(idreturn), f_name, m_name, l_name, rolno, divi, addr, father_n, mother_n, std, dob, bg, doa, father_occ, mother_occ, phone, sex);
END &&
DELIMITER ;

# FUNCTION TO GET THE CORRECT ID FOR STUDENT
DELIMITER &&
CREATE FUNCTION get_correct_sid(idi VARCHAR(8))
RETURNS VARCHAR(8)
DETERMINISTIC
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE rore VARCHAR(8);
    DECLARE noofro INT;
    DECLARE ex_id INT;
    SELECT COUNT(*) INTO noofro FROM student; 
    id_label:LOOP
        SELECT id INTO rore FROM student ORDER BY id LIMIT 1 OFFSET i;
        SELECT SUBSTRING(rore, 3, 5) INTO ex_id;
        IF i >= noofro THEN RETURN idi;
        ELSEIF rore = idi THEN 
            SET ex_id = ex_id + 1;
            SET idi = CONCAT("ST", ex_id);
            SET i = i + 1;
        ELSE SET i = i + 1;
        END IF;
    END LOOP;
END &&
DELIMITER ;

# CREATING TRIGGER TO AUTO DELETE THE LOGIN DETAILS FORM THE STUDENT
DELIMITER &&
CREATE TRIGGER dele_student_login AFTER DELETE ON student
FOR EACH ROW
BEGIN
    DELETE FROM login_details WHERE id = old.id;
END &&
DELIMITER ;

# CREATING THE TABLE FOR STORING THE FEES FOR EACH YEAR
CREATE TABLE store_fees(
    year_ YEAR NOT NULL PRIMARY KEY,
    monthly INT,
    yearly INT
);

# CREATING TABLE FOR FEES 
CREATE TABLE fees (
    id VARCHAR(8) NOT NULL,
    fullyearpaid ENUM("Y","N"),
    year_ YEAR NOT NULL,
    jan ENUM("Y","N"), feb ENUM("Y","N"), mar ENUM("Y","N"),
    april ENUM("Y","N"), may ENUM("Y","N"), june ENUM("Y","N"),
    july ENUM("Y","N"), aug ENUM("Y","N"), sept ENUM("Y","N"),
    oct ENUM("Y","N"), nov ENUM("Y","N"), dece ENUM("Y","N"),
    FOREIGN KEY (id) REFERENCES student(id) ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (year_) REFERENCES store_fees(year_) ON DELETE NO ACTION ON UPDATE NO ACTION
);


# CREATE A TRIGGER TO AUTO ADD THE STUDENT IN THE FEES TABLE
DELIMITER &&
CREATE TRIGGER auto_add_fees AFTER INSERT ON student
FOR EACH ROW
BEGIN
    INSERT INTO fees VALUES (NEW.id, "N", YEAR(NEW.doa), "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N");
END &&
DELIMITER ;

# CREATE PROCEDURE TO ADD THE FEES 
DELIMITER &&
CREATE PROCEDURE add_fees(IN id_c VARCHAR(8), IN ye YEAR)
BEGIN
    INSERT INTO fees VALUES (id_c, "N", ye, "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N");
END &&
DELIMITER ;

# CREATING THE PRESENT WORKING DAYS TABLE
CREATE TABLE present(present_date DATE PRIMARY KEY NOT NULL);

# CREATING A TABLE FOR THE ATTENDANCE
CREATE TABLE attendance(
    id VARCHAR(8) NOT NULL,
    attended ENUM("Y","N"),
    date_attend DATE,
    FOREIGN KEY (date_attend) REFERENCES present(present_date)
);

# CREATING A FUNCTION FOR GETTING ABSENT OR PRESENT
DELIMITER &&
CREATE FUNCTION get_presentee(PA CHAR(1))
RETURNS VARCHAR(45)
DETERMINISTIC
BEGIN
    IF PA = "Y" THEN RETURN "Present";
    ELSEIF PA = "N" THEN RETURN "Absent";
    END IF;
END &&
DELIMITER ;
