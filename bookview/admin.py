from django.contrib.admin import AdminSite


class BookviewAdminSite(AdminSite):
    site_header = "Bookview Admin"
    site_title = "Bookview Admin"


admin_site = BookviewAdminSite()
