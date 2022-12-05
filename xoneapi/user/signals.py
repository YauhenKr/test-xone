def post_save_user(sender, instance, created, **kwargs):

    from categories.models import BasicCategory, UserCategory

    if not instance.created:
        categories_list = BasicCategory.objects.first().categories.all()
        for category in categories_list:
            UserCategory.objects.create(user=instance, category=category)
        instance.created = True
        instance.save()
