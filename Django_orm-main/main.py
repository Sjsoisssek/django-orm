import django_setup
from django_orm.models import Role, Admin, User


def create_role(short_role, full_role):
    new_role = Role(short_role=short_role, full_role=full_role)
    new_role.save()
    print(f"Роль '{short_role}' створенно успішно.")
    return new_role


def delete_role(role_id):
    try:
        role = Role.objects.get(id=role_id)
        role.delete()
        print(f"Роль із Id {role_id} успішно видалена.")
    except Role.DoesNotExist:
        print(f"Роль із ID {role_id} не знайдена.")


def create_admin(admin_name, admin_email, admin_role_id):
    try:
        admin_role = Role.objects.get(id=admin_role_id)
        admin = Admin(name=admin_name, email=admin_email, role=admin_role)
        admin.save()
        print(f"Адмін '{admin_name}' створенно успішно.")
    except Role.DoesNotExists:
        print(f"Роль із ID {admin_role_id} не знайдена.")


def delete_admin(admin_id):
    try:
        admin = Admin.objects.get(id=admin_id)
        admin.delete()
        print(f"Адмін із Id {admin_id} успішно видалений.")
    except Admin.DoesNotExists:
        print(f"Адмін із ID {admin_id} не знайдений.")


def create_user(user_name, user_email, user_role_id):
    try:
        user_role = Role.objects.get(id=user_role_id)
        user = User(name=user_name, email=user_email, role=user_role)
        user.save()
        print(f"Користувач '{user_name}' створено успішно.")
    except Role.DoesNotExist:
        print(f"Роль із ID {user_role_id} не знайдена.")


def delete_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        print(f"Користувач із ID {user_id} успішно видалений.")
    except User.DoesNotExist:
        print(f"Користувач із ID {user_id} не знайдений.")


while True:
    print("\n1. Створити роль")
    print("2. Створити нового адміна")
    print("3. Створити нового користувача")
    print("4. Видалити роль")
    print("5. Видалити адміна")
    print("6. Видалити користувача")
    print("7. Вийти")

    choice = input("Виберіть дію (1-7): ")

    if choice == '1':
        short_role = input("Введіть короткий код ролі: ")
        full_role = input("Введіть повну назву ролі: ")
        create_role(short_role, full_role)

    elif choice == '2':
        name = input("Введіть ім'я: ")
        email = input("Введіть email: ")
        role_id = input("Введіть Id ролі: ")
        create_admin(name, email, role_id)

    elif choice == '3':
        name = input("Введіть і'м'я: ")
        email = input("Введіть email: ")
        role_id = input("Введіть Id ролі: ")
        create_user(name, email, role_id)

    elif choice == '4':
        role_id = input("Введіть ID ролі для видалення: ")
        delete_role(role_id)

    elif choice == '5':
        admin_id = input("Введіть ID адміна для видалення: ")
        delete_admin(admin_id)

    elif choice == '6':
        user_id = input("Введіть ID користувача для видалення: ")
        delete_user(user_id)

    elif choice == '7':
        print("Завершення роботи")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")
