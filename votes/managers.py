from djongo import models


class VoteManager(models.Manager):
    pass

"""
class ResultManager(models.Manager):

    def get_queryset(self):
        return super(VoteManager, self).get_queryset().filter(supervisior_id= 0000 )


class Manager(models.Manager):

    def get_queryset(self):
        return super(VoteManager, self).get_queryset().filter(supervisior_id= 0000 )

"""