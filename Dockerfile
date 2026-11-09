# استخدام نسخة بايثون خفيفة وآمنة
FROM python:3.10-slim

# إنشاء مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملف المتطلبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# تشغيل التطبيق بدون صلاحيات الجذر (Root) لزيادة الأمان حسب متطلبات المشروع
RUN useradd -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# المنفذ اللي بيشتغل عليه التطبيق
EXPOSE 8080

# أمر تشغيل التطبيق
CMD ["python", "app.py"]
