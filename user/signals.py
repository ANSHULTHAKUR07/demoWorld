from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from user.models import ShoppingUser, Profile
from django.dispatch import receiver

user = ShoppingUser()

@receiver(post_save, sender=ShoppingUser)
def create_profile(sender, instance, created, **kwargs):
    print(sender, "---------->>>  sender")
    print(instance, "---------->>>  instance")
    print(created, "---------->>>  created")
    if created:
        Profile.objects.create(user = instance)
