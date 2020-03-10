# Instaworks Team Manager

### This project is an assignment

The entire project is Dockerized using Docker-compose.
Comprises of 3 containers: 

*Backend* (Django-based API Engine)
*UI* (React-based User Interface)
*DB* (MySQL database)

### Steps to setup the project

1. Clone the repository into any folder of your choice on your local machine.
2. Browse to the folder containing the __docker-compose.yml__ file using terminal.
3. Build the containers by using the command `sudo docker-compose build`
4. Wait for the build process to complete. 
5. Run the containers by using the command `sudo docker-compose up`
    * In case the *UI* container does not come up, it's safer to use the command 
        `COMPOSE_HTTP_TIMEOUT=200 sudo docker-compose up`
6. API Endpoints are at => [http://localhost:8008/team-manager/api/v1/team_manager/manage_member/] (All CRUD operations permitted)
7. UI URL is => [InstaW Team Management Portal](http://localhost:3000)

### API Payload Format

1. Get Team Member Data:

```
curl -X GET -H "Content-Type:application/json"
http://localhost:8008/team-manager/api/v1/team_manager/manage_member/
```


2. Add Team Member Data:
```
curl -X POST -H "Content-Type:application/json"
http://localhost:8008/team-manager/api/v1/team_manager/manage_member/ -d '{"member_id": 1, "first_name": "David", "last_name": "Jones", "phone": "+15101234567", "emailId": "test@test.com", "role": "ADMIN | REGULAR"}'
```

3. Edit Team Member Data (__PS: Member_ID is a unique field and hence should not be changed via PUT requests__):
```
curl -X PUT -H "Content-Type:application/json"
http://localhost:8008/team-manager/api/v1/team_manager/manage_member/ -d '{"member_id": 1, "first_name": "David", "last_name": "Jones", "phone": "+15101234567", "emailId": "test@test.com", "role": "ADMIN | REGULAR"}'

```

4. Delete Team Member Data:
```
curl -X DELETE -H "Content-Type:application/json"
http://localhost:8008/team-manager/api/v1/team_manager/manage_member/ -d '{"member_id": 1}'
```

