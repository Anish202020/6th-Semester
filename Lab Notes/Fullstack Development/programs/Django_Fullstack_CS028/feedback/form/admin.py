from django.contrib import admin

from .models import Product, Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer_name', 'date', 'happy',)
    list_filter = ('product', 'date',)
    search_fields = ('product__name', 'details',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Product)