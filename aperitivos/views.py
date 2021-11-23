from django.shortcuts import render


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.vimeo_id = vimeo_id
        self.titulo = titulo
        self.slug = slug


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', 647338996),
    Video('impressao', 'Impressão 3d', 648966504)
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
