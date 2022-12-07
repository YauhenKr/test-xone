from categories.models import UserCategory, Category
from user.models import User


def creating_category(user, data):
    category = Category.objects.filter(name_of_category=data['category'])
    if not category.exists():
        get_category = Category.objects.create(name_of_category=data['category'])
    else:
        get_category = category.get()
    UserCategory.objects.create(user=user, category=get_category)


def get_user_categories_list(user):
    user_categories = user.categories.values_list('category_id', flat=True)
    return user_categories


def get_user(request):
    user_name = request.user
    return User.objects.get(user=user_name)


def delete_category(user, category):
    UserCategory.objects.filter(user=user, category=category).delete()

