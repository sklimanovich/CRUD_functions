from fastapi import FastAPI
from db import Db


app = FastAPI()
db = Db()


# get
@app.get("/")
def all_posts():
    connection = db.connection_pool
    cursor = connection.cursor()

    if cursor:
        sql = "SELECT * FROM posts ORDER BY id LIMIT 10"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    else: 
        return {"Error":"Something went wrong!"}


# create
@app.post("/")
def create_post(title: str, content: str):
    connection = db.connection_pool
    cursor = connection.cursor()

    if cursor:
        sql = "INSERT INTO posts (title, content) VALUES (%s, %s)"
        
        values = (title, content)

        cursor.execute(sql, values)
        connection.commit()

        return {"message":"Post created!"}
    else: 
        return {"Error":"Something went wrong!"}


# delete
@app.delete("/{post_id}")
def delete_post(post_id: int):
    connection = db.connection_pool
    cursor = connection.cursor()

    if cursor:
        sql = "DELETE FROM posts WHERE id=%s"

        cursor.execute(sql, post_id)
        connection.commit()

        return {"message":"Post deleted!"}
    else: 
        return {"Error":"Something went wrong!"}
    

# update
@app.put("/{post_id}")
def update_post(post_id: int, title: str, content: str):
    connection = db.connection_pool
    cursor = connection.cursor()

    if cursor:
        sql = "UPDATE posts SET title=%s, content=%s WHERE id=%s"

        values = (title, content, post_id)

        cursor.execute(sql, values)
        connection.commit()

        return {"message":"Post updated!"}
    else: 
        return {"Error":"Something went wrong!"}
    