# Klein
🖇️ The most intelligent URL shortening framework on the planet.

## Setup
1. Create a virtual environment:
```
mkvirtualenv klein
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Setup environment variables
```
cd klein && cp .env.example .env && vim .env
```

4. Run migrations
```
./manage.py migrate
```

5. Run server
```
./manage.py runserver
```
