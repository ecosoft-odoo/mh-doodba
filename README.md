Installation Note:

* Install Doodba as normal, make sure to use postgres 9.6
* To install Java 7 add following in apt.txt, and run > invoke img-build

```
openjdk-7-jdk
```

* To restore database

```
# copy file into postgres container
docker cp <file path> <postgres container name>:<file path>

# Move into postgres container
docker exec -it -u 0 <postgres container name> bash
```

* Ininstall Jasper Report and Java 7 on your local machine
