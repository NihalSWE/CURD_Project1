This Django project implements a simple CRUD (Create, Read, Update, Delete) functionality for managing student records.
The addandshow.html template presents a form for adding new students and displays an interactive table with the existing 
student data. Users can edit individual records by clicking the "Edit" button, leading to the update.html template where 
they can update student information. The "Delete" button triggers the deletion of a student record. The views.py file defines 
functions to handle these operations, including adding, deleting, and updating student records. URL patterns in urls.py connect 
these views to specific URLs. The project structure includes the enroll app, templates, static files for Bootstrap styling, and 
a forms.py file defining a form for student registration based on the User model defined in models.py. Overall, this project serves 
as a foundation for managing student information in a Django web application.





