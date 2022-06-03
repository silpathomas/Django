from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    is_active = models.BooleanField()


    def __unicode__(self):
        return '%s' % (self.name)



class Policy(models.Model):
    # user_id = models.ForeignKey(User)

    user_id=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default="", null=True
    )
    hash_id = models.UUIDField(default=uuid.uuid4, editable=False)
    start_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=150, null=True)

class Page(models.Model):
    name = models.CharField(max_length=150, null=True)


class Visit(models.Model):
    policy_id = models.ForeignKey(Policy, related_name="policy", on_delete=models.CASCADE)
    page_id = models.ForeignKey(Page, related_name="page", on_delete=models.CASCADE)
   

class Queries(models.Model):
	query_set = models.TextField()
    



   