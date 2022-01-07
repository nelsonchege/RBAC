# RBAC
a simple Role based Access Control App 

for the app the super Admin is the only person how can get,post,update and delete users namely mainusers

a user (mainuser) can post subusers using there user_id as a foreign key to the sub-user

### to get the database run the following inside the virtual environment

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py createsuperuser (this will act as the admin to the system)
