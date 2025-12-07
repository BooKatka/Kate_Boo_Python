import pytest
from sqlalchemy import create_engine, inspect, text

# Строка подключения
CONN_STR = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

db_engine = create_engine(CONN_STR)

@pytest.fixture(scope="function")
def connection():
    conn = db_engine.connect()
    yield conn
    conn.close()


def test_connect(connection):
    #Проверка подключения к БД и есть нужная таблица
    inspector = inspect(db_engine)
    table_list = inspector.get_table_names()
    assert 'student' in table_list


def test_add_new(connection):
    #добавление новой записи
    new_user_id = 1000

    insert_query = text("INSERT INTO student "
                        "(user_id, level, education_form, subject_id)"
                        "VALUES("
                        ":user_id, :level, :education_form, :subject_id)")

    # Запрос с заданными параметрами
    connection.execute(insert_query, {
        "user_id": new_user_id,
        "level": "Elementary",
        "education_form": "Personal",
        "subject_id": 5
    })

    # Проверка новой записи
    select_query = text("SELECT * FROM student WHERE user_id=:user_id")
    row = connection.execute(select_query, {"user_id": new_user_id}).fetchone()
    assert row is not None, "Запись не была добавлена!"

    # Удаление после теста
    delete_query = text("DELETE FROM student WHERE user_id=:user_id")
    connection.execute(delete_query, {"user_id": new_user_id})


def test_update_user(connection):
    #обновление существующей записи
    updated_level = "Advanced"
    update_user_id = 2000

    #Добавление новой запись перед обновлением
    insert_query = text("INSERT INTO student "
                        "(user_id, level, education_form, subject_id)"
                        "VALUES("
                        ":user_id, :level, :education_form, :subject_id)")
    connection.execute(insert_query, {
        "user_id": update_user_id,
        "level": "Beginner",
        "education_form": "Group",
        "subject_id": 10
    })

    #Обновление уровня студента
    update_query = text(
        "UPDATE student SET level=:new_level WHERE user_id=:user_id")
    connection.execute(update_query, {
        "new_level": updated_level,
        "user_id": update_user_id
    })

    #Проверка обновления
    select_query = text("SELECT level FROM student WHERE user_id=:user_id")
    result = connection.execute(
        select_query, {"user_id": update_user_id}).fetchone()[0]
    assert result == updated_level, "Обновление уровня прошло неудачно."

    #Удаление после теста
    delete_query = text("DELETE FROM student WHERE user_id=:user_id")
    connection.execute(delete_query, {"user_id": update_user_id})


def test_remove_record(connection):
    #Тест на удаление записи
    remove_user_id = 3000

    #Добавление запись для удаления
    insert_query = text("INSERT INTO student "
                        "(user_id, level, education_form, subject_id)"
                        "VALUES("
                        ":user_id, :level, :education_form, :subject_id)")
    connection.execute(insert_query, {
        "user_id": remove_user_id,
        "level": "Advanced",
        "education_form": "Corporate",
        "subject_id": 15
    })

    # Удаление записи
    delete_query = text("DELETE FROM student WHERE user_id=:user_id")
    connection.execute(delete_query, {"user_id": remove_user_id})

    # Проверка, что запись отсутствует в БД
    select_query = text("SELECT COUNT(*) FROM student WHERE user_id=:user_id")
    count = connection.execute(
        select_query, {"user_id": remove_user_id}).scalar()
    assert count == 0, "Удаление записи не сработало."
