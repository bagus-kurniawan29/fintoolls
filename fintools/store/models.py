from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0) 
    discount_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    
    # Link Google Drive/MediaFire
    download_link = models.URLField(max_length=500, blank=True, null=True, help_text="Link GDrive/Mediafire")
    
    is_best_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    
    # Pastikan baris ini ada (Email pengganti WA)
    customer_email = models.EmailField()
    
    # Pastikan baris ini ada (Status Pembayaran) <-- INI YANG BIKIN ERROR KALAU HILANG
    is_paid = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.product.name}"

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='comment_images/', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.text[:20]}"