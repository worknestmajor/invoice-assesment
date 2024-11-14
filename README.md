Create a Virtual Environment:
python -m venv env
`env\Scripts\activate`

Install Dependencies:
pip install -r requirements.txt

Run Migrations:
python manage.py migrate

Run the Application:
python manage.py runserver


API Endpoints:

/api/invoices/	: List all invoices	
http://127.0.0.1:8000/	: Create a new invoice
/api/update/ : update invoices
