from django.db import models
type_mt={
    "FC": "Fan_cosplay",
    "SO": "Sophomore",
    "JR": "Junior",
    "SR": "Senior",
    "GR": "Graduate",
}
visiablitie_type= {
    "+": "Public",
    "#": "Protected",
    "-": "Private",
}



class meetup_data(models.Model):
    id= models.BigAutoField( auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    name_meetup= models.CharField(max_length=30),
    time_start =models.DateTimeField(),
    time_end =models.DateTimeField(),
    discription=models.CharField(max_length=255),
    #Test options 
    type_meetup=models.CharField(max_length=10, choices=type_mt, default='FC')
    location_meetup= models.BigIntegerField(),
    pins=  models.BigIntegerField(),
    visiablitie= models.CharField(max_length=10, choices=visiablitie_type, default='-')


class meetup_userdata(models.Model):
    id= models.BigAutoField( auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    meeting_id = models.BigIntegerField(), 
    #user unknown value  ,
    visiablitie = models.BooleanField(),
    #foreign key (meeting_id) references meetup_data(id)
    #foreign key (user) references ?(?)  ,