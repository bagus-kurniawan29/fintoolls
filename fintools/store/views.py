from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import Product, Comment, Order
from .forms import OrderForm, CommentForm

def home(request):
    products = Product.objects.all()
    featured_product = Product.objects.filter(is_best_seller=True).first()
    context = {
        'products': products,
        'featured': featured_product
    }
    return render(request, 'index.html', context)

def checkout(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            # Redirect ke halaman pembayaran QRIS
            return redirect('payment', pk=order.pk)
    else:
        form = OrderForm()

    context = {
        'product': product,
        'form': form
    }
    return render(request, 'checkout.html', context)

# --- VIEW BARU: Halaman Pembayaran QRIS ---
def payment(request, pk):
    order = get_object_or_404(Order, pk=pk)
    
    if request.method == 'POST':
        # Simulasi verifikasi pembayaran sukses
        order.is_paid = True
        order.save()
        
        # --- KIRIM EMAIL OTOMATIS ---
        subject = f'Link Download Produk: {order.product.name}'
        message = f'''Halo {order.customer_name},
        
Terima kasih telah melakukan pembayaran Rp 1.
Berikut adalah link download produk Anda:

{order.product.download_link}

Selamat belajar!
Tim FinTools
        '''
        # Pastikan EMAIL_HOST_USER di settings.py sudah diatur nanti
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [order.customer_email],
                fail_silently=True, # Agar tidak error jika SMTP belum setting
            )
        except:
            pass # Abaikan error email untuk sementara (biar tidak crash)

        return redirect('success', pk=order.pk)

    return render(request, 'payment.html', {'order': order})

def success(request, pk):
    order = get_object_or_404(Order, pk=pk)
    # Hanya boleh akses sukses jika sudah bayar
    if not order.is_paid:
        return redirect('payment', pk=order.pk)
        
    return render(request, 'success.html', {'order': order})

def discussion(request):
    comments = Comment.objects.filter(parent=None).order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES) 
        if form.is_valid():
            comment = form.save(commit=False)
            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)
                comment.parent = parent_comment
            comment.save()
            return redirect('discussion')
    else:
        form = CommentForm()
    return render(request, 'discussion.html', {'comments': comments, 'form': form})

def like_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.likes += 1
    comment.save()
    return redirect('discussion')

def lynk(request):
    products = Product.objects.all()
    return render(request, 'lynk.html', {'products': products})