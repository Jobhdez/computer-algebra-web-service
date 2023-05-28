from django.contrib import admin
from .models import Friend_Request, DiffExpression, LinearAlgebra, Polynomial
from .models import DiffComment, LalgComment, PolyComment

admin.site.register(Friend_Request)
admin.site.register(DiffExpression)
admin.site.register(LinearAlgebra)
admin.site.register(Polynomial)
admin.site.register(DiffComment)
admin.site.register(LalgComment)
admin.site.register(PolyComment)
