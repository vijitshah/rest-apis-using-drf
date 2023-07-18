# rest-apis-using-drf
An app that create and uses various Restful APIs to perform CRUD operations using Django Rest Framework aka DRF.

## Step by step instructions to run this project locally
1. Clone Repository.
`git clone https://github.com/vijitshah/rest-apis-using-drf.git`
2. Go inside the folder where project repo has been cloned and create a virtual environment.
`python3 -m venv .venv`
3. Activate the virtual environment.
`source .venv/bin/activate`
4. Install requirements.
`pip install -r requirements.txt`
5. Set up the database.
`python manage.py makemigrations`
`python manage.py migrate`
6. Run the app
`python manage.py runserver`
7. Browse the API endpoint to fire the request as given below - http://127.0.0.1:8000/api/cart-items/

## API requests
API Endpoint - `/api/cart-items/` 
- Method: POST
    - Description: Add the product to the cart.
    - Example
        - Request
        `curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/cart-items/ -d "{\"product_name\":\"apple iphone\",\"product_price\":\"1000\",\"product_quantity\":\"1\"}"`
        - Response
            `{
                "status": "success",
                "data": {
                    "id": 1,
                    "product_name": "apple iphone",
                    "product_price": 1000,
                    "product_quantity": 1
                }
            }`

- Method: GET
    - Description: Lists the product(s) in the cart.
    - Example
        - Request
        `curl -X GET http://127.0.0.1:8000/api/cart-items/`
        - Response
            `{
                "status": "success",
                "data": {
                    "id": 1,
                    "product_name": "apple iphone",
                    "product_price": 1000,
                    "product_quantity": 1
                }
            }`
    - Alternatively, we can also list the product by providing `Id` of the product.
        - Request
        `curl -X GET http://127.0.0.1:8000/api/cart-items/1`
        - Response
        `{
            "status": "success",
            "data": {
                "id": 1,
                "product_name": "apple iphone",
                "product_price": 1000,
                "product_quantity": 1
            }
        }`
- Method: PATCH
    - Description: Update the product(s) in the cart.
    - Example
        - Request
        `curl -X PATCH http://127.0.0.1:8000/api/cart-items/1 -H 'Content-Type: application/json' -d '{"product_quantity":4}'`
        - Response
            `{
                "status": "success",
                "data": {
                    "id": 1,
                    "product_name": "apple iphone",
                    "product_price": 1000,
                    "product_quantity": 4
                }
            }`
- Method: DELETE
    - Description: Delete the product from the cart.
    - Example
        - Request
        `curl -X "DELETE" http://127.0.0.1:8000/api/cart-items/1`
        - Response
            `{
                "status": "success",
                "data": "Item Deleted"
            }`