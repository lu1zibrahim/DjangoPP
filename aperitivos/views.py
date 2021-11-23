from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 647338996},
        'impressao': {'titulo': 'Impressão 3d', 'vimeo_id': 648966504},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
