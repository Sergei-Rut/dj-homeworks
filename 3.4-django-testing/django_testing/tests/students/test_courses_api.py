import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from django.urls import reverse
from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


# проверка получения 1го курса
@pytest.mark.django_db
def test_get_one_course(client, course_factory):
    courses = course_factory(_quantity=1)

    course = Course.objects.first()
    url = reverse('courses-detail', args=(course.id,))
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['name'] == course.name


# проверка получения списка курсов
@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    courses = course_factory(_quantity=2)

    url = reverse('courses-list')
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


# проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_get_id_course(client, course_factory):
    courses = course_factory(_quantity=5)

    url = reverse('courses-list')
    response = client.get(url, data={'id': courses[0].id})

    assert response.status_code == 200


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_get_name_course(client, course_factory):
    courses = course_factory(_quantity=5)

    url = reverse('courses-list')
    response = client.get(url, data={'name': courses[0].name})

    assert response.status_code == 200


# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()

    url = reverse('courses-list')
    response = client.post(url, data={'name': 'CourseTheBST'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


# тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(name='CourseOne')

    url = reverse('courses-detail', args=(course.id,))
    response = client.patch(url, data={'name': 'CourseTwo'})

    assert response.status_code == 200


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(name='CourseOne')

    url = reverse('courses-detail', args=(course.id,))
    response = client.delete(url)

    assert response.status_code == 204
