import tkinter as tk
import json
import os
from canvas import app
from helpers import clean_screen
from PIL import Image, ImageTk


full_path = os.path.dirname(__file__)


def update_user(username, product_id):
    with open("db/users.txt", "r+", newline="\n") as file:
        users = [json.loads(user.strip()) for user in file]
        for user in users:
            if user["username"] == username:
                user["products"].append(product_id)
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(user) + "\n" for user in users])
                return


def update_product(product_id):
    with open("db/products.txt", "r+") as file:
        products = [json.loads(product.strip()) for product in file]
        for product in products:
            if product["id"] == product_id:
                product["count"] -= 1
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(product) + "\n" for product in products])
                return


def buy_product(product_id):
    clean_screen()

    with open("db/current_user.txt") as file:
        username = file.read()

    if username is not None:
        update_user(username, product_id)
        update_product(product_id)

    render_products_screen()


def add_product(name, image, count):
    with open("db/products.txt", "r+") as file:
        if name == "" or image == "" or count == "":
            render_add_product_screen(error="All fields are required!")
            return
        file.write(json.dumps({
            "id": len(file.readlines()) + 1,
            "name": name,
            "image": image,
            "count": count,
        }) + "\n")
        render_products_screen()


def render_add_product_screen(error=None):
    clean_screen()

    tk.Label(app, text="Name: ").grid(row=0, column=0)
    name = tk.Entry(app)
    name.grid(row=0, column=1)

    tk.Label(app, text="Image: ").grid(row=1, column=0)
    image = tk.Entry(app)
    image.grid(row=1, column=1)

    tk.Label(app, text="Count: ").grid(row=2, column=0)
    count = tk.Entry(app)
    count.grid(row=2, column=1)

    tk.Button(app,
              text="Add",
              command=lambda: add_product(name.get(), image.get(), count.get())
              ).grid(row=3, column=0)

    if error is not None:
        tk.Label(app, text=error).grid(row=4, column=0)


def render_products_screen():
    clean_screen()

    with open("db/current_user.txt") as file:
        username = file.read()
    with open("db/users.txt") as file:
        users = [json.loads(user.strip())for user in file]
        for user in users:
            if user["username"] == username and user["is_admin"]:
                tk.Button(app,
                          text="Add product",
                          command=lambda: render_add_product_screen()
                          ).grid(row=5, column=0)
                break

    with open("db/products.txt") as file:
        products = [json.loads(product.strip()) for product in file]
        for i, product in enumerate(products):
            row = i // 4 * 4
            column = i % 4
            tk.Label(app, text=product["name"]).grid(row=row, column=column)

            img = Image.open(os.path.join(full_path, "db/images", product["img_path"])).resize((100, 100))
            photo_img = ImageTk.PhotoImage(img)
            img_label = tk.Label(image=photo_img)
            img_label.image = photo_img
            img_label.grid(row=row + 1, column=column)

            tk.Label(app, text=product["count"]).grid(row=row + 2, column=column)
            tk.Button(app,
                      text=f"Buy {product['id']}",
                      bg="lightgrey",
                      fg="black",
                      command=lambda p=product["id"]: buy_product(p)
                      ).grid(row=row + 3, column=column)
