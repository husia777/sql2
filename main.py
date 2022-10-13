import psycopg2


def output_of_all_ads(cursor):
    req = """ 
        SELECT 
        ads_1."Id"
        ,ads_1."name"
        , name_author
        , price
        , description
        , name_address
        , is_published
        FROM ads_1 
        JOIN author ON author.author_id = ads_1.author
        JOIN address ON address.address_id = ads_1.address
        ORDER BY ads_1."Id"
    """
    cursor.execute(req)
    rows = cursor.fetchall()
    for row in rows:
        print(', '.join(str(i).replace('\n', '') for i in row))


def ad_output_by_name(cursor, name):
    req = f""" 
        SELECT 
        ads_1."Id"
        ,ads_1."name"
        , name_author
        , price
        , description
        , name_address
        , is_published
        FROM ads_1 
        JOIN author ON author.author_id = ads_1.author
        JOIN address ON address.address_id = ads_1.address        
        WHERE name_author = '{name}'
        ORDER BY ads_1."Id"
    """
    cursor.execute(req)
    rows = cursor.fetchall()
    for row in rows:
        print(', '.join(str(i).replace('\n', '') for i in row))


def ad_output_by_price_range(cursor, from_, to):
    req = f""" 
        SELECT 
        ads_1."Id"
        ,ads_1."name"
        , name_author
        , price
        , description
        , name_address
        , is_published
        FROM ads_1 
        JOIN author ON author.author_id = ads_1.author
        JOIN address ON address.address_id = ads_1.address        
        WHERE price BETWEEN '{from_}'AND '{to}'
        ORDER BY ads_1."price"
        """
    cursor.execute(req)
    rows = cursor.fetchall()
    for row in rows:
        print(', '.join(str(i).replace('\n', '') for i in row))


def get_ads_from_the_city(cursor, name_city):
    req = f""" 
        SELECT 
        ads_1."Id"
        ,ads_1."name"
        , name_author
        , price
        , description
        , name_address
        , is_published
        FROM ads_1 
        JOIN author ON author.author_id = ads_1.author
        JOIN address ON address.address_id = ads_1.address        
        WHERE name_address LIKE '%{name_city}%'
        ORDER BY ads_1."Id"
            """
    cursor.execute(req)
    rows = cursor.fetchall()
    for row in rows:
        print(', '.join(str(i).replace('\n', '') for i in row))


def ad_output_by_name_and_price(cursor, name, from_, to):
    req = f""" 
        SELECT 
        ads_1."Id"
        ,ads_1."name"
        , name_author
        , price
        , description
        , name_address
        , is_published
        FROM ads_1 
        JOIN author ON author.author_id = ads_1.author
        JOIN address ON address.address_id = ads_1.address        
        WHERE name_author = '{name}' and price BETWEEN '{from_}'AND '{to}'
        ORDER BY ads_1."Id"
            """
    cursor.execute(req)
    rows = cursor.fetchall()
    for row in rows:
        print(', '.join(str(i).replace('\n', '') for i in row))


def db_connecting():
    """
    Функция подключения к базе данных
    :return: Возвращает
    """
    try:
        connection = psycopg2.connect(user="postgres"
                                      , password="postgres"
                                      , host="127.0.0.1"
                                      , port="5432"
                                      ,database="testdb")
        print('Подключение к базе данных установленно')
        return connection
    except:
        print('Ошибка подключения')
        return False






def main():
    conn = db_connecting()
    if conn:
        cursor = conn.cursor()

    while True:
        try:
            print('1.Вывести все объявления\n2.Вывести объявления конткретного пользователя\n3.Вывести объявления в диапазоне цен, которые указал пользователь отсортированных в порядке возрастания цены\n4.Вывести объявления для конкретного города\n5.Вывести информацию для определенного пользователя и цены\n6.Вывести информацию о базе данных\n7.Выход')
            user_input = int(input('Введите номер нужной операции'))


            match user_input:
                case 1:
                    output_of_all_ads(cursor)
                case 2:
                    name_ = input('Введите имя человека объявления которого вы хотите увидеть')
                    ad_output_by_name(cursor, name_)
                case 3:
                    from_ = int(input('Введите начальное значение диапазона'))
                    to = int(input('Введите конечное значение диапазона '))
                    ad_output_by_price_range(cursor, from_, to)
                case 4:
                    name_city = input('Введите название города в котором нужно произвести поиск обхявлений')
                    get_ads_from_the_city(cursor, name_city)
                case 5:
                    name_ = input('Введите имя человека объявления которого вы хотите увидеть')
                    from_ = int(input('Введите начальное значение диапазона'))
                    to = int(input('Введите конечное значение диапазона '))
                    ad_output_by_name_and_price(cursor, name_, from_, to)
                case 6:
                    print(conn.get_dsn_parameters(), "\n")
                case 7:
                    break
        except:
            print('Ошибка поиска')
            break

if __name__ == '__main__':
    main()
