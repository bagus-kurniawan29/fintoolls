from django.contrib import admin
from .models import Category, Product, Order

# 1. Konfigurasi Judul Halaman Admin
admin.site.site_header = "FinTools Admin Panel"
admin.site.site_title = "FinTools Dashboard"
admin.site.index_title = "Selamat Datang di Dapur FinTools"

# 2. Tampilan Tabel Produk
class ProductAdmin(admin.ModelAdmin):
    # Kolom yang muncul di tabel
    list_display = ('name', 'formatted_price', 'category', 'is_best_seller', 'image_status')
    
    # Menu filter di sebelah kanan
    list_filter = ('category', 'is_best_seller')
    
    # Kolom yang bisa diedit langsung tanpa masuk ke detail
    list_editable = ('is_best_seller',)
    
    # Kolom pencarian
    search_fields = ('name', 'description')

    # Menampilkan harga dengan format Rp
    def formatted_price(self, obj):
        return f"Rp {obj.price:,}"
    formatted_price.short_description = "Harga"

    # Cek apakah gambar sudah diupload
    def image_status(self, obj):
        return "✅ Ada" if obj.image else "❌ Kosong"
    image_status.short_description = "Gambar"

# 3. Tampilan Tabel Order (Pesanan Masuk) - SUDAH DIPERBAIKI
class OrderAdmin(admin.ModelAdmin):
    # Ganti 'customer_whatsapp' jadi 'customer_email' dan tambah 'is_paid'
    list_display = ('created_at', 'customer_name', 'customer_email', 'product', 'is_paid')
    
    list_filter = ('created_at', 'product', 'is_paid') # Tambah filter status bayar
    search_fields = ('customer_name', 'customer_email')
    
    # Agar data pesanan tidak bisa diubah sembarangan (hanya baca)
    readonly_fields = ('created_at', 'product', 'customer_name', 'customer_email')

    # Mengurutkan dari yang terbaru
    ordering = ('-created_at',)

# 4. Daftarkan ke Admin
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)