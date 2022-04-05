from django.shortcuts import render


def main(request):
    menu_links = [
        {"href": "mainapp:main", "name": "Design"},
        {"href": "mainapp:main", "name": "Collaborate"},
        {"href": "mainapp:main", "name": "Apps"},
        {"href": "mainapp:main", "name": "Resources"},
        {"href": "mainapp:main", "name": "Pricing"},
    ]

    title = 'Your Website'

    content = {
        'title': title,
        'menu_links': menu_links,
    }
    return render(request, 'mainapp/main.html', content)
