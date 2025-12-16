from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count 
from .models import*


def blog_details(request):
    dept_id = Department.objects.all()
    print("Department Data:", dept_id)
    total_cart_price = Cart.get_cart_total()
    
    context = {
        "dept_id" : dept_id,
        "total_cart_price": total_cart_price
        }
    return render(request, 'blog_details.html', context)

# ___________________________________________________________Blog page________________________________________________________

def blog(request):
    dept_id = Department.objects.all()
    print("Department Data:", dept_id)
    total_cart_price = Cart.get_cart_total()
    
    context = {
        "dept_id" : dept_id,
        "total_cart_price": total_cart_price
        }
    return render(request, 'blog.html', context)

# ___________________________________________________________Check-Out page________________________________________________________

def checkout(request):
    
    if request.method=='POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        
        billing_detail = Billingdetail(
            f_name=f_name,
            l_name=l_name,
            email=email,
            phone=phone,
            address=address,
            city=city
        )
        billing_detail.save()
        
        return redirect('checkout') 
        
    dept_id = Department.objects.all()
    print("Department Data:", dept_id)
    
    cart_items = Cart.objects.all()
    total_cart_price = Cart.get_cart_total()
        
        
    context = {
        "dept_id" : dept_id,
        "cart_items": cart_items,
        "total_cart_price": total_cart_price
        }
    return render(request, 'checkout.html', context)

# ___________________________________________________________Contact page________________________________________________________

def contact(request):
    dept_id = Department.objects.all()
    print("Department Data:", dept_id)
    total_cart_price = Cart.get_cart_total()
    
    context = {
        "dept_id" : dept_id,
        "total_cart_price": total_cart_price
        }
    return render(request, 'contact.html', context)

# ___________________________________________________________Index page________________________________________________________

def index(request):
    dept_id = Department.objects.all()
    cart_items = Cart.objects.all()
    total_cart_price = Cart.get_cart_total()
    
    shop_id = request.GET.get('shop_id')
    search_query = request.GET.get('search')

    product_id = Product.objects.all()
    
    if shop_id:
        product_id = product_id.filter(Department=shop_id)
    
    if search_query:
        product_id = product_id.filter(product_name__icontains=search_query)
    
    context = {
        "dept_id": dept_id,
        "shop_id": shop_id,
        "cart_items": cart_items,
        "product_id": product_id,
        "total_cart_price": total_cart_price,
        "search": search_query
    }
    return render(request, 'index.html', context)


# ___________________________________________________________Login page________________________________________________________

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            uid = User_Detail.objects.get(email=email)

            if uid.password == password:  
                contaxt = {
                    'msg': 'Successfully logged'
                }
                return redirect(index)
            else:
                contaxt = {
                    'msg': 'Wrong password'
                }
        except User_Detail.DoesNotExist:
            
            contaxt = {
                'msg': 'Invalid email, please go to the registration form'
            }

        return render(request, "login.html", contaxt)

    else:
        return render(request, "login.html")
    
    return render(request, "login.html")

# ___________________________________________________________Sign-Up page________________________________________________________

def signup(request):
    if request.method=='POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        print(f_name, l_name, email, password, c_password, phone, address)
        print(f"Password: '{password}', Confirm Password: '{c_password}'")
        
        try:
            uid = User_Detail.objects.get(email=email)  
            contaxt = {
                "msg": "Email already exists"
                }
            return render(request, "signup.html", contaxt)
        
        except User_Detail.DoesNotExist: 
            
            if c_password != password:
                contaxt = {
                    "msg": "Enter correct password"
                    }
                return render(request, "signup.html", contaxt)
            
            else:
                contaxt={
                "msg":"Welcome to our family !"
                }
                User_Detail.objects.create(f_name=f_name, l_name=l_name, email=email, password=password, c_password=c_password, phone=phone, address=address)
                return render(request,"signup.html",contaxt)
    else:      
        return render(request, "signup.html")

# ___________________________________________________________Main page________________________________________________________
def main(request):
    dept_id = Department.objects.all()
    print("Department Data:", dept_id)
    context = {
        "dept_id" : dept_id,
        }
    return render(request, 'main.html', context)

# ___________________________________________________________Shop-Details page________________________________________________________

def open_details(request, id):
    product = get_object_or_404(Product, id=id)  
    total_cart_price = Cart.get_cart_total()

    context = {
        "product": product,
        "total_cart_price": total_cart_price
    }
    return render(request, 'shop_details.html', context)

# ___________________________________________________________Shop-Grid page________________________________________________________
def shop_grid(request):
    
    dept_id = Department.objects.all()
    product_id = Product.objects.all()
    cid=Color_filter.objects.all()
    sid = Size_filter.objects.all()
    total_cart_price = Cart.get_cart_total()
    
    
    shop_id = request.GET.get('shop_id')
    p_color=request.POST.get('p_color')
    p_count = sid.annotate(count=Count('product'))
    
    print(p_color)
    
    print("Shop ID:", shop_id)
    print("Department Data:", dept_id)
    print("Product Data:", product_id)
    
    email = request.session.get('email')

    if email:
        try:
            uid = User_Detail.objects.get(email=email)
            wishlist_ids = Wishlist.objects.filter(user=uid).values_list('product__id', flat=True)
        except User_Detail.DoesNotExist:
            wishlist_ids = []
    else:
        wishlist_ids = []
    
    if shop_id:
        product_id = Product.objects.filter(Department=shop_id)
    else:
        product_id = Product.objects.all()
           
    context = {
        "dept_id" : dept_id,
        "product_id" : product_id,
        "shop_id" : shop_id,
        "sid":sid,
        "wishlist_ids": wishlist_ids,
        "p_count": p_count,
        "cid":cid,
        "p_color":p_color,
        "total_cart_price": total_cart_price,
        
        }
    return render(request, 'shop_grid.html',context)

