from django.shortcuts import render
from django.templatetags.static import static

def index_page(request):
    context = {
        "page_name": "Туристическое агентство",
        "tours": [
            {
                "title": "Экскурсия по городу",
                "img": static("images/city-tour.jpg"),
            },
            {
                "title": "Горный поход",
                "img": static("images/mountain-hike.jpg"),
            },
            {
                "title": "Круиз по морю",
                "img": static("images/cruise.jpg"),
            },
            {
                "title": "Сафари в пустыне",
                "img": static("images/safari.jpg"),
            }
        ]
    }
    return render(request, 'index.html', context)