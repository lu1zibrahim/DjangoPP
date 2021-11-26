import pytest
from django.test import Client  # noqa
from django.urls import reverse

from djangopp.django_assertions import assert_contains
from model_bakery import baker

from modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_titulo_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_titulo_modulo_url_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')


def test_vimeo(resp, aula: Aula):
    assert_contains(resp, f"https://player.vimeo.com/video/{aula.vimeo_id}")