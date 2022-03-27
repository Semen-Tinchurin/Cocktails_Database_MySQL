import json
import pymysql

LONG_DRINK_GLASSES = ("Харрикейн", "Хайбол", "Слинг", "Бокал для вина", "Коллинз", "Кубок",
                      "Тики-бокал", "Коктейльная креманка", "Пинта", "Калабас")
SHORT_DRINK_GLASSES = ("Коктейльный бокал", "Рокс", "Шампанское блюдце", "Бокал для ирландского кофе",
                       "Флюте", "Бокал сауэр", "Чашка", "Медная кружка", "Коньячный бокал", "Бокал маргарита",
                       "Коническая колба", "Пластиковый стакан", "Банка с крышкой")
SHOT_GLASSES = "Стопка"

with open('new_cocktails_dict.json', 'r', encoding='utf-8') as file:
    file = file.read()
    file = json.loads(file)

with open('recipe_and_ingredients.json', 'r', encoding='utf-8') as dict_of_all:
    dict_of_all = json.load(dict_of_all)


try:
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root_password123',
        database='cocktails',
        cursorclass=pymysql.cursors.DictCursor)
    print('connected')
    print('#' * 30)

    try:
        crs = connection.cursor()

# creating database cocktails, insert data in table cocktails
        # query_create = 'CREATE DATABASE cocktails;'
        # crs.execute(query_create)
        # print('created')

        # query = 'CREATE TABLE cocktails (id int AUTO_INCREMENT, name varchar(255),' \
        #         ' glass varchar(100), PRIMARY KEY (id));'
        # crs.execute(query)
        # print('created')

        # for name_of_cocktail, list_ingredients in file.items():
        #     insert_query = f"INSERT INTO cocktails (name, glass) VALUES " \
        #                    f"('{name_of_cocktail}', '{list_ingredients[1]}');"
        #     crs.execute(insert_query)
        #     connection.commit()

        # add_query = 'ALTER TABLE cocktails ADD type_id int'
        # crs.execute(add_query)
        # connection.commit()

        # update_query = 'UPDATE cocktails SET type_id=1 WHERE glass = "Стопка";'
        # crs.execute(update_query)
        # connection.commit()

        # update_query2 = f'UPDATE cocktails SET type_id=2 WHERE glass in {SHORT_DRINK_GLASSES}'
        # crs.execute(update_query2)
        # connection.commit()

        # update_query3 = f'UPDATE cocktails SET type_id=3 WHERE glass in {LONG_DRINK_GLASSES}'
        # crs.execute(update_query3)
        # connection.commit()

        # update_query4 = 'UPDATE cocktails SET glass = "Стопка" WHERE type_id = 1'
        # crs.execute(update_query4)
        # connection.commit()

        # update_query5 = 'UPDATE cocktails SET type_id = 4 WHERE type_id is null and glass not like "Стопка%"'
        # crs.execute(update_query5)
        # connection.commit()

# creating table cocktails_type, insert data
#         create_query = 'CREATE TABLE cocktails_type (type_id int, type varchar(255));'
#         crs.execute(create_query)
#         print('created')

        # insert_query = 'INSERT INTO cocktails_type VALUES (1, "shot"), (2, "short"), (3, "long"), (4, "custom glass")'
        # crs.execute(insert_query)
        # connection.commit()
        # print('done')

# creating table recipe_and_ingredients, insert data
#         create_query = 'CREATE TABLE recipe_and_ingredients (id int AUTO_INCREMENT, ' \
#                        'recipe varchar(650), ingredients varchar(500), PRIMARY KEY (id));'
#         crs.execute(create_query)
#         print('created')

        # query = 'DELETE FROM recipe_and_ingredients;'
        # crs.execute(query)
        # connection.commit()

# insert ingredients and recipe into table
        for ing, rec in dict_of_all.items():
            rec =  str(rec).replace("['", "").replace("']", "").replace("', '", ", ")
            insert_query = f'INSERT INTO recipe_and_ingredients (ingredients, recipe) ' \
                           f'VALUES ("{ing}", "{rec}");'
            crs.execute(insert_query)
        connection.commit()
        print('done')


    finally:
        connection.close()

except Exception as ex:
    print(ex)
