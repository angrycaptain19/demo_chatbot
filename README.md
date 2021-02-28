## Setup Steps

1. `rasa shell --debug`
2. `rasa run actions -vv`
3. `docker build -t mysql-example -f docker/mysql/Dockerfile .`   
3. `docker run -e MYSQL_ROOT_PASSWORD=yourpassword -P mysql-example`
4. `docker run -d -p 8000:8000 rasa/duckling:latest`

Note: Please change the mysql password and modify PWD constant available in `actions/constants location

Case1: User provides incomplete information

```
Your input ->  I want to book                                                                                                         
Please provide the space you are looking for. Is it Office/Cubicles/Recreational Space?
Your input ->  Cubicle                                                                                                                
Please provide the floor number are you looking for.
Your input ->  1                                                                                                                      
Please provide the name of space if you remember.
Your input ->  I dont know                                                                                                            
Hi Booking done for Cube1 Seating number- 1 Floor number- 1
```

Case2: User provides time duration of booking

```
Your input ->  Book a pool table                                                                                                      
Provide the duration of booking
Your input ->  2pm to 5pm                                                                                                             
Please provide the name of space if you remember.
Your input ->  dont know                                                                                                              
Hi Booking done for recreation Seating number- 1 Floor number- 10  from 2021-02-28T14:00 to 2021-02-28T18:00

```

Case3: User access the cubicle which is full capacity.

````
Your input ->  Please book available individual seating space                                                                         
Please provide the floor number are you looking for.
Your input ->  6                                                                                                                      
Please provide the name of space if you remember.
Your input ->  dont know                                                                                                              
Sorry we could not find a seat for you. The room cannot accomodate more people as per COVID-19 norms of the company
````

Case4: User access the cubicle which is already occupied.

```
Your input ->  Please book available individual seating space                                                                         
Please provide the floor number are you looking for.
Your input ->  5                                                                                                                      
Please provide the name of space if you remember.
Your input ->  dont know                                                                                                              
Sorry we could not find result.This can be due to the seats is occupied by 4657 employee id

```

Case5: Seat not sanitized

```
Your input ->  book an empty space                                                                                                    
Please provide the floor number are you looking for.
Your input ->  4                                                                                                                      
Please provide the name of space if you remember.
Your input ->  dont know                                                                                                              
Sorry we could not find a seat for you. This can be due to seat of preference with seat id 14 is not sanitized
```

Case6: Slot filling

```
Your input ->  I would like to book available individual seating space at floor number 1 with cubicle name Cube2                                                   
Hi Booking done for Cube1 Seating number- 1 Floor number- 1
```

Case7: Pool table with participants

```

```
