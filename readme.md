#to study
explain the diference between asyncio + aiohttp(non blocking io) and threadpoolexecuter(thread-based concurrency)


#constraints
python <= 3.12

# Create a Virtual Environment with Python <= 3.12

In order to run our app we first need to install some requirements, they are located in the requeirements.txt file, in order to do that we need first to create a venv:

windows
´
python -m venv venv
.\venv\Scripts\activate
´
linux

´
python -m venv venv
.\venv\bin\activate
´

will need a .env file with the following content

`
export API_TOKEN='<ValidTokenFromCoinGecko>'
`
