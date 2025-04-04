import json
def save_user_info(name, age, email):
    user_info = {
        "name": name,
        "age": age,
        "email": email
    }
    with open('user_info.json', 'w') as file:
        json.dump(user_info, file)
# Пример использования
save_user_info("Alice", 25, "alice@example.com")