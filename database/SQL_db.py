import sqlite3 as sq



def sql_start():
    global base, cur
    base = sq.connect('Shop.db')
    cur = base.cursor()
    if base:
        print('Database was connected')
    cur.execute("CREATE TABLE IF NOT EXISTS menu (product_id INTEGER PRIMARY KEY AUTOINCREMENT, img TEXT, name TEXT, description TEXT, price TEXT)")
    base.commit()
        
        
async def sql_add_comand(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO menu (img, name, description, price) VALUES (?, ?, ?, ?)", tuple(data.values()))
        base.commit
        

async def get_all_products():
    products = cur.execute("SELECT * FROM menu").fetchall()
    return products


async def get_product_img(prduct_id):
    img_query = "SELECT img FROM menu WHERE product_id = ?"
    img = cur.execute(img_query, (prduct_id,)).fetchone() 
    return img


async def get_product_title(prduct_id):
    title_query = "SELECT name FROM menu WHERE product_id = ?"
    title = cur.execute(title_query, (prduct_id,)).fetchone() 
    return title


async def get_product_description(prduct_id):
    description_query = "SELECT description FROM menu WHERE product_id = ?"
    description = cur.execute(description_query, (prduct_id,)).fetchone() 
    return description

async def get_product_price(prduct_id):
    price_query = "SELECT price FROM menu WHERE product_id = ?"
    price = cur.execute(price_query, (prduct_id,)).fetchone() 
    return price[0] if price else "0.0"


async def delete_product (prduct_id: int) -> None:
    cur.execute("DELETE FROM menu WHERE product_id = ?", (prduct_id,))
    base.commit()