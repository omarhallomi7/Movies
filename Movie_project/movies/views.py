from django.shortcuts import render, get_object_or_404,redirect
from .models import Movie, Review
from .forms import ReviewForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.movie = movie
                review.user = request.user
                review.save()
                return redirect('movies:movie_detail', slug=slug)
        else:
            return redirect('accounts:login')
    else:
        form = ReviewForm()
    reviews = Review.objects.filter(movie=movie)  # Get all reviews for the movie
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'review_form': form, 'reviews': reviews})

def submit_review(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.movie = movie
                review.reviewer_name = request.user.username  # Capture the username
                review.save()
                return redirect('movies:movie_detail', slug=slug)
        else:
            return redirect('accounts:login')
    else:
        form = ReviewForm()
    return render(request, 'movies/submit_review.html', {'form': form, 'movie': movie})

