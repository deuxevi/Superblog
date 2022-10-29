from django.contrib import admin

from utilisateur.models import User
from blogs.models import *

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'first_name', 'last_name', 'password', 'role')



class ArticlesAdmin(admin.ModelAdmin):
	list_display = ('title', 'contenu', 'author', 'published', 'date_pub', 'date_mod','theme', 'slug')
	#list_editable = ('title', 'contenu', 'published', 'theme')


class CommentsAdmin(admin.ModelAdmin):
	list_display = ('article', 'contenu', 'internaute', 'date')
	#list_editable = ('contenu',)

#class ThemesAdmin(admin.ModelAdmin):
#	list_display=('theme')

admin.site.register(User, UserAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Themes)
admin.site.register(Likes)
admin.site.register(Enregistrements)