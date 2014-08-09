from django.db import models

from django.contrib.auth.models import User

from django.db.models import Count

class PostVoteCountManager(models.Manager):
    def get_query_set(self):
        return super(PostVoteCountManager, self).get_query_set().annotate(
            votes=Count('vote')).order_by('-votes')

class Post(models.Model):
    title = models.CharField("Headline", max_length=100)
    submitter = models.ForeignKey(User)
    submitted_on = models.DateTimeField(auto_now_add=True)
    rank_score = models.FloatField(default=0.0)
    #url = models.URLField("URL", max_length=250, blank=True)
    description = models.TextField(blank=True)

    with_votes = PostVoteCountManager()
    objects = models.Manager() #default manager

    def __unicode__(self):
        return self.title

class Vote(models.Model):
    voter = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return "%s upvoted %s" % (self.voter.username, self.post.title)