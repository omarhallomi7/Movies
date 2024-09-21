# movies/views.py
from django.shortcuts import render, get_object_or_404,redirect
from .models import Movie, Review
from .forms import ReviewForm

# function to render all movies that the admin added  
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

# function to render movie detail
def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug) # getting the movie object that includes all movie detailes
    if request.method == 'POST': # if user want to submit a review
        if request.user.is_authenticated: # checking user auth 
            form = ReviewForm(request.POST) # getting the review form
            if form.is_valid(): # checking if the form is valid , if yes review saved and movie detail redirecting with the new review
                review = form.save(commit=False)
                review.movie = movie
                review.user = request.user
                review.save()
                return redirect('movies:movie_detail', slug=slug)
        else: # if user is not logged in , user can't submit a review  
            return redirect('accounts:login')
    else: # if the request is NOT post request
        form = ReviewForm() # getting the form
    reviews = Review.objects.filter(movie=movie)  # Get all reviews for the movie
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'review_form': form, 'reviews': reviews}) # rendring movie detail include the review form and all previous reviews (if any)

# function to submit review 
def submit_review(request, slug):
    movie = get_object_or_404(Movie, slug=slug) # getting the movie object that includes all movie detailes
    if request.method == 'POST': # if user want to submit a review
        if request.user.is_authenticated: # checking user auth
            form = ReviewForm(request.POST) # getting the form
            if form.is_valid(): # checking if the form is valid , if yes review saved and movie detail redirecting with the new review
                review = form.save(commit=False)
                review.movie = movie
                review.reviewer_name = request.user.username  
                review.save()
                return redirect('movies:movie_detail', slug=slug)
        else: # if user is not logged in , user can't submit a review
            return redirect('accounts:login')
    else: # if the request is NOT post request
        form = ReviewForm() # getting the form
    return render(request, 'movies/submit_review.html', {'form': form, 'movie': movie})

