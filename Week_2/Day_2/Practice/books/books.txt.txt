select * from users;


INSERT INTO users (name)
VALUE ("Jane Amsden"), ("Emily Dixon"), ("Theodore Dostoevsky"), ("William Shapiro"), ("Lao Xiu");



select * from books;

INSERT INTO books (title)
VALUE (" C Sharp"), ("Java"), ("Python"), ("PHP"), ("Ruby");


update books
set title = "C#"
where id = 1;

update users
set name = "Bill"
where id = 4;



select * from favorites;

INSERT INTO favorites (user_id, book_id)
VALUE (1,1), (1,2);


INSERT INTO favorites (user_id, book_id)
VALUE (2,1), (2,2), (2,3);


INSERT INTO favorites (user_id, book_id)
VALUE (3,1), (3,2), (3,3), (3,4);

INSERT INTO favorites (user_id, book_id)
VALUE (4,1), (4,2), (4,3), (4,4), (4,5);


SELECT *
from users
left join favorites on users.id = favorites.user_id
left join books on books.id= favorites.book_id
where favorites.book_id = 3;


DELETE
FROM favorites
WHERE book_id = 3
order by user_id
limit 1;

INSERT INTO favorites (user_id, book_id)
VALUE (5,2);

select users.name, books.title  
from users
join favorites on users.id = favorites.user_id
join books on books.id = favorites.book_id
where users.id = 3 ;


select users.name, books.title,  books.id  
from users
join favorites on users.id = favorites.user_id
join books on books.id = favorites.book_id
where books.id = 5 ;







