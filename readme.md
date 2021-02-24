## BlockChain Administration ###

Application allows the blockchain administrator or usecase admin to configure the policies and roles for an use case. And it is allows allows the admins to configure the usecase admins and other users for the required usecases.

#### Application Platform ###
    - Python 3.8+
    - Flask
    - MySQL 8

-   External Dependencies  (Managed by BC Team)
    - blockchain_client
    - registraion usecase cli
    - workstation cli

There are several secrets are required to communicate with various endpoints and those are given below
    - APIGEE secrets required for blockchain client to communicate with blockchain API's
    - HPID secrets are required for HPID integration.

None of the credentails should committed to the git. Currently, all the secrets are mentioned in the developer, docker or server environments.

Please contact srikanth.bhandary1@hp.com to configure the environments.

### Database ###
- Setup a MySQL db and create a database ```bc_administration```.
- Run the following command to run the database migrations.        
         flask db init
         flask db migrate
         flask db upgrade
         
- Run the following command to start the server.
        python3 manage.py runserver -p 3000
            OR
        flask run --port 3000                     
        
Application can be run either through docker image or in a workstation or server directly. Please follow the following steps to run the application.

- Docker 
    - Please make sure you have all the environments ready in the `.docker-env` file and place the file relatively to the `bc_adminstration` folder.
    - Copy the credentials file and place the file relatively to the `bc_adminstration` folder.
    - Build the image by using the command `docker build . -t bc_administration`
    - Run the image by using the command `docker run -p 3000:3000 --env-file ./.docker-env bc_administration:latest bash -c "flask db upgrade && gunicorn --workers 10 'app:create_app()' -b 0.0.0.0:3000"`
    
    - Docker Environments:    
      ```  
        BC_PRIVATE_KEY=
        BC_PUBLIC_KEY=
        FLASK_ENV=development
        HPID_CLIENT=
        HPID_SECRET=
        FLASK_DEBUG=True
        DB_NAME=bc_administration
        DB_USERNAME=root
        DB_PASSWORD=password
        DB_HOST=host.docker.internal
        SECRET_KEY=
        ```
    -  Credentials.txt
         ```
             apikey: <APIGEE_KEY>
             secret: <APIGEE_SECRET>
         ```
- Workstation
     - Please make sure you have all the environments ready in the `.env` file and place the file relatively to the          `bc_adminstration` folder. Similar entries mentioned in the `.docker-env` file should also exist in the `.env` file.
     - Copy the credentials file and place the file relatively to the `bc_adminstration` folder.
     - Run the following command to install the dependencies
        ```pip install -r requirements.txt```
     - Run the command `flask db upgrade`
     - Run the command `python3 managae.py runserver --port 3000`

