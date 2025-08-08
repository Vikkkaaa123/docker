CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name varchar(50),
    last_name varchar(50),
    age int,
    university varchar(100)
);

INSERT INTO students (first_name, last_name, age, university) 
VALUES 
('Иван', 'Иванов', 20, 'МГУ'),
('Петр', 'Петров', 21, 'СПбГУ'),
('Анна', 'Сидорова', 19, 'НГУ'),
('Мария', 'Кузнецова', 22, 'МФТИ');
