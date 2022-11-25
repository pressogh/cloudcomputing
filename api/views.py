from django.shortcuts import render


def PostListView(request):
    if request.method == 'GET':
        return render(request, 'main.html')


def PostDetailView(request, pk):
    if request.method == 'GET':
        return render(request, 'post_detail.html')
