from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.team_pg import Team_pg
from .models.conversation import Conversation
from .models.notification import Notification
from .models.message import Message
from .models.foro import Foro
from .models.comment import Comment




admin.site.register(User)
admin.site.register(Account)
admin.site.register(Team_pg)
admin.site.register(Comment)
admin.site.register(Conversation)
admin.site.register(Notification)
admin.site.register(Message)
admin.site.register(Foro)
