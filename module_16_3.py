from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Эдуард, Возраст: 24'}


@app.get('/users')
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str = Path(min_length=2, max_length=20, description='Enter name', example='Alex'),
                      age: int = Path(ge=18, le=200, description='Enter age', example='18')):
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {f'User {user_id} is registered'}


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int = Path(ge=1, le=999, description='Change id', example='1-999'),
                      username: str = Path(min_length=2, max_length=20, description='Change name', example='John'),
                      age: int = Path(ge=18, le=200, description='Change age', example='24')):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {f'The user {user_id} is updated'}


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=0, le=999, description='Delete id', example='0-999')):
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'