def get_color(request):
    dept_id = Department.objects.all()
    product_id = Product.objects.all()
    cid=Color_filter.objects.all()
    sid = Size_filter.objects.all()
    
    
    cf=request.POST.get('p_color')
    
    l=[]
    if cf:
        product_id = Product.objects.filter(Color_filter__p_color=cf)
        l.extend(product_id)
        print(product_id)
    else:
        product_id=Product.objects.all()
    
    p_count = sid.annotate(count=Count('product'))
    
    context={
        "dept_id" : dept_id,
        "product_id": product_id,
        "cid": cid,
        "cf": cf,
        "sid":sid,
        "p_count": p_count,
    }
    return render(request,'shop_grid.html',context)

def get_size(request):
    dept_id = Department.objects.all()
    product_id = Product.objects.all()
    cid=Color_filter.objects.all()
    sid = Size_filter.objects.all()
    
    sf = request.POST.get('p_size')
        
    l=[]
    if sf:
        product_id = Product.objects.filter(Size_filter__p_size=sf)
        l.extend(product_id)
        print(product_id)
    else:
        product_id=Product.objects.all()
    
    p_count = sid.annotate(count=Count('product'))
        
    context ={
        "dept_id" : dept_id,
        "product_id": product_id,
        "cid":cid,
        "sid":sid,
        "sf": sf,
        "p_count": p_count,
    }
    return render(request, 'shop_grid.html', context)

def price_range(request):
    dept_id = Department.objects.all()
    product_id = Product.objects.all()
    cid=Color_filter.objects.all()
    sid=Size_filter.objects.all()
    
    if request.POST:
        min_price = request.POST['min_price']
        max_price = request.POST['max_price']
        
        product_id=Product.objects.filter(product_price__lte=max_price[1:],product_price__gte=min_price[1:])
        
        print(min_price)
        print(max_price)
        print(product_id)
        
        context ={
            # "dept_id" : dept_id,
            "product_id": product_id,
            # "cid":cid,
            # "sid":sid,
            "min_price": min_price,
            "max_price": max_price,
        }
        return render(request, 'shop_grid.html', context) 
    else:
        context ={
            # "dept_id" : dept_id,
            "product_id": product_id,
            # "cid":cid,
            # "sid":sid,
            "min_price": None,
            "max_price": None,
        }
        return render(request, 'shop_grid.html', context) 
    
def wishlist(request, id):
    
    # uid=Register.objects.get(email = request.POST.get('email'))
    product_id = Product.objects.get(id=id)
    peid = Wishlist.objects.filter(product = product_id).exists()
    
    if peid:
        Wishlist.objects.filter(product = product_id).delete()
        return redirect('shop_grid')
    else:
        Wishlist.objects.create(product=product_id,  
                                product_image=product_id.product_image, 
                                product_name=product_id.product_name, 
                                product_price=product_id.product_price)
        return redirect('shop_grid')

# ___________________________________________________________Shoping Cart page________________________________________________________

def shoping_cart(request):
    dept_id = Department.objects.all()
    cart_items = Cart.objects.all()
    total_cart_price = Cart.get_cart_total()
    
    print("Department Data:", dept_id)
    context = {
        "dept_id" : dept_id,
        "cart_items": cart_items,
        'total_cart_price': total_cart_price,
        }
    return render(request, 'shoping_cart.html', context)

def add_to_cart(request,id):
    
    dept_id = Department.objects.all()
    product_id = Product.objects.get(id=id)
    
    peid = Cart.objects.filter(product=product_id).first()
    print(peid)
    
    if peid :
        peid.quantity +=1
        peid.total_price = peid.quantity * peid.product_price
        peid.save()
    
    else:
        Cart.objects.create(product=product_id,  
                        product_name=product_id.product_name,  
                        product_image=product_id.product_image,  
                        product_price=product_id.product_price,  
                        quantity=1, 
                        total_price=product_id.product_price)

    return redirect('shoping_cart')
   
def pluscart(request,id):
    cart_item = Cart.objects.get(id=id)
    cart_item.quantity = cart_item.quantity + 1
    cart_item.total_price = cart_item.quantity * cart_item.product_price
    cart_item.save()
    return redirect("shoping_cart")

def minuscart(request,id):
    cart_item = Cart.objects.get(id=id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.total_price = cart_item.quantity * cart_item.product_price
        cart_item.save()
    else:
        cart_item.delete()
    return redirect("shoping_cart")

def update_cart(request, id):
    cart_item = Cart.objects.get(id=id)
    cart_items = Cart.objects.all()
    print(cart_item)
    
    if request.method == "POST":
        quantity = int(request.POST.get("quantity"))
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.total_price = cart_item.quantity * cart_item.product_price
            cart_item.save()
        else :
            cart_item.delete()
        
        return redirect('shoping_cart')
    
    context = {
        "peid":peid,
        "cart_items" : cart_items,
    }
    return render(request, 'shoping_cart', context)

def remove_cart(request, id):
    cart_item = get_object_or_404(Cart, id=id)  
    cart_item.delete()
    return redirect('shoping_cart')  
