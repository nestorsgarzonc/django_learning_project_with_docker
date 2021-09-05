from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
posts = [
    {
        'name': 'NW',
        'user': 'SG',
        'timestamp': datetime.now().strftime(r"%b %dth  %Y %H:%M"),
        'picture': 'https://picsum.photos/id/23/200/200',
    }
]


def list_posts(request):
    # content = []
    # for post in posts:
    #     content.append(
    #         f"""
    #         <div class="post">
    #             <h1>{post['name']}</h1>
    #             <figure><img src="{post['picture']}"></figure>
    #             <p>{post['user']}</p>
    #             <i><small>{post['timestamp']}</small></i>
    #         </div>
    #         """
    #     )
    # return HttpResponse(content, content_type='text/html')
    return render(request, 'feed.html', {'posts': posts})
