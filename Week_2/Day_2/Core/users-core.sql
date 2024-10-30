select * from dojos;


INSERT INTO dojos (name)
VALUE ("GROUP1"), ("GROUP2"), ("GROUP3");


delete FROM dojos WHERE ID>0;

INSERT INTO dojos (name)
VALUE ("GROUP4"), ("GROUP5"), ("GROUP6");


select * from ninjas;


INSERT INTO ninjas (first_name, last_name, age, dojos_id ) value ("mounir","ben ammar",37,4), ("ahmed","ben salah",37,4),("kamel","ben mohamed",37,4);
INSERT INTO ninjas (first_name, last_name, age, dojos_id ) value ("patrick","fromage",32,5), ("jean","lamaison",30,5),("celine","dojo",39,5);
INSERT INTO ninjas (first_name, last_name, age, dojos_id ) value ("robert","doe",28,6), ("michel","york",22,6),("stephan","lila",25,6);

select* from ninjas where dojos_id= 4;

select* from ninjas where dojos_id= 5;


SELECT * FROM ninjas	
ORDER BY id desc
limit 1;


select ninjas.id, ninjas.first_name, ninjas.last_name, ninjas.age, ninjas.created_at, ninjas.updated_at, dojos.id, dojos.name, dojos.created_at, dojos.updated_at
from ninjas
join dojos on dojos.id=dojos_id where ninjas.id = 6;


select ninjas.id, ninjas.first_name, ninjas.last_name, ninjas.age, ninjas.created_at, ninjas.updated_at, dojos.id, dojos.name, dojos.created_at, dojos.updated_at
from ninjas
join dojos on dojos.id=dojos_id;



