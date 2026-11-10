import pytest
from app import app  # نفترض أن ملف التطبيق الرئيسي اسمه app.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# 1. اختبار الناتج الطبيعي
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

# 2. اختبار نقطة الصحة
def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    # تأكد من أن الرد يحتوي على نجاح أو حالة تعمل
    assert b"healthy" in response.data.lower() or response.json is not None

# 3. اختبار حالة استثنائية أو خطأ (مثلاً صفحة غير موجودة)
def test_not_found(client):
    response = client.get('/nonexistent-page')
    assert response.status_code == 404
