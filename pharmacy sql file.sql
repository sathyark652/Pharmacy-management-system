create database pharmacy_ms;

create table customer(cust_id int not null,fname varchar(15),lname varchar(15),
gender varchar(10),dob date,phone varchar(15),address varchar(50),primary key(cust_id));

create table prescription(presc_id int not null,ssn int,drug_name varchar(50) not null,
presc_qty int,presc_date date,primary key(presc_id,drug_name));

 
create table company(cmp_id int not null,fname varchar(20),lname varchar(20),dos date,
license varchar(20),phone varchar(15),primary key(cmp_id));


create table order_o(orderid int not null,presc_id int,cmp_id int,order_qty int,order_date date,
primary key(orderid),constraint fulfilled foreign key(presc_id) references prescription(presc_id),
constraint given_to foreign key(cmp_id) references company(cmp_id));

alter table order_o add cust_id int after cmp_id;
alter table order_o add constraint foreign key(cust_id) references customer(cust_id);

create table medicine(drug_name varchar(50) not null,batch_num varchar(15) not null,
expiry_date date,stock_qty int,price int,med_type varchar(30),primary key(drug_name,batch_num));
alter table medicine add column cmp_id int after batch_num ;
alter table medicine add constraint foreign key(cmp_id) references company(cmp_id);

create table bill(bill_num int not null,cust_id int,order_id int,cust_pay int,total_amt int,
primary key(bill_num),constraint fk1 foreign key(cust_id) references 
customer(cust_id),constraint fk2 foreign key(order_id) references order_o(orderid));

insert into customer values(112,"sanjay","sagarad","male","2002-01-05","9854726458","raichur");
insert into customer(cust_id,fname,lname,gender,dob,phone,address) 
values(152,"john","lukes","male","1999-11-06","8542685471","america"),
(256,"pallavi","naik","female","1999-10-08","7842569854","bangalore"),
(325,"tharun","sena","male","2000-06-03","6587458698","mumbai");
insert into prescription values(156,1,"ambrosol",2,"2022-08-11");
insert into prescription values(352,3,"Monticope",4,"2022-08-10"),
(086,4,"paracetomol",6,"2022-07-11");
insert into prescription values(214,2,"DOLO650",5,current_date());
insert into company values(2582,"sun","pharma","1989-06-06","as021","7584698547");
insert into company(cmp_id,fname,lname,dos,license,phone)
values(302,"biocon","pvt ltd","1986-02-02","AB8970","8456975258"),
(123,"mankind","pvt ltd","1986-04-03","AB5842","9856472158");
update company set license ="AB3333" where cmp_id = 2582;
update company set license ="AB3333" where cmp_id = 2582;
insert into order_o values(523,156,2582,50),(652,86,123,256,"2022-07-12",35);
insert into medicine values ("ambrosol","AD768","2021-06-05",530,120,"syrup"),
("DOLO650","TB768","2021-06-05",730,50,"tablet");
update medicine set expiry_date = "2024-05-03" where price =50;
update medicine set cmp_id =123 where drug_name ="ambrosol";
update medicine set cmp_id =302 where drug_name ="dolokind";
update medicine set cmp_id =2582 where drug_name ="Monticope";

insert into bill values(5682,112,523,6000,3500),(254,256,652,500,1050);
