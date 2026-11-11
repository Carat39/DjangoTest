from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Band,Listing
from listings.forms import ContactUsForm,BandForm,ListingForm
from django.core.mail import send_mail
from django.contrib import messages

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

def home(request):
    return render(request,'navigation/home.html')

def band_list(request):
    bands = Band.objects.all()
    return render(request,'listings/band_list.html',{'bands': bands})

def band_detail(request, band_id): #Y'a une fonction id intégrée à python
    try:
        the_band = Band.objects.get(id = band_id)
        listings = the_band.listing_set.all()
        return render(request,'listings/band_detail.html', {'band' : the_band, 'listings':listings})

    except Band.DoesNotExist:
        return render(request,'errors/objectserrors.html',{'id':band_id})

def band_add(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = BandForm(request.POST)
    
        if form.is_valid(): #Action quand tous les champs sont valides form.cleaned_data = dict du form
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide (on arrive sur la page)
            form = BandForm()

    return render(request,
        'listings/band_add.html',
        {'form': form})  # passe ce formulaire au gabarit

def band_modify(request, band_id):
    try:
        the_band = Band.objects.get(id = band_id)
        if request.method == 'POST':
            form = BandForm(request.POST,instance=the_band)
            if form.is_valid(): #Action quand tous les champs sont valides form.cleaned_data = dict du form
                band = form.save()
                return redirect('band-detail', band.id)
            return render(request,'listings/band_modify.html', {'form':form, 'band':the_band})

        else:
            # ceci doit être une requête GET, donc créer un formulaire vide (on arrive sur la page)
            form = BandForm(instance=the_band)
            
            return render(request,'listings/band_modify.html',{'form': form, 'band':the_band})  # passe ce formulaire au gabarit
    
    except Band.DoesNotExist:
        return render(request,'errors/objectserrors.html',{'id':band_id})

def band_delete(request, band_id):
    try:
        the_band = Band.objects.get(id = band_id)
        if request.method == 'POST':
            action = request.POST.get('action') #On regarde la valeur de l'action
            if action == 'Supprimer':
                the_band.delete()
                messages.success(request, f"Le groupe « {the_band.name} » a été supprimé.")
            return redirect('band-list')
        
        return render(request,'listings/band_delete.html',{'band':the_band})  # passe ce formulaire au gabarit
    
    except Band.DoesNotExist:
        return render(request,'errors/objectserrors.html',{'id':band_id})


def about(request):
    return render(request,'listings/about.html')

def listing_list(request):
    listings = Listing.objects.all()
    return render(request,'listings/listing_list.html',{'listings': listings})

def listing_detail(request, listing_id): #Y'a une fonction id intégrée à python
    try:
        the_listing = Listing.objects.get(id = listing_id)
        return render(request,'listings/listing_detail.html', {'listing' : the_listing})

    except Listing.DoesNotExist:
        return render(request,'errors/objectserrors.html',{'id':listing_id})

def listing_add(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ListingForm(request.POST)
    
        if form.is_valid(): #Action quand tous les champs sont valides form.cleaned_data = dict du form
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide (on arrive sur la page)
            form = ListingForm()

    return render(request,
        'listings/listing_add.html',
        {'form': form})  # passe ce formulaire au gabarit

def listing_modify(request, listing_id):
    try:
        the_listing = Listing.objects.get(id = listing_id)
        if request.method == 'POST':
            form = ListingForm(request.POST,instance=the_listing)
            if form.is_valid(): #Action quand tous les champs sont valides form.cleaned_data = dict du form
                listing = form.save()
                return redirect('listing-detail', listing.id)
            return render(request,'listings/listing_modify.html', {'form':form, 'listing':the_listing})

        else:
            # ceci doit être une requête GET, donc créer un formulaire vide (on arrive sur la page)
            form = ListingForm(instance=the_listing)
            
            return render(request,'listings/listing_modify.html',{'form': form, 'listing':the_listing})  # passe ce formulaire au gabarit
    
    except Listing.DoesNotExist:
        return render(request,'errors/objectserrors.html',{'id':listing_id})

def listing_delete(request, listing_id):
    try:
        the_listing = Listing.objects.get(id = listing_id)
        if request.method == 'POST':
            action = request.POST.get('action') #On regarde la valeur de l'action
            if action == 'Supprimer':
                the_listing.delete()
                messages.success(request, f"Le groupe « {the_listing.title} » a été supprimé.")
            return redirect('listing-list')

        return render(request,'listings/listing_delete.html',{'listing':the_listing})  # passe ce formulaire au gabarit
    
    except Listing.DoesNotExist:
        return render(request,'errors/objectserrors.html',{'id':listing_id})

def voir_profil_utilisateur(request, username):
  # Récupère l'utilisateur ou renvoie une erreur 404 s'il n'existe pas
  utilisateur = get_object_or_404(User, username=username)
  return render(request, 'listings/profil.html', {'utilisateur': utilisateur})
"""
def mon_profil(request):
  users = User.objects.all()
  return render(request, 'listings/profil.html', {'users': users})
"""

def contact(request):
    if request.method == 'POST':
    # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid(): #Action quand tous les champs sont valides form.cleaned_data = dict du form
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
            #!!! il faut configurer un serveur SMTP
            print("print ",form.cleaned_data)
            return redirect('email-sent')
    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    return render(request,
            'listings/contact.html',
            {'form': form})  # passe ce formulaire au gabarit

def email_sent(request):
    return render(request,'listings/email_sent.html')