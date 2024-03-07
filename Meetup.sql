DROP DATABASE IF EXISTS meetup;
CREATE DATABASE meetup;

USE meetup;

CREATE TABLE meetup_data(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name_meetup VARCHAR(30),
    time_start DATETIME,
    time_end DATETIME,
    discription VARCHAR(255),
    type_meetup VARCHAR(30),
    location_meetup INT not NULL,
    pins int not NULL,
    visiablitie_type VARCHAR(30)
);

CREATE TABLE meetup_userdata(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    meeting_id INT NOT NULL ,
   /* user unknown value  ,*/
     visiablitie BOOLEAN,
     foreign key (meeting_id) references meetup_data(id)
      /*  foreign key (user) references ?(?)  ,*/
);
